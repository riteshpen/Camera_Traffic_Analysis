# Camera_Traffic_Analysis

**Traffic Speed Analysis at Austin Intersections**  
*By Team 11:* Ritesh Penumatsa, John Trelford, Lucas Chiang, Travis Welsh, and Brian Pham

---

## 📌 Project Summary

This project investigates the **factors associated with average vehicle speeds at intersections in Austin, Texas**. Using traffic count data and weather/temporal variables, we explore which conditions are linked with higher or lower traffic speeds and offer insights that may help **inexperienced drivers make safer decisions**.


<img width="193" height="122" alt="Image" src="https://github.com/user-attachments/assets/0309eef7-8871-40ae-83fb-4ba305050e99" />
<img width="686" height="382" alt="Image" src="https://github.com/user-attachments/assets/4628c0be-e2eb-4b2b-bf19-af28acd9edb9" />

The work consists of:
- **Exploratory Data Analysis**
- **Predictive Modeling** (Ridge Regression & Random Forest)
- **Final Report and Interpretation**

---

## 📥 Dataset Access

The dataset used is **too large for GitHub** and is hosted on Google Drive.

**Download here:**  
🔗 *Camera Traffic Counts & related files*  
👉 https://drive.google.com/drive/u/3/folders/1osDlrN4x127uuhuqeRXGJaXXZ2Ig7znp

> Make sure the folder is set to “Anyone with the link can view” so that collaborators and reviewers can access it without signing in. :contentReference[oaicite:0]{index=0}

---

## 🧠 High-Level Findings

- **Recent traffic history** (lagged speeds & volumes) strongly predicts current average speed.
- **Temporal factors** (time of day, day of week) influence speeds.
- **Weather effects** (rain, wind, visibility) have minimal influence in short 15-minute periods.
- Both Ridge Regression and Random Forest models confirm similar patterns, with the Random Forest showing more explanatory power.

---

## 🛠 Modeling Overview

**Models Used**
- **Ridge Regression:** Interpretable linear model with regularization.
- **Random Forest:** Captures non-linear patterns and feature importance.

**Evaluation**
- Metrics: R² and RMSE on validation/test sets.
- Ridge Regression achieved moderate explanatory power.
- Random Forest showed stronger performance, highlighting the significance of lagged traffic history.

---

## 🧩 Key Insight

Traffic speed at intersections is primarily driven by **immediate past conditions** rather than broader environmental or calendar features. Drivers should be aware that heavy congestion or high recent speeds are indicators of continued high speed or unstable driving conditions.

---

## 📁 Repository Contents

- **EDA Notebooks** – data exploration and visualization
- **Modeling Scripts** – training & evaluation
- **Results & Figures** – graphs and summary tables
- **Final Report** – detailed write-up

---

## 🧑‍🤝‍🧑 Team

Ritesh Penumatsa · John Trelford · Lucas Chiang · Travis Welsh · Brian Pham

---

## 📄 References

- Austin Camera Traffic Counts dataset (City of Austin Open Data)  
  https://data.austintexas.gov/Transportation-and-Mobility/Camera-Traffic-Counts/sh59-i6y9

---

