import streamlit as st
import joblib
import pandas as pd

# Load the model and the scaler
model = joblib.load('heart_model.pkl')
scaler = joblib.load('scaler.pkl')

# Inside your predict function:
# 1. Take user input
# 2. Put into a DataFrame
# 3. Apply the loaded scaler: input_scaled = scaler.transform(input_df)
# 4. Predict: model.predict(input_scaled)