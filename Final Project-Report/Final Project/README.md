# 🚦 Austin Traffic Analysis: Final Project

**Predicting Traffic Volume to Reduce Congestion at Austin Intersections**  
*By Team 11:* Ritesh Penumatsa, John Trelford, Lucas Chiang, Travis Welsh, and Brian Pham

---

## 📌 Project Summary

This project investigates **factors driving traffic congestion at Austin intersections** using 15-minute interval traffic data from GRIDSMART optical detectors. We developed predictive models to identify key features influencing traffic volume, enabling individuals to make more informed driving decisions and reduce time wasted on the road.

### Research Question
**"What factors drive congestion at intersections?"**

---

## 📊 Dataset
- **File**: Camera_Traffic_Counts2_20250918.csv
- **Source**: GRIDSMART optical detectors at Austin intersections
- **Time Period**: January 1, 2019 - December 31, 2019
- **Original Size**: 82.1 million rows (filtered to 14.7 million)
- **Filtering Rationale**: Avoids COVID-19 pandemic effects and computational constraints
---
- **File**: Austin 2019-01-01 to 2023-07-22.csv
- **Source**: Austin weather forecast
- **Time Period**: January 1, 2019 - July 22, 2023 (filtered to stop at December 31, 2019)
- **Original Size**: 1665 rows
- **Filtering Rationale**: Avoids COVID-19 pandemic effects and computational constraints

### Data Access
The full dataset is available via [Google Drive](https://drive.google.com/drive/u/3/folders/1MASJueZORSwywnJHiAhAmR_5JKQCizZw).

## 📊 Dataset Overview

### Primary Data Sources
- **Camera Traffic Counts**: 15-minute interval traffic data by intersection in Austin
- **Visual Crossing Weather Data**: Austin climate conditions by day

### Data Processing
- **Original Size**: 82.1 million rows (2014-2023)
- **Filtered to**: 14,717,624 rows from 2019 only
- **Rationale**: Avoids COVID-19 pandemic interference and computational constraints
- **Final Shape**: (14,717,624, 19)

### Target Variable
- **Volume**: Number of vehicles in 15-minute intervals

### Feature Selection
| Feature | Justification | Processing |
|---------|---------------|------------|
| Day of the Week | Travel patterns vary weekly | One-hot encoded |
| Holiday | Patterns deviate around holidays | Binary indicator |
| Precipitation | Severe weather affects travel | Continuous |
| Heavy Vehicle Presence | Larger vehicles affect turns | Binary |
| Time of Day | Morning/afternoon rush patterns | Continuous (hour) |
| Lagged Volumes (1,2,4) | Captures short-term dynamics | Time-lagged features |
| Visibility | Low visibility affects safety | Continuous |
| Temperature | Extreme temperatures affect the likelihood of driving | Continuous |

---

## 🏗️ Model Architecture

### Temporal Data Splitting
To avoid temporal leakage and simulate real-world prediction:
- **Training Set**: January-September 2019
- **Validation Set**: October-November 2019  
- **Testing Set**: December 2019
- **Note**: k-fold CV was inappropriate as it breaks time order

### Model Selection

#### 1. Ridge Regression
- **Purpose**: Interpretable linear model with regularization
- **Advantages**: 
  - Appropriate for temporal data with smooth trends
  - Easy coefficient interpretation
  - Low computational cost
  - Avoids overfitting (L2 regularization)
- **Regularization**: α = 0.001 (tuned on validation set)

#### 2. Random Forest
- **Purpose**: Capture complex, non-linear relationships
- **Advantages**:
  - Resistant to outliers
  - Models complex feature interactions
  - Higher predictive accuracy
- **Hyperparameters**:
  - n_estimators = 50
  - max_depth = 9
  - min_samples_leaf = 2
  - min_samples_split = 5

### Justification of Feature Set
1. **Nature of Outcome**: Volume is real-valued
2. **Data Availability**: Features available for every observation
3. **Data Integrity**: No data leakage
4. **Causal Structure**: All predictors causally precede volume
5. **Predictive Signal**: Expected meaningful relationships with volume

---

## 📈 Results & Analysis

### Statistical Significance (OLS)
| Feature | OLS Coefficient | P-Value |
|---------|----------------|---------|
| Time (of day) | 0.2015 | 0.0000 |
| lag_2 | 0.28597 | 0.0000 |
| lag_1 | 0.11773 | 0.0000 |
| lag_4 | 0.13533 | 0.0000 |
| Visibility | 0.03929 | 0.0113 |
| Temperature | 0.01240 | 2.80e-21 |
| Heavy Vehicle | -18.0048 | 0.0000 |

### Ridge Regression Results (α=0.001)
- **R²**: 0.2284 (explains 22.84% of variance)
- **RMSE**: 50.51 units of traffic volume
- **Top 5 Features** (by standardized coefficient magnitude):
  1. Lag_2 (15-30 minutes prior volume)
  2. Heavy Vehicle Presence
  3. Lag_4 (45-60 minutes prior volume)
  4. Lag_1 (0-15 minutes prior volume)
  5. Time of day

### Random Forest Results
- **R²**: 0.3263 (explains 32.63% of variance)
- **RMSE**: 47.16 units of traffic volume
- **Top Features** (SHAP importance):
  1. Lagged volumes (past 15-60 minutes)
  2. Vehicle type (heavy vs. regular)
  3. Time of day
  4. Weather conditions
  5. Day of week

---

## ⚡ Energy & Computational Efficiency

| Model | Training Fits | Avg. Training Time | Energy Consumed | CO₂ Emitted |
|-------|--------------|-------------------|-----------------|-------------|
| Ridge Regression | 1 | 0.5262s | 0.000007 kWh | 0.000003 kg CO₂ |
| Random Forest | 1 | 57.1712s | 0.000794 kWh | 0.000318 kg CO₂ |

**Trade-off Analysis**: While Ridge Regression is dramatically more efficient (100× faster, 100× less energy), Random Forest provides superior predictive performance. Given our models don't need frequent retraining, we prioritize accuracy over efficiency.

---

## 🎯 Model Comparison & Selection

### Performance Metrics
| Metric | Random Forest | Ridge Regression |
|--------|---------------|------------------|
| **R²** | 0.3263 | 0.2284 |
| **RMSE** | 47.16 | 50.51 |

### Final Model Choice: **Random Forest**
**Rationale**:
1. **Higher R²**: Explains 32.63% vs. 22.84% of variance
2. **Lower RMSE**: 47.16 vs. 50.51 units of error
3. **Alignment with goals**: Minimizes large mispredictions (critical for traffic planning)
4. **Practical considerations**: Infrequent retraining makes computational cost acceptable

**Ridge Regression Role**: Provided stable, interpretable coefficients for causal understanding

---

## 🔍 Key Insights & Practical Implications

### 1. Temporal Persistence is Key
- **Finding**: Recent traffic volume (past 15-60 minutes) is the strongest predictor
- **Interpretation**: Traffic queues "snowball" - busy intersections stay busy
- **Recommendation**: If an intersection is congested, expect it to remain congested in the short term

### 2. Heavy Vehicle Presence Reduces Congestion
- **Finding**: Negative correlation with volume (-18 coefficient in OLS)
- **Interpretation**: Routes frequented by heavy vehicles may have lower overall traffic
- **Recommendation**: Consider alternate paths that heavy vehicles typically use

### 3. Time of Day Matters
- **Finding**: Later times correlate with higher congestion
- **Recommendation**: Schedule outings earlier in the day to avoid peak congestion

### 4. Weather Has Limited Short-Term Impact
- **Finding**: Precipitation, visibility, and temperature have minimal effect in 15-minute windows
- **Interpretation**: Traffic doesn't naturally slow down quickly in poor conditions
- **Caution**: Inexperienced drivers shouldn't rely on weather-related slowing

---

## ⚠️ Limitations & Future Work

### Current Limitations
1. **Temporal Scope**: Single year (2019) prevents multi-year seasonal analysis
2. **Demographic Changes**: Population growth effects not captured
3. **Holiday Impact**: Limited ability to model holiday period variations
4. **Anomalies**: Natural disasters, road closures, and pandemics not accounted for
5. **Geographic Specificity**: Austin-only findings may not generalize

### Future Improvements
1. **Multi-year Data**: Capture seasonal patterns and demographic shifts
2. **Real-time Features**: Integrate live traffic, events, and construction data
3. **Advanced Models**: LSTM/GRU for temporal dependencies
4. **Spatial Analysis**: Network effects between intersections
5. **Causal Inference**: Establish causal rather than correlational relationships
