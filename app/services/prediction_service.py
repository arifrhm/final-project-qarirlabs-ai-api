from abc import ABC, abstractmethod


class PredictionService(ABC):
    @abstractmethod
    async def predict(self, image_data: bytes):
        pass


class RoboflowPredictionService(PredictionService):
    def __init__(self, roboflow_service):
        self.roboflow_service = roboflow_service

    async def predict(self, image_data: bytes):
        return await self.roboflow_service.predict(image_data)
