import pandas as pd
import numpy as np
import os

os.makedirs("data", exist_ok=True)

np.random.seed(42)
n = 500

data = pd.DataFrame({
    "study_hours": np.random.randint(1, 10, n),
    "attendance": np.random.randint(50, 100, n),
    "quiz_score": np.random.randint(40, 100, n),
    "assignment_score": np.random.randint(40, 100, n),
    "midterm_score": np.random.randint(40, 100, n)
})

data["final_score"] = (
    data["study_hours"] * 5 +
    data["attendance"] * 0.3 +
    data["quiz_score"] * 0.2 +
    data["assignment_score"] * 0.2 +
    data["midterm_score"] * 0.3
)

data["pass"] = (data["final_score"] > 60).astype(int)

data.to_csv("data/students.csv", index=False)

print("✅ Dataset created!")