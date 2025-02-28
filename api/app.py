from fastapi import FastAPI
import pickle
import pandas as pd
from pydantic import BaseModel

# Load the trained model
model_path = "model/model.pkl"
with open(model_path, "rb") as f:
    model = pickle.load(f)

app = FastAPI()

# Define the input data structure
class InputData(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.post("/predict/")
def predict(data: InputData):
    input_df = pd.DataFrame([data.model_dump()])
    prediction = model.predict(input_df)[0]
    return {"prediction": prediction}
