import logging
from fastapi import APIRouter, Response
from pydantic import BaseModel
from typing import List
from app.services.model import text_classification_model

router = APIRouter()

class Prediction(BaseModel):
    label: str
    score: float

class ClassifyResponse(BaseModel):
    predictions: List[Prediction]

class ClassifyPayload(BaseModel):
    text: str
    labels: List[str]

@router.get("/api/healthz", status_code=204)
async def default():
    return Response(status_code=204)

@router.post("/api/classify", response_model=ClassifyResponse)
async def classify(payload: ClassifyPayload):
    candidate_labels = payload.labels
    text = payload.text

    logging.info("candidate_labels : %s", candidate_labels)
    logging.info("text : %s", text)

    predictions = text_classification_model.predict(text, candidate_labels)

    logging.info("predictions : %s", predictions)

    return {"predictions": predictions}
