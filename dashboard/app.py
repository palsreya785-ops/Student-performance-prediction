import streamlit as st
import requests

st.set_page_config(page_title="Student Predictor", layout="centered")

st.title("🎓 Student Performance Predictor")

study_hours = st.slider("Study Hours", 1, 10)
attendance = st.slider("Attendance (%)", 50, 100)
quiz = st.slider("Quiz Score", 40, 100)
assignment = st.slider("Assignment Score", 40, 100)
midterm = st.slider("Midterm Score", 40, 100)

if st.button("Predict"):

    data = {
        "study_hours": study_hours,
        "attendance": attendance,
        "quiz_score": quiz,
        "assignment_score": assignment,
        "midterm_score": midterm
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=data)
    result = response.json()

    st.subheader(f"📌 Prediction: {result['prediction']}")
    st.write(f"📊 Risk Probability: {result['risk_probability']:.2f}")
    st.info(result["advice"])

    if result["prediction"] == "FAIL":
        st.error("⚠️ At Risk Student")
    else:
        st.success("✅ Student is doing well")