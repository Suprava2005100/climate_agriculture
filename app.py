import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------
# Load the saved models
# ------------------------------
lr_model = joblib.load("lr_model_2features.pkl")          # Linear Regression trained on 2 features
rf_model = joblib.load("random_forest_model.pkl")         # Random Forest trained on 10 features

st.title("🌾 Climate & Agriculture Predictor")
st.write("Predict crop yield based on climate features.")

# ------------------------------
# User inputs
# ------------------------------
rainfall = st.number_input("Enter total precipitation (mm)", min_value=0.0, max_value=10000.0, value=500.0)
temperature = st.number_input("Enter average temperature (°C)", min_value=-50.0, max_value=60.0, value=25.0)

st.subheader("Optional: Additional features for more accurate Random Forest prediction")
co2_emissions = st.number_input("CO2 emissions (mt)", min_value=0.0, max_value=1000.0, value=20.0)
extreme_weather_events = st.number_input("Extreme weather events", min_value=0, max_value=50, value=5)
irrigation_access = st.number_input("Irrigation access (%)", min_value=0.0, max_value=100.0, value=50.0)
pesticide_use = st.number_input("Pesticide use (kg/ha)", min_value=0.0, max_value=500.0, value=10.0)
fertilizer_use = st.number_input("Fertilizer use (kg/ha)", min_value=0.0, max_value=500.0, value=15.0)
soil_health_index = st.number_input("Soil health index", min_value=0.0, max_value=100.0, value=70.0)
adaptation_strategies_score = st.number_input("Adaptation strategies score", min_value=0.0, max_value=10.0, value=5.0)
economic_impact = st.number_input("Economic impact (million USD)", min_value=0.0, max_value=10000.0, value=500.0)

# ------------------------------
# Choose model
# ------------------------------
model_choice = st.selectbox("Choose Machine Learning Model", ["Linear Regression", "Random Forest"])

# ------------------------------
# Make prediction
# ------------------------------
if st.button("Predict"):
    if model_choice == "Linear Regression":
        input_data = [[rainfall, temperature]]  # only 2 features
        prediction = lr_model.predict(input_data)
    else:
        # 10 features for Random Forest
        input_data = [[
            rainfall,
            temperature,
            co2_emissions,
            extreme_weather_events,
            irrigation_access,
            pesticide_use,
            fertilizer_use,
            soil_health_index,
            adaptation_strategies_score,
            economic_impact
        ]]
        prediction = rf_model.predict(input_data)
    
    st.success(f"Predicted crop yield: {prediction[0]:.2f} mt/ha")

# ------------------------------
# Optional: Show sample predictions graph (Linear Regression only)
# ------------------------------
st.subheader("Sample Predictions Visualization (Linear Regression)")
df = pd.read_csv(r"C:\Users\Suprava\Desktop\Climate_agriculture\processed\climate_change_impact_on_agriculture_2024_cleaned.csv")
df_small = df[['total_precipitation_mm', 'average_temperature_c', 'crop_yield_mt_per_ha']].head(50)

X_plot = df_small[['total_precipitation_mm','average_temperature_c']]
y_actual = df_small['crop_yield_mt_per_ha']

fig, ax = plt.subplots()
ax.scatter(df_small['total_precipitation_mm'], y_actual, color='blue', label='Actual')
ax.scatter(df_small['total_precipitation_mm'], lr_model.predict(X_plot), color='red', label='Predicted (LR)')
ax.set_xlabel('Total Precipitation (mm)')
ax.set_ylabel('Crop Yield (mt/ha)')
ax.legend()
st.pyplot(fig)
