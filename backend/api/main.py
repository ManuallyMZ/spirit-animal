from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os

# Load model and encoder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, '..', 'models', 'animal_model.pkl')
encoder_path = os.path.join(BASE_DIR, '..','models','animal_encoder.pkl')

model = joblib.load(model_path)
encoder = joblib.load(encoder_path)

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # or "*" for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request body schema


class QuizAnswers(BaseModel):
    social_preference: str
    energy_time: str
    activity: str
    pace: str
    stress_response: str
    favorite_color: str


@app.post("/predict")
def predict_animal(answers: QuizAnswers):
    # Convert to DataFrame
    input_df = pd.DataFrame([answers.dict()])

    # Encode features
    input_encoded = encoder.transform(input_df)

    # Predict
    prediction = model.predict(input_encoded)[0]

    return {"predicted_animal": prediction}
