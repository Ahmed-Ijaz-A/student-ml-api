from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

APP_VERSION = "1.1.0"
MODEL_VERSION = "model-1"

class PredictRequest(BaseModel):
    value: float

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": "student-ml-api",
        "application_version": APP_VERSION,
        "model_version": MODEL_VERSION
    }

@app.post("/predict")
def predict(request: PredictRequest):
    prediction = request.value * 2
    return {"input": request.value, "prediction": prediction}