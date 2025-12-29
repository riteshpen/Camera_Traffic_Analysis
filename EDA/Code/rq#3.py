import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

pd.set_option('display.max_columns', None)
df = pd.read_csv(r'C:\Users\travi\Downloads\Camera_Traffic_Counts2_20250918.csv')
print(df.head())

df['Day Type'] = df['Day of Week'].apply(lambda x: 'Weekend' if x in [0, 6] else 'Weekday')

# 🔹 T-Test: Compare Volume between Weekend and Weekday
weekday_volumes = df[df['Day Type'] == 'Weekday']['Volume']
weekend_volumes = df[df['Day Type'] == 'Weekend']['Volume']

t_stat, p_val = ttest_ind(weekday_volumes, weekend_volumes, equal_var=False)

print("\n--- T-Test Results ---")
print(f"T-statistic: {t_stat:.3f}")
print(f"P-value: {p_val:.4f}")
if p_val < 0.05:
    print("✅ Statistically significant difference in volume between weekends and weekdays.")
else:
    print("❌ No statistically significant difference in volume between weekends and weekdays.")

sns.boxplot(data=df, x='Day Type', y='Volume', showfliers=False)

plt.title('Volume Distribution by Heavy Vehicle Presence')
plt.xlabel('Type of Day')
plt.ylabel('Volume')

plt.show()

def whiskers(x):
    Q1 = x.quantile(0.25)
    Q3 = x.quantile(0.75)
    IQR = Q3 - Q1
    lower_whisker = x[x >= (Q1 - 1.5 * IQR)].min()
    upper_whisker = x[x <= (Q3 + 1.5 * IQR)].max()
    return pd.Series({
        'Lower Whisker': lower_whisker,
        'Q1': Q1,
        'Median': x.median(),
        'Q3': Q3,
        'Upper Whisker': upper_whisker,
        'Mean': x.mean()
    })

summary_stats = df.groupby('Day Type')['Volume'].apply(whiskers).unstack().T

print(summary_stats)
