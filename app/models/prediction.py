from fastapi import APIRouter, UploadFile, File, Depends
from app.services.prediction_service import (PredictionService,
                                             RoboflowPredictionService)
from app.services.roboflow_service import RoboflowService

router = APIRouter()


def get_prediction_service():
    roboflow_service = RoboflowService()
    return RoboflowPredictionService(roboflow_service)


@router.post("/predict")
async def predict(
    file: UploadFile = File(...),
    service: PredictionService = Depends(get_prediction_service),
):
    image_data = await file.read()
    result = await service.predict(image_data)
    return result
