import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("diabetes.joblib")

# Create simple label encoders matching the model's training logic
gender_map = {"Female": 0, "Male": 1, "Other": 3}
smoking_map = {"No Info": 0, "current": 1, "ever": 2, "former": 3, "never": 4, "not current": 5}
BMI_map = {"Normal": 0, "Obese": 1, "Overweight": 2, "Underweight": 3}
age_group_map = {"26-40 Adult": 0, "41-50 Old Adult": 1, "<=25 Young Adult": 2, ">=51 Elders": 3, "Other": 4}

# Streamlit UI
st.title("Diabetes Prediction App")

# Input fields
age = st.number_input("Age", min_value=0, max_value=100)
bmi= st.number_input("BMI", min_value=0.0)
HbA1c_level = st.number_input("HbA1c_level", min_value=2.0, max_value=11.0)
blood_glucose_level = st.number_input("Blood Glucose Level", min_value=75, max_value=330)

# Categorical inputs
gender = st.selectbox("Gender", list(gender_map.keys()))
smoking = st.selectbox("Smoking", list(smoking_map.keys()))
hypertension = st.selectbox("Hypertension", [0, 1])
heart_disease = st.selectbox("Heart Disease", [0, 1])

# Encode values
input_data = pd.DataFrame([{
    "Age": age,
    "BMI": bmi,
    "HbA1c level": HbA1c_level,
    "Blood glucose level": blood_glucose_level,
    "Gender": gender,
    "Smoking": smoking,
    "Hypertension": hypertension,
    "Heart disease": heart_disease,
}])

# Make prediction
if st.button("Predict Diabetes"):
    prediction = model.predict(input_data)
    st.success(f"Prediction: {'Diabetic (1)' if prediction[0] == 1 else 'Non diabetic (0)'}")