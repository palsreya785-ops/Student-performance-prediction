from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("models/model.pkl")

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])

    pred = model.predict(df)[0]
    prob = model.predict_proba(df)[0][1]

    if pred == 0:
        advice = "⚠️ Increase study hours and attendance"
    else:
        advice = "✅ Keep up the good work"

    return {
        "prediction": "PASS" if pred == 1 else "FAIL",
        "risk_probability": float(prob),
        "advice": advice
    }