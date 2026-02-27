import streamlit as st
import numpy as np
import pandas as pd
import joblib

# ----------------------------
# Load saved objects
# ----------------------------

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
feature_columns = joblib.load("feature_columns.pkl")

st.title("🎓 Campus Placement Prediction System")

st.write("Enter student details:")

# ----------------------------
# Numeric Inputs
# ----------------------------

age = st.number_input("Age", 17, 40, 22)
ssc_percentage = st.number_input("SSC Percentage", 0.0, 100.0)
hsc_percentage = st.number_input("HSC Percentage", 0.0, 100.0)
degree_percentage = st.number_input("Degree Percentage", 0.0, 100.0)
mba_percentage = st.number_input("MBA Percentage", 0.0, 100.0)

internships_count = st.number_input("Internships Count", 0, 10)
projects_count = st.number_input("Projects Count", 0, 20)
certifications_count = st.number_input("Certifications Count", 0, 20)

technical_skills_score = st.slider("Technical Skills Score", 0, 100)
soft_skills_score = st.slider("Soft Skills Score", 0, 100)
aptitude_score = st.slider("Aptitude Score", 0, 100)
communication_score = st.slider("Communication Score", 0, 100)

work_experience_months = st.number_input("Work Experience (Months)", 0, 60)
leadership_roles = st.number_input("Leadership Roles", 0, 10)
extracurricular_activities = st.number_input("Extracurricular Activities", 0, 10)
backlogs = st.number_input("Backlogs", 0, 20)

# ----------------------------
# Prediction
# ----------------------------

if st.button("Predict Placement"):

    # Create dictionary of inputs
    input_dict = {
        "age": age,
        "ssc_percentage": ssc_percentage,
        "hsc_percentage": hsc_percentage,
        "degree_percentage": degree_percentage,
        "mba_percentage": mba_percentage,
        "internships_count": internships_count,
        "projects_count": projects_count,
        "certifications_count": certifications_count,
        "technical_skills_score": technical_skills_score,
        "soft_skills_score": soft_skills_score,
        "aptitude_score": aptitude_score,
        "communication_score": communication_score,
        "work_experience_months": work_experience_months,
        "leadership_roles": leadership_roles,
        "extracurricular_activities": extracurricular_activities,
        "backlogs": backlogs
    }

    # Convert to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Add missing columns from training
    for col in feature_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Ensure correct column order
    input_df = input_df[feature_columns]

    # Scale input
    input_scaled = scaler.transform(input_df)

    # Predict
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.success("🎉 Student is Likely to be Placed")
    else:
        st.error("❌ Student is Not Likely to be Placed")
