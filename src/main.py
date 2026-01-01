from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="CreditPathAI Backend")

class LoanRequest(BaseModel):
    sk_id_curr: int

@app.get("/")
def health_check():
    return {"status": "CreditPathAI Backend Running"}

@app.post("/predict")
def predict(data: LoanRequest):
    return {
        "sk_id_curr": data.sk_id_curr,
        "risk_category": "High",
        "recovery_probability": 0.42,
        "recommended_action": "Immediate follow-up by recovery agent"
    }
