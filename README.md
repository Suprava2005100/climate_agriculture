# 🌾 Climate & Agriculture Predictor

Predict crop yield based on climate and agriculture features using machine learning.

---

## Project Overview

This project predicts crop yield (`mt/ha`) based on climate parameters such as precipitation, temperature, and other agricultural factors. The goal is to provide a simple interface for farmers, researchers, or policymakers to understand crop yield trends under different climate scenarios.

The project uses two models:

- **Linear Regression** – for simple predictions using two features (rainfall and temperature).  
- **Random Forest** – for more accurate predictions using multiple features.

---

## Features Used

- `total_precipitation_mm` – Total rainfall (mm)  
- `average_temperature_c` – Average temperature (°C)  
- `co2_emissions_mt` – CO₂ emissions (megatonnes)  
- `extreme_weather_events` – Number of extreme weather events  
- `irrigation_access_%` – Irrigation access percentage  
- `pesticide_use_kg_per_ha` – Pesticide usage (kg/ha)  
- `fertilizer_use_kg_per_ha` – Fertilizer usage (kg/ha)  
- `soil_health_index` – Soil health score  
- `adaptation_strategies_score` – Score of adaptation strategies implemented  
- `economic_impact_million_usd` – Economic impact in million USD  

---

## Folder Structure

Climate_agriculture/
│
├── processed/ # Cleaned datasets
│ └── climate_change_impact_on_agriculture_2024_cleaned.csv
├── raw/ # Raw datasets
├── src/ # Source code for training
│ └── train_and_evaluate.ipynb
├── models/ # Saved ML models
│ ├── lr_model_2features.pkl
│ └── random_forest_model.pkl
├── app.py # Streamlit deployment script
├── venv/ # Python virtual environment
└── README.md # Project documentation


---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/Climate_agriculture.git
   cd Climate_agriculture
Create a virtual environment and install dependencies:

python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py


Enter your climate and agricultural features in the input fields and choose the machine learning model to get crop yield predictions.

Notes

Large .pkl model files are included. They may not preview on GitHub, but they are fully usable.

Use Linear Regression for simple 2-feature predictions.

Use Random Forest for accurate multi-feature predictions.


Author

Suprava – B.Tech ECE | Aspiring Full-Stack & Software Developer
