from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import sqlite3
import os

app = FastAPI(title="CreditPathAI Backend")

MODEL_PATH = "model/xgboost_model.pkl"
DB_PATH = "src/creditpath.db"

model = joblib.load(MODEL_PATH)

class LoanRequest(BaseModel):
    sk_id_curr: int

@app.get("/")
def health_check():
    return {"status": "CreditPathAI Backend Running"}

def fetch_features(sk_id):
    conn = sqlite3.connect(DB_PATH)
    query = f"SELECT * FROM borrower_features WHERE SK_ID_CURR = {sk_id}"
    df = pd.read_sql(query, conn)
    conn.close()
    return df.drop(columns=["SK_ID_CURR"])

@app.post("/predict")
def predict(data: LoanRequest):
    X = fetch_features(data.sk_id_curr)

    prob = model.predict_proba(X)[0][1]

    if prob > 0.7:
        risk = "High"
        action = "Immediate legal follow-up"
    elif prob > 0.4:
        risk = "Medium"
        action = "Agent follow-up"
    else:
        risk = "Low"
        action = "Automated reminder"

    return {
        "sk_id_curr": data.sk_id_curr,
        "risk_category": risk,
        "recovery_probability": round(prob, 2),
        "recommended_action": action
    }
