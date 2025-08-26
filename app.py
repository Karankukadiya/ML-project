import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

# Streamlit UI
st.title("🏠 House Price Prediction")
st.write("Enter details below to predict house price:")

# Input fields
size = st.number_input("Size in sqft:", min_value=500, max_value=10000, step=100)
bedrooms = st.number_input("Number of bedrooms:", min_value=1, max_value=10, step=1)
location = st.slider("Location index (out of 10):", 1, 10, 5)
age = st.number_input("Age of the house (in years):", min_value=0, max_value=100, step=1)

# Prediction
if st.button("Predict Price"):
    input_data = np.array([[size, bedrooms, location, age]])
    predicted_price = model.predict(input_data)[0]
    st.success(f"💰 Predicted House Price: ₹{predicted_price:,.2f}")
    