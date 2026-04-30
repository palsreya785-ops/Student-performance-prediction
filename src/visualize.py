import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("outputs", exist_ok=True)

df = pd.read_csv("data/students.csv")

# Distribution plot
sns.histplot(df["final_score"], kde=True)
plt.title("Final Score Distribution")
plt.savefig("outputs/final_score_distribution.png")
plt.clf()

# Scatter plot
plt.scatter(df["attendance"], df["final_score"])
plt.xlabel("Attendance")
plt.ylabel("Final Score")
plt.title("Attendance vs Performance")
plt.savefig("outputs/attendance_vs_score.png")

print("✅ Visualizations saved in outputs/")