from fastapi import FastAPI
from app.api.routes import prediction

app = FastAPI(title="AI Engineering Service")

app.include_router(prediction.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
