from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Initialize FastAPI app
app = FastAPI(title="GreenGuard API", description="API for predicting Solar AC Power", version="1.0")

# Load the trained Random Forest model
model = joblib.load("models/rf_greenguard.pkl")

# Define input data schema
class InputData(BaseModel):
    IRRADIATION: float
    AMBIENT_TEMPERATURE: float
    MODULE_TEMPERATURE: float
    DC_POWER: float

@app.get("/")
def home():
    return {"message": "Welcome to GreenGuard API! Go to /docs for Swagger UI."}

@app.post("/predict")
def predict(data: InputData):
    try:
        # Convert input to numpy array for prediction
        features = np.array([[data.IRRADIATION, data.AMBIENT_TEMPERATURE, data.MODULE_TEMPERATURE, data.DC_POWER]])
        
        prediction = model.predict(features)[0]

        return {
            "AC_POWER": round(float(prediction), 2),
            "Input_Features": data.dict()
        }
    except Exception as e:
        return {"error": str(e)}
