from fastapi import APIRouter, HTTPException
from ..schemas.predict import PredictionInput
from ..crud.predict import predict_arrival_time

router = APIRouter()

@router.post("/predict")
def predict_time_to_arrival(input: PredictionInput):
    try:
        prediction = predict_arrival_time(input)
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
