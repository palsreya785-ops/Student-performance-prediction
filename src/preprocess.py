import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def split_data(df):
    X = df.drop(["pass", "final_score"], axis=1)
    y = df["pass"]
    return X, y