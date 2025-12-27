# 🚦 Austin Traffic: Exploratory Data Analysis

## 📋 Project Overview
This repository contains the exploratory data analysis for the Austin Camera Traffic Counts project, analyzing 14.7 million traffic observations from 2019 to understand patterns in vehicle speeds and volumes at intersections.

## 📊 Dataset
- **Source**: GRIDSMART optical detectors at Austin intersections
- **Time Period**: January 1, 2019 - December 31, 2019
- **Original Size**: 82.1 million rows (filtered to 14.7 million)
- **Filtering Rationale**: Avoids COVID-19 pandemic effects and computational constraints

### Data Access
The full dataset is available via [Google Drive](https://drive.google.com/drive/u/3/folders/1MASJueZORSwywnJHiAhAmR_5JKQCizZw).

A 100-row sample (`sample_data.csv`) is included in the `data/` directory for testing.

## 🔍 Key Hypotheses Tested

### Hypothesis 1: "People tend to drive slower toward the end of the week"
- **Method**: Daily average speed comparison
- **Finding**: Speed decreases from Monday (17.20 mph) to Sunday (16.89 mph)
- **Visualization**: `figures/speed_by_day_of_week.png`

### Hypothesis 2: "People tend to drive less on weekends"
- **Method**: Two-sample t-test comparing weekday vs. weekend volumes
- **Finding**: Significant difference (p < 0.05) with lower mean volume on weekends (22.17 vs. 26.87)
- **Visualization**: `figures/volume_distribution_weekday_vs_weekend.png`

### Hypothesis 3: "Vehicles drive more slowly during rush hours"
- **Method**: One-tailed t-test comparing rush hour (7-9 AM, 4-7 PM) vs. non-rush hour speeds
- **Finding**: Overwhelming evidence (p ≈ 2.2e-192) supporting slower speeds during rush hours
- **Visualization**: `figures/speed_by_hour.png`

### Hypothesis 4: "Cars move faster at turns when heavy vehicles are present"
- **Method**: Welch's t-test on turning intersections only
- **Finding**: Statistical evidence (p ≈ 0.0) supporting faster speeds when heavy vehicles are present
- **Visualization**: `figures/turn_speed_heavy_vehicle.png`

## 🛠️ Technical Implementation

### Statistical Analysis
- **T-tests**: For comparing group means
- **Box plots**: For distribution visualization
- **Correlation matrix**: For identifying relationships between numeric features

### Key Features Analyzed
- `Speed Average (Miles Per Hour)`: Primary speed metric
- `Volume`: Vehicle count per 15-minute interval
- `Heavy Vehicle`: Boolean for vehicles ≥17 feet
- `Day of Week`, `Hour`: Temporal features
- `Direction`, `Movement`: Spatial and turning features

## 📈 Results Summary
1. **Temporal Patterns**: Speed gradually decreases through the week; significantly slower during rush hours
2. **Volume Differences**: Weekend driving is less frequent but more variable
3. **Heavy Vehicle Effect**: Presence correlates with higher speeds at turns
4. **Feature Relationships**: Volume and speed show moderate positive correlation (0.32)

## 📁 Repository Structure
