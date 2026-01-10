# Austin Traffic Analysis Project Structure

This repository contains the complete analysis of traffic patterns in Austin, Texas. The project is organized into three main phases: **Exploratory Data Analysis (EDA)**, **Predictive Modeling**, and **Final Project/Report**.

## 📁 Repository Structure
```
Austin_Traffic_Analysis/
├── Datasets/ # Data sources and documentation
│ └── README.md # Dataset descriptions and access instructions
│
├── EDA/ # Exploratory Data Analysis
│ ├── Code/
│ │ └── research_question_3.ipynb # Hypothesis testing and analysis
│ ├── Presentation/
│ │ ├── Group 11 Exploratory Data Analysis.pdf
│ │ └── Group 11 Exploratory Data Analysis.pptx
│ └── README.md # EDA methodology and findings
│
├── Modeling/ # Predictive modeling phase
│ ├── Code/
│ │ ├── linear_regression.ipynb # Linear regression implementation
│ │ ├── random_forest_q1.ipynb # Random Forest for research question 1
│ │ └── weather_data.ipynb # Weather impact analysis
│ ├── Presentation/
│ │ ├── Group 11 Modeling Presentation.pdf
│ │ └── Group 11 Modeling Presentation.pptx
│ └── README.md # Modeling approach and results
│
├── Final Project-Report/ # Final deliverables
│
├── Final Project/ # Integrated project application
│ ├── Code/
│ │ ├── Final_Project.ipynb # Main project notebook
│ │ └── Visuals/ # Generated visualizations
│ │ │ ├── newplot (5).png
│ │ │ ├── newplot (10).png
│ │ │ └── newplot (11).png
│ ├── Presentation/
│ │ ├── Group 11 Final Project.pdf
│ │ └── Group 11 Final Project.pptx
│ └── README.md # Project overview and instructions
│
├── Final Report/ # Comprehensive report
│ ├── Code/
│ │ └── final_project.py # Production-ready analysis script
│ │ └── Visuals/ # All model outputs and figures
│ │ | └── best_average_speed_model.pkl
│ │ | └── feature_importance.png
│ │ | └── prediction_vs_actual.png
│ │ | └── rf_feature_importance.png
│ │ | └── ridge_coefficients.png
│ │ | └── shap_summary.png
│ ├── README.md # Report summary and findings
│ ├── Report/
│ │ └── Team 11 - Final Report.pdf # Production-ready analysis script
│ │ └── team 11 - final report_.docx
```

## 📊 Project Overview

### Phase 1: Exploratory Data Analysis (EDA)
**Location:** `EDA/`
- **Objective**: Understand traffic patterns, test hypotheses, and identify key variables
- **Key Outputs**: Statistical tests, visualizations, and initial insights
- **Main Files**: `research_question_3.ipynb` explores specific hypotheses about traffic behavior

### Phase 2: Predictive Modeling
**Location:** `Modeling/`
- **Objective**: Build and evaluate machine learning models for traffic prediction
- **Models Implemented**:
  - Linear Regression (`linear_regression.ipynb`)
  - Random Forest (`random_forest_q1.ipynb`)
  - Weather impact analysis (`weather_data.ipynb`)
- **Key Outputs**: Model performance metrics, feature importance, predictions

### Phase 3: Final Project & Report
**Location:** `Final Project-Report/`

#### **Final Project** (`Final Project-Report/Final Project/`)
- **Objective**: Integrated application combining EDA and modeling insights
- **Components**:
  - `Final_Project.ipynb`: Complete analysis pipeline
  - Visualizations: Key findings in PNG format
  - Presentation: Final project summary in PDF/PPTX

#### **Final Report** (`Final Project-Report/Final Report/`)
- **Objective**: Comprehensive documentation of the entire project
- **Components**:
  - `Team 11 - Final Report.pdf/docx`: Complete written report
  - `final_project.py`: Production code version
  - Visuals folder: All model outputs and figures for publication

## 🚀 Getting Started

### 1. Access the Data
Start with the `Datasets/README.md` for information on:
- Dataset sources and descriptions
- Download instructions
- Data preprocessing steps

### 2. Explore the Analysis
Follow the logical progression:
1. **EDA Phase**: Review hypothesis testing in `EDA/Code/research_question_3.ipynb`
2. **Modeling Phase**: Examine model implementations in `Modeling/Code/`
3. **Final Analysis**: See the integrated project in `Final Project-Report/Final Project/Code/`

### 3. Review Results
- **Presentations**: Each phase has PDF/PPTX summaries
- **Visualizations**: All figures are organized in respective `Visuals/` folders
- **Reports**: Comprehensive documentation in the Final Report section

## 🔍 Key Files Explained

### Notebooks (`*.ipynb`)
- `research_question_3.ipynb`: Tests specific traffic hypotheses
- `linear_regression.ipynb`: Implements and evaluates linear regression models
- `random_forest_q1.ipynb`: Random Forest implementation for research question 1
- `weather_data.ipynb`: Analyzes weather impact on traffic
- `Final_Project.ipynb`: Complete project integration and analysis

### Python Scripts (`*.py`)
- `final_project.py`: Production version of the main analysis

### Model Outputs (`Visuals/`)
- `best_average_speed_model.pkl`: Serialized trained model
- `feature_importance.png`: Feature importance visualization
- `prediction_vs_actual.png`: Model prediction accuracy
- `rf_feature_importance.png`: Random Forest feature importance
- `ridge_coefficients.png`: Ridge regression coefficients
- `shap_summary.png`: SHAP values for model interpretability

## 📈 Analysis Flow

1. **Data Understanding** → `Datasets/`
2. **Hypothesis Testing** → `EDA/`
3. **Model Building** → `Modeling/`
4. **Integration & Reporting** → `Final Project-Report/`

## 👥 Team 11
**Members**: John Trelford, Lucas Chiang, Travis Welsh, Brian Pham, Ritesh Penumatsa

## 📄 License
All materials in this repository are available for academic and research purposes.


*Last Updated: December 2025*  
*Project: Austin Traffic Patterns Analysis*
