## Dataset

The full datasets are approximately 3 GB and cannot be hosted directly on GitHub.

### Download Details

| File Name | Description | Size | Direct Download |
| :--- | :--- | :--- | :--- |
| `Austin 2019-01-01 to 2023-07-22.csv` | Granular, localized weather observations for Austin, TX. | **486 KB** | [📥 Download](https://drive.google.com/drive/u/3/folders/1MASJueZORSwywnJHiAhAmR_5JKQCizZw) |
| `data.csv` | Standardized daily weather summaries from official stations. | **766 KB** | [📥 Download](https://drive.google.com/file/d/YOUR_FILE_ID/view?usp=sharing) |
| `emissions.csv` | Tracks energy consumption & carbon emissions from model runs. | **3 KB** | [📥 Download](https://drive.google.com/file/d/YOUR_FILE_ID/view?usp=sharing) |
| `Camera_Traffic_Counts_sample.csv` | Core traffic analysis data (sample). | **156 KB** | [📥 Download](https://drive.google.com/file/d/YOUR_FILE_ID/view?usp=sharing) |
| `Camera_Traffic_Counts2_20250918.csv` | Full core traffic analysis dataset (main file). | **2.33 GB** | [📥 Download](https://drive.google.com/file/d/YOUR_FILE_ID/view?usp=sharing) |

## 📊 Dataset Descriptions

### 1. **Austin Weather Data** (`Austin 2019-01-01 to 2023-07-22.csv`)
This dataset provides granular, localized weather observations in Austin, Texas.

*   **Content**: Features include temperature (`temp`, `tempmax`, `tempmin`), precipitation (`precip`, `preciptype`), humidity, wind speed, solar radiation, and descriptive weather conditions.
*   **Usefulness**: Ideal for analyzing the direct impact of weather on traffic patterns (e.g., Does rain slow down traffic? Does temperature affect volume?). The hyperlocal data is more relevant to traffic conditions than regional averages.

### 2. **Regional Weather Summary** (`data.csv`)
This dataset contains standardized daily weather summaries from official weather stations.

*   **Content**: Key variables are daily temperature averages/extremes (`TAVG`, `TMAX`, `TMIN`) and precipitation/snowfall (`PRCP`, `SNOW`).
*   **Usefulness**: Acts as a reliable, consistent baseline for weather analysis. It can be used to fill gaps in the Austin-specific data or to validate trends observed in the more detailed dataset.

### 3. **Code Carbon Emissions** (`emissions.csv`)
This dataset tracks the energy consumption and carbon emissions generated while running your computational experiments and models.

*   **Content**: Logs `timestamp`, `energy_consumed`, calculated `emissions`, hardware details (`cpu_model`, `gpu_model`), cloud provider info, and geographical `region`.
*   **Usefulness**: **Crucial for sustainable data science**. It allows you to measure and report the environmental footprint of your project, promoting transparency and efficiency in model training and data processing.

### 4. **Austin Traffic Counts** (`Camera_Traffic_Counts_sample.csv`)
This is the **core dataset** for traffic analysis, containing detailed readings from traffic cameras.

*   **Content**: For each observation, it records `Volume` (vehicle count), `Speed Average`, the `Intersection Name`, `Movement` (e.g., left turn), `Heavy Vehicle` count, and precise `Read Date` and time.
*   **Usefulness**: Enables comprehensive traffic analysis. You can:
    *   Model traffic volume and identify congestion patterns.
    *   Analyze how speed correlates with time of day, day of week, or weather.
    *   Study the impact of heavy vehicles on traffic flow.
    *   The sample file allows for initial code testing and exploratory data analysis before working with the full dataset.

## 🔗 How the Datasets Work Together

The power of this project lies in **joining these datasets** to answer complex questions:

1.  **Traffic + Austin Weather**: Merge traffic data with local weather conditions to quantify how rain, high temperatures, or low visibility affect traffic speed and volume at specific intersections.
2.  **Traffic + Regional Weather**: Use the summary data to see if broader weather trends correlate with city-wide traffic patterns.
3.  **Process + Emissions**: Link your analysis scripts to the emissions log to identify which stages of your pipeline (data cleaning, model training, etc.) are the most computationally intensive and carbon-heavy.
