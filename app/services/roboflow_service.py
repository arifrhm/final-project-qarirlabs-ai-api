from roboflow import Roboflow
from app.core.config import settings


class RoboflowService:
    def __init__(self):
        rf = Roboflow(api_key=settings.ROBOFLOW_API_KEY)
        self.project = rf.workspace().project(settings.MODEL_ID)
        self.model = self.project.version(1).model

    async def predict(self, image_data: bytes):
        return self.model.predict(image_data, confidence=40, overlap=30).json()
