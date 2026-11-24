from fastapi import FastAPI, HTTPException

from backend.schemas import PredictionRequest

app = FastAPI(title="UK IT Salary Prediction")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/predict")
def predict(request: PredictionRequest) -> None:
    raise HTTPException(status_code=503, detail="Salary model is not available yet.")
