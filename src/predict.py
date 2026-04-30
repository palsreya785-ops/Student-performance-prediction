import joblib
import pandas as pd

model = joblib.load("models/model.pkl")

sample = pd.DataFrame([{
    "study_hours": 6,
    "attendance": 75,
    "quiz_score": 65,
    "assignment_score": 70,
    "midterm_score": 60
}])

pred = model.predict(sample)[0]
prob = model.predict_proba(sample)[0][1]

print("Prediction:", "PASS" if pred == 1 else "FAIL")
print("Risk Probability:", round(prob, 2))