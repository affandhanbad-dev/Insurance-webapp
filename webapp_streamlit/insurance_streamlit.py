# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 21:21:28 2025

@author: Affan
"""

import streamlit as st
import json
import requests

st.title("Insurance Cost Prediction App")

url = 'https://steelless-figureless-star.ngrok-free.dev/Insurance_prediction'

age = st.number_input("Age", min_value=1, max_value=120, step=1)
sex = st.selectbox("Sex", ["Female", "Male"])
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, step=0.1)
children = st.number_input("Number of Children", min_value=0, max_value=10, step=1)
smoker = st.selectbox("Smoker", ["No", "Yes"])
region = st.selectbox("Region", ["Southwest(2)", "Southeast(1)", "Northwest(3)", "Northeast(0)"])

sex_value = 1 if sex == "Male" else 0
smoker_value = 1 if smoker == "Yes" else 0
region_mapping = {
    "Northeast(0)": 0,
    "Southeast(1)": 1,
    "Southwest(2)": 2,
    "Northwest(3)": 3
}
region_value = region_mapping[region]

if st.button("Predict Insurance Cost"):
    input_data = {
        'age': age,
        'sex': sex_value,
        'bmi': bmi,
        'children': children,
        'smoker': smoker_value,
        'region': region_value
    }

    response = requests.post(url, data=json.dumps(input_data))

    if response.status_code == 200:
        st.success(f"Predicted Insurance Cost: ${response.text}")
    else:
        st.error("Error occurred while fetching prediction. Check backend server!")
