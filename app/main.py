from fastapi import FastAPI
from pydantic import BaseModel
from .modelo.modelo import predict_pipeline
from .modelo.modelo import _version_ as model_version

app = FastAPI()

class TextIn(BaseModel):
    text: str

class PredictionOut(BaseModel):
    language: str

@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}

@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    language = predict_pipeline(payload.text)
    return {"idioma": language}