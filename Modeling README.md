# 🚦 Austin Traffic: Predictive Modeling

## 📋 Project Overview
This repository contains predictive models for analyzing factors that influence traffic speeds and volumes at Austin intersections. We compare Ridge Regression and Random Forest approaches, with consideration of computational efficiency and environmental impact.

## 🎯 Modeling Problems

### Problem 1: Traffic Volume Prediction
**Objective**: Predict 15-minute traffic volume based on temporal features
- **Target**: `Volume` (vehicle count)
- **Key Features**: Day of week, time, holiday, precipitation, heavy vehicle presence
- **Models**: Linear Regression, Random Forest
- **Best Model**: Random Forest (R²=0.0344, RMSE=58.14)

### Problem 2: Average Speed Prediction
**Objective**: Predict vehicle speed based on weather and traffic conditions
- **Target**: `Speed Average (Miles Per Hour)`
- **Key Features**: Precipitation, temperature, lagged volumes/speeds
- **Models**: Random Forest, Gradient Boosting
- **Best Model**: Random Forest (R²=0.81, RMSE=0.194)

## 🏗️ Model Architecture

### Ridge Regression
- **Purpose**: Interpretable model for understanding feature relationships
- **Regularization**: L2 penalty with α=0.001
- **Key Features**:
  - Lagged volumes (15-60 minutes prior)
  - Time of day
  - Day of week (one-hot encoded)
  - Heavy vehicle presence

### Random Forest
- **Purpose**: High-accuracy prediction capturing non-linear relationships
- **Parameters**: n_estimators=100, max_depth=10
- **Feature Importance**: Lagged speeds are dominant predictors

## 📊 Model Performance

### Volume Prediction (Problem 1)
| Model | R² | RMSE | Training Time | Energy Used |
|-------|----|------|---------------|-------------|
| Linear Regression | 0.0013 | 59.12 | 4.61s | 0.000288 kWh |
| Random Forest | 0.0344 | 58.14 | 8m44s | 0.007644 kWh |

### Speed Prediction (Problem 2)
| Model | R² | RMSE | Energy Used | CO₂ Emissions |
|-------|----|------|-------------|---------------|
| Random Forest | 0.81 | 0.194 | 0.031 kWh | 0.013 kg CO₂ |
| Gradient Boosting | 0.813 | 0.436 | 0.142 kWh | 0.061 kg CO₂ |

## 🔍 Key Insights

### Feature Importance
1. **Lagged Features Dominate**: Recent traffic conditions (past 15-60 minutes) are strongest predictors
2. **Weather Minimal Impact**: Precipitation, temperature have negligible effect in 15-minute windows
3. **Temporal Patterns**: Time of day more important than day of week

### Energy Considerations
- **Ridge Regression**: 100× more energy efficient than Random Forest
- **Random Forest**: Better accuracy but higher computational cost
- **Practical Trade-off**: For frequent predictions, efficiency matters; for occasional analysis, accuracy prioritizes

## 🛠️ Technical Implementation

### Data Splitting Strategy
- **Training**: January-September 2019
- **Validation**: October-November 2019
- **Testing**: December 2019
- **Rationale**: Avoids temporal leakage; simulates real-world prediction

### Hyperparameter Tuning
- **Ridge Regression**: Manual search for α (0.001 optimal)
- **Random Forest**: Limited tuning of n_estimators and max_depth
- **Constraint**: Avoided cross-validation to prevent temporal leakage

### Evaluation Metrics
- **RMSE**: Primary metric (penalizes large errors)
- **R²**: Explanatory power assessment
- **Energy Consumption**: Environmental impact consideration
