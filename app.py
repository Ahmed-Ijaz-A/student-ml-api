from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

APP_VERSION = "1.0.0"

class PredictRequest(BaseModel):
    value: float

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": "student-ml-api",
        "version": APP_VERSION
    }

@app.post("/predict")
def predict(request: PredictRequest):
    prediction = request.value * 2
    return {"input": request.value, "prediction": prediction}