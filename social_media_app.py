import streamlit as st
import numpy as np
import joblib

model = joblib.load("social_media_model.pkl")

st.title("📱 Social Media Impact Analyzer")

st.write("Enter your details to predict your mental health score.")

age = st.number_input("Age", 10, 100, 20)

usage = st.number_input(
    "Average Daily Social Media Usage (Hours)",
    0.0, 24.0, 4.0
)

sleep = st.number_input(
    "Sleep Hours Per Night",
    0.0, 24.0, 7.0
)

if st.button("Predict"):

    data = np.array([[usage, sleep, age]])

    result = model.predict(data)[0]

    st.success(f"Predicted Mental Health Score: {result:.2f}")