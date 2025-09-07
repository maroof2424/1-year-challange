from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

with open("model.pkl","rb") as f:
    model = pickle.load(f)

app = FastAPI()

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def home():
    return {"message": "Wellcome to Iris Prediction API"}

@app.post("/predict")
def predict(data: IrisInput):
    features = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    prediction = model.predict(features)[0]
    species = ["setosa","versicolor","virginica"]
    result = species[prediction]

    return {"prediction":result}