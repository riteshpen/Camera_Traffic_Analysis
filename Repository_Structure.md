## 📁 Repository Structure

├── .dvc/                      # DVC configuration files
├── .git/                      # Git repository data
├── .ipynb_checkpoints/        # Jupyter notebook checkpoints
├── data/
│   ├── Camera_Traffic_Counts2_20250918.csv.dvc    # DVC pointer to main dataset
│   ├── Austin 2019-01-01 to 2023-07-22.csv        # Weather data
│   ├── emissions.csv          # Code carbon emissions tracking
│   ├── data.csv              # Regional weather summary
│   └── sample/               # Sample data for testing
│       └── Camera_Traffic_Counts_sample.csv
├── notebooks/
│   ├── weather_data.ipynb    # Weather analysis
│   ├── research_question_3.ipynb  # Advanced analysis
│   └── Final_Project.ipynb   # Main project notebook
├── scripts/
│   ├── final_project.py      # Main analysis script
│   ├── rq#3.py              # Research question 3 implementation
│   └── COde.R               # R code analysis
├── models/
│   └── best_average_speed_model.pkl  # Trained model
├── figures/
│   ├── feature_importance.png
│   ├── prediction_vs_actual.png
│   ├── rf_feature_importance.png
│   ├── ridge_coefficients.png
│   └── shap_summary.png
├── reports/
│   ├── Group 11 Exploratory Data Analysis.pdf
│   ├── Group 11 Modeling Presentation (3).pdf
│   └── Team 11 - Final Report.pdf
├── .dvcignore               # DVC ignore patterns
├── .gitattributes          # Git LFS configuration
├── .gitignore             # Git ignore patterns
├── requirements.txt       # Python dependencies
├── LICENSE               # Project license
└── README.md             # Main project documentation
