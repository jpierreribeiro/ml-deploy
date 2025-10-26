from fastapi import FastAPI
from pydantic import BaseModel
from app.modelo.modelo import predict_pipeline
from app.modelo.modelo import _version_ as model_version

app = FastAPI()

class TextIn(BaseModel):
    text: str

class PredictionOut(BaseModel):
    idioma: str

@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}

app.post("/predict", response_model=PredictionOut)
def predic(payload: TextIn):
    idioma = predict_pipeline(payload.text)
    return {"idioma": idioma}