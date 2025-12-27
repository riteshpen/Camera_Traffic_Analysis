import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import gc

# Check and install SHAP if necessary
try:
    import shap
except ImportError:
    print("SHAP library not found. Attempting to install...")
    try:
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "shap"])
        import shap
        print("SHAP installed successfully.")
    except Exception as e:
        print(f"Failed to install SHAP. Error: {e}")
        shap = None 

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV

# --- 1. MEMORY-OPTIMIZED Data Loading ---

# Specify only columns we need
needed_cols = [
    'Read Date', 'Intersection Name', 'Movement', 'Volume',
    'Speed Average (Miles Per Hour)', 'Heavy Vehicle',
    'Month', 'Day', 'Year', 'Day of Week'
]

try:
    print("Loading traffic data for 2019 only (ULTRA memory-optimized)...")
    chunk_size = 100000  # Smaller chunks
    chunks = []
    total_loaded = 0
    
    for i, chunk in enumerate(pd.read_csv("./Camera_Traffic_Counts2_20250918.csv",
                                          usecols=needed_cols,  # Only load needed columns
                                          chunksize=chunk_size,
                                          engine='python',
                                          on_bad_lines='skip'), start=1):
        # Parse date and filter for 2019 immediately
        chunk['Date_Time'] = pd.to_datetime(chunk['Read Date'], format='mixed', errors='coerce')
        chunk = chunk[chunk['Date_Time'].dt.year == 2019]
        
        # Sample 20% of data to reduce size dramatically
        if len(chunk) > 0:
            chunk = chunk.sample(frac=0.2, random_state=42)  # Keep only 20%
            chunks.append(chunk)
            total_loaded += len(chunk)
            print(f"  Chunk {i}: {len(chunk):,} rows sampled (Total: {total_loaded:,})")
        
        # Force garbage collection every 5 chunks
        if i % 5 == 0:
            gc.collect()
    
    traffic_data = pd.concat(chunks, ignore_index=True)
    del chunks  # Free memory
    gc.collect()
    print(f"✓ Traffic data: {len(traffic_data):,} records (20% sample)\n")
    
    # Load weather data with only needed columns
    weather_cols = ['datetime', 'windspeed', 'precip', 'visibility', 'temp', 'snow']
    print("Loading weather data...")
    weather_data = pd.read_csv("./Austin 2019-01-01 to 2023-07-22.csv",
                               usecols=weather_cols,
                               engine='python',
                               on_bad_lines='skip')
    print(f"✓ Weather data: {len(weather_data):,} records")
    
    # Filter weather for 2019
    weather_data["datetime"] = pd.to_datetime(weather_data["datetime"], format='mixed', errors='coerce')    
    weather_2019 = weather_data[weather_data["datetime"].dt.year == 2019].copy()
    del weather_data
    gc.collect()
    
    # Extract M/D/Y for merging
    weather_2019['Month'] = weather_2019['datetime'].dt.month
    weather_2019['Day'] = weather_2019['datetime'].dt.day
    weather_2019['Year'] = weather_2019['datetime'].dt.year
    weather_2019 = weather_2019.drop(columns=['datetime'])

    # Merge
    merged_df = pd.merge(traffic_data, weather_2019, on=["Month", "Day", "Year"], how="inner")
    del traffic_data, weather_2019
    gc.collect()
    print(f"After merge: {len(merged_df):,} records")
    
    # Convert to efficient data types
    merged_df['Heavy Vehicle'] = merged_df['Heavy Vehicle'].astype('category')
    merged_df['Day of Week'] = merged_df['Day of Week'].astype('category')
    merged_df['snow'] = merged_df['snow'].astype('category')
    print(f"Memory usage: {merged_df.memory_usage(deep=True).sum() / 1024**2:.1f} MB")
    
except FileNotFoundError as e:
    print(f"Error loading files: {e}")
    raise

# --- 2. Sort Data ---
merged_df = merged_df.sort_values(by=['Intersection Name', 'Movement', 'Date_Time']).reset_index(drop=True)

# --- 3. Feature Engineering ---
GROUP_COLS = ['Intersection Name', 'Movement']
TARGET_COL = 'Speed Average (Miles Per Hour)'
VOLUME_COL = 'Volume'

print("\n--- Creating Lagged Features ---")

# Only most important lags (1 and 4)
merged_df['Lag_1_Speed'] = merged_df.groupby(GROUP_COLS)[TARGET_COL].shift(1)
merged_df['Lag_4_Speed'] = merged_df.groupby(GROUP_COLS)[TARGET_COL].shift(4)
merged_df['Lag_1_Volume'] = merged_df.groupby(GROUP_COLS)[VOLUME_COL].shift(1)

# Holiday Feature
def create_holiday_flag(df):
    holidays_2019 = [
        ('01-01', 'New Year\'s Day'), ('01-21', 'MLK Day'), ('02-18', 'Presidents\' Day'),
        ('05-27', 'Memorial Day'), ('07-04', 'Independence Day'), ('09-02', 'Labor Day'),
        ('10-14', 'Columbus Day'), ('11-11', 'Veterans Day'), ('11-28', 'Thanksgiving'),
        ('12-25', 'Christmas Day')
    ]
    df['date_key'] = df['Date_Time'].dt.strftime('%m-%d')
    df['Is_Holiday'] = df['date_key'].apply(lambda x: x in [h[0] for h in holidays_2019]).astype('category')
    df = df.drop(columns=['date_key'])
    return df

merged_df = create_holiday_flag(merged_df)

# --- 4. Clean Data ---
rows_before = len(merged_df)
merged_df = merged_df.dropna(subset=[TARGET_COL, 'Lag_1_Speed', 'Lag_4_Speed', 'Lag_1_Volume'])
print(f"Dropped {rows_before - len(merged_df):,} rows with NaN")

# --- 5. Chronological Split ---
train_end = '2019-09-30'
val_end = '2019-11-30'

train_df = merged_df[merged_df['Date_Time'] <= train_end]
val_df = merged_df[(merged_df['Date_Time'] > train_end) & (merged_df['Date_Time'] <= val_end)]
test_df = merged_df[merged_df['Date_Time'] > val_end]

print(f"\n--- Data Split ---")
print(f"Train: {len(train_df):,} | Val: {len(val_df):,} | Test: {len(test_df):,}")

# Define Features (removed Lag_3_Speed)
feature_cols = [
    'windspeed', 'precip', 'Heavy Vehicle', 'visibility', 'temp', 
    'Lag_1_Volume', 'Lag_1_Speed', 'Lag_4_Speed',
    'snow', 'Day of Week', 'Is_Holiday'
]

X_train, y_train = train_df[feature_cols], train_df[TARGET_COL]
X_val, y_val = val_df[feature_cols], val_df[TARGET_COL]
X_test, y_test = test_df[feature_cols], test_df[TARGET_COL]

del merged_df, train_df, val_df, test_df
gc.collect()

# --- 6. Preprocessing ---
numerical_features = ['windspeed', 'precip', 'visibility', 'temp', 
                      'Lag_1_Volume', 'Lag_1_Speed', 'Lag_4_Speed']
categorical_features = ['Heavy Vehicle', 'snow', 'Day of Week', 'Is_Holiday'] 

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_features)
    ],
    remainder='drop'
)

# --- 7. Simplified Hyperparameter Tuning ---
rf_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                              ('model', RandomForestRegressor(random_state=42, n_jobs=-1))])

# MUCH smaller grid for speed
param_grid = {
    'model__n_estimators': [50, 100],
    'model__max_depth': [10, 20]
}

X_full_train_val = pd.concat([X_train, X_val])
y_full_train_val = pd.concat([y_train, y_val])
train_indices = list(range(len(X_train)))
val_indices = list(range(len(X_train), len(X_full_train_val)))
custom_cv = [(train_indices, val_indices)] 

print("\n--- Hyperparameter Tuning ---")
grid_search = GridSearchCV(rf_pipeline, param_grid, cv=custom_cv, 
                           scoring='neg_mean_squared_error', refit=False, 
                           n_jobs=-1, verbose=1)

try:
    grid_search.fit(X_full_train_val, y_full_train_val)
    best_params = grid_search.best_params_
    print(f"Best parameters: {best_params}")
except Exception as e:
    best_params = {'model__n_estimators': 50, 'model__max_depth': 10}
    print(f"GridSearch failed, using defaults: {best_params}")

# --- 8. Train Final Model ---
best_rf_model = RandomForestRegressor(
    n_estimators=best_params.get('model__n_estimators', 50),
    max_depth=best_params.get('model__max_depth', 10),
    random_state=42,
    n_jobs=-1
)

best_pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('model', best_rf_model)])
best_pipeline.fit(X_full_train_val, y_full_train_val)

# --- 9. Evaluation ---
print("\n--- Model Performance ---")

y_val_pred = best_pipeline.predict(X_val)
val_rmse = np.sqrt(mean_squared_error(y_val, y_val_pred))
val_r2 = r2_score(y_val, y_val_pred)
print(f"Validation RMSE: {val_rmse:.4f} | R²: {val_r2:.4f}")

y_test_pred = best_pipeline.predict(X_test)
test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
test_r2 = r2_score(y_test, y_test_pred)
print(f"Test RMSE: {test_rmse:.4f} | R²: {test_r2:.4f}")

# --- 10. Prediction vs Actual Plot ---
plt.figure(figsize=(10, 6))
sample_size = min(10000, len(y_test))
sample_idx = np.random.choice(len(y_test), sample_size, replace=False)
plt.scatter(y_test.iloc[sample_idx], y_test_pred[sample_idx], alpha=0.3, s=1)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual Speed (MPH)')
plt.ylabel('Predicted Speed (MPH)')
plt.title('Predicted vs Actual Speed - Test Set')
plt.tight_layout()
plt.savefig('prediction_vs_actual.png', dpi=300, bbox_inches='tight')
print("\nSaved: prediction_vs_actual.png")
plt.close()

# --- 11. SHAP (Very Small Sample) ---
if shap:
    print("\n--- SHAP Interpretation ---")
    
    X_test_processed = best_pipeline.named_steps['preprocessor'].transform(X_test)
    ohe_feature_names = list(best_pipeline.named_steps['preprocessor'].transformers_[1][1].get_feature_names_out(categorical_features))
    feature_names = numerical_features + ohe_feature_names
    X_test_processed_df = pd.DataFrame(X_test_processed, columns=feature_names)
    
    # Only 100 samples for SHAP
    sample_size = min(100, len(X_test_processed_df))
    X_sample = X_test_processed_df.sample(sample_size, random_state=42)
    print(f"Computing SHAP for {sample_size} samples...")

    explainer = shap.TreeExplainer(best_pipeline.named_steps['model'])
    shap_values = explainer.shap_values(X_sample)

    plt.figure(figsize=(10, 8))
    shap.summary_plot(shap_values, X_sample, feature_names=feature_names, show=False)
    plt.title('SHAP Summary Plot: Feature Impact on Speed')
    plt.tight_layout()
    plt.savefig('shap_summary.png', dpi=300, bbox_inches='tight')
    print("Saved: shap_summary.png")
    plt.close()

# --- 12. Feature Importance ---
print("\n--- Feature Importance ---")
ohe_feature_names = list(best_pipeline.named_steps['preprocessor'].transformers_[1][1].get_feature_names_out(categorical_features))
feature_names = numerical_features + ohe_feature_names

importances = best_pipeline.named_steps['model'].feature_importances_
feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False).head(15)

plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=feature_importance_df)
plt.title('Top 15 Feature Importances')
plt.tight_layout()
plt.savefig('feature_importance.png', dpi=300, bbox_inches='tight')
print("Saved: feature_importance.png")
plt.close()

print("\nTop 10 Features:")
for idx, row in feature_importance_df.head(10).iterrows():
    print(f"  {row['Feature']}: {row['Importance']:.4f}")

# --- 13. Save Model ---
joblib.dump(best_pipeline, 'best_average_speed_model.pkl')
print("\n✓ Model saved as 'best_average_speed_model.pkl'")
print("✓ All plots saved successfully")