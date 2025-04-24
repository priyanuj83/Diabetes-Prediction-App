import streamlit as st
import joblib 
import numpy as np

# Loading the trained model
model = joblib.load("diabetes_rf_model.pkl")

st.set_page_config(page_title = "Diabetes Prediction", layout = "centered")

# App title
st.title("🩺 Diabetes Prediction App")
st.markdown("This app uses a trained **Random Forest model** to predict whether a person has diabetes based on diagnostic measurements.")

# Input fields
st.subheader("Enter the following medical details:")

pregnancies = st.number_input("Pregnancies", min_value=0, step=1)
glucose = st.number_input("Glucose Level", min_value=0)
blood_pressure = st.number_input("Blood Pressure", min_value=0)
skin_thickness = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0, format="%.2f")
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f")
age = st.number_input("Age", min_value=1)

# Predict button
if st.button("Predict"):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                            insulin, bmi, dpf, age]])
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"🟥 The person is likely **Diabetic** with {probability*100:.2f}% confidence.")
    else:
        st.success(f"🟩 The person is **Not Diabetic** with {(1-probability)*100:.2f}% confidence.")