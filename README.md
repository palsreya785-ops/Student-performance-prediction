# 🎓 Student Performance Prediction System

## 📌 Overview
This project predicts whether a student will pass or fail based on academic and behavioral data using Machine Learning.

It simulates real-world education analytics systems used by universities and EdTech platforms.

---

## 🚀 Features
- 📊 Predict student performance (Pass/Fail)
- 🤖 Machine Learning model (Random Forest)
- 🌐 FastAPI backend for real-time predictions
- 📊 Streamlit dashboard for interactive UI
- 📈 Data visualizations and insights

---

## 🛠 Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- FastAPI
- Streamlit
- Matplotlib, Seaborn

---

## 📁 Project Structure
Student-Performance-Prediction/ │ ├── data/ # Dataset ├── src/ # ML scripts ├── models/ # Saved model ├── api/ # FastAPI backend ├── dashboard/ # Streamlit UI ├── outputs/ # Graphs ├── main.py # Dataset generator ├── requirements.txt └── README.md

---

## ▶️ How to Run

### 1️⃣ Install dependencies
pip install -r requirements.txt

### 2️⃣ Generate dataset
python main.py

### 3️⃣ Train model
python src/train.py

### 4️⃣ Run API
uvicorn api.app:app --reload

### 5️⃣ Run Dashboard
streamlit run dashboard/app.py

---

## 📊 Sample Output
- Prediction: PASS / FAIL
- Risk Probability Score
- Performance Graphs

---

## 🎯 Use Cases
- Identify at-risk students
- Improve academic performance
- Personalized learning recommendations
- Dropout prevention

---

## 📈 Future Improvements
- XGBoost model for better accuracy
- SHAP explainability
- Deployment using Docker
- Next.js frontend

---

## 💼 Author
Sreya Pal

---

## ⭐ If you like this project, give it a star!
