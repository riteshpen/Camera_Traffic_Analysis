# 🚦 Austin Traffic Analysis: Final Report

## 📋 Comprehensive Project Summary
This repository contains the final report, presentation, and complete analysis of factors influencing traffic speeds at Austin intersections. The project combines exploratory analysis, predictive modeling, and practical recommendations for driver safety.

## 🎯 Research Question
**"What factors are associated with higher average speeds at intersections?"**

### Primary Objectives
1. Identify interpretable factors linked to traffic speeds
2. Provide actionable insights for inexperienced drivers
3. Compare model performance and interpretability trade-offs

## 📊 Dataset & Methodology

### Data Source
- **Primary**: Austin Camera Traffic Counts (GRIDSMART detectors)
- **Time Period**: 2019 only (avoids COVID-19 effects)
- **Sample Size**: 14.7 million rows (from original 82.1 million)
- **Weather Data**: Visual Crossing weather API

### Analytical Approach
1. **Exploratory Analysis**: Hypothesis testing of temporal patterns
2. **Predictive Modeling**: Ridge Regression vs. Random Forest
3. **Interpretation**: Feature importance and practical implications

## 🔑 Key Findings

### Dominant Factors
1. **Recent Traffic History**: Lagged speeds (15-60 minutes prior) are the strongest predictors
2. **Temporal Patterns**: Time of day influences speed more than day of week
3. **Heavy Vehicles**: Presence associated with higher speeds at turns

### Minimal Influence Factors
1. **Weather Conditions**: Precipitation and visibility have a negligible short-term impact
2. **Calendar Effects**: Holidays show minimal influence on 15-minute speeds
3. **Temperature**: Limited effect within observed range

## 📈 Model Performance

### Comparative Results
| Model | Test R² | Test RMSE | Key Strength |
|-------|---------|-----------|--------------|
| Ridge Regression | 0.20 | 11.54 mph | Interpretability |
| Random Forest | 0.40 | 9.99 mph | Predictive accuracy |

### Energy Efficiency Comparison
| Model | Training Time | Energy Used | CO₂ Emissions |
|-------|---------------|-------------|---------------|
| Ridge Regression | 0.53s | 0.000007 kWh | 0.000003 kg |
| Random Forest | 57.17s | 0.000794 kWh | 0.000318 kg |

## 🧩 Model Interpretation

### Ridge Regression Insights
- **Statistically Significant**: Lagged volumes, time of day, heavy vehicle presence
- **Counterintuitive Finding**: Higher volumes predict higher speeds (potential confounding)
- **Practical Use**: Clear coefficient interpretation for driver guidance

### Random Forest Insights
- **Feature Hierarchy**: Lag_4_speed > Lag_1_speed > Lag_1_volume
- **SHAP Analysis**: Confirms dominance of recent traffic patterns
- **Practical Use**: Higher accuracy for prediction applications

## 🛡️ Practical Applications

### For Inexperienced Drivers
1. **Recent Conditions Matter**: Current speed depends heavily on very recent traffic
2. **Weather Less Important**: Don't expect natural slowing in poor conditions
3. **Heavy Vehicle Caution**: Roads with heavy vehicles may have higher speeds
4. **Temporal Awareness**: Rush hours show consistently lower speeds

### For Traffic Management
1. **Short-Term Focus**: 15-minute predictions most reliable
2. **Efficiency Trade-offs**: Ridge regression sufficient for many applications
3. **Data Gaps**: Unmeasured factors (road quality, curvature) are likely important

## 📚 Report Contents

### Included Documents
1. **Final Report** (`Team_11_Final_Report.pdf`): Comprehensive analysis
2. **Modeling Presentation** (`Group_11_Modeling_Presentation.pdf`): Technical details
3. **Project Summary** (`Group_11_Final_Project.pdf`): High-level overview

### Key Sections
- Literature Review: Historical context of speed factor analysis
- Methodology: Data processing and modeling decisions
- Results: Statistical findings and visualizations
- Discussion: Interpretation and limitations
- Applications: Practical recommendations

## ⚠️ Limitations & Future Work

### Current Limitations
1. **Temporal Scope**: Single year prevents seasonal pattern analysis
2. **Unobserved Confounders**: Road quality, curvature, urban development
3. **Geographic Specificity**: Austin-only data may not generalize
4. **Model Explanatory Power**: 40-60% of variance unexplained

### Future Directions
1. **Multi-Year Analysis**: Capture seasonal and demographic changes
2. **Additional Features**: Road characteristics, nearby developments
3. **Real-Time Application**: Integration with traffic management systems
4. **Comparative Studies**: Other cities with similar intersection data
