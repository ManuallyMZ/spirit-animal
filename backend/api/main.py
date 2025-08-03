from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, '..', 'models', 'animal_model.pkl')
encoder_path = os.path.join(BASE_DIR, '..','models','animal_encoder.pkl')

model = joblib.load(model_path)
encoder = joblib.load(encoder_path)

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:5173",
    "https://spirit-animal-781i.vercel.app",
    "https://spirit-animal-nimaramezani.vercel.app",
    "https://spirit-animal-nima-ramezani.vercel.app",
    "https://spirit-animal-781i-lnwffr5m6-manuallymzs-projects.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QuizAnswers(BaseModel):
    social_preference: str
    energy_time: str
    activity: str
    pace: str
    stress_response: str
    favorite_color: str


@app.post("/predict")
def predict_animal(answers: QuizAnswers):
    input_df = pd.DataFrame([answers.dict()])

    input_encoded = encoder.transform(input_df)

    prediction = model.predict(input_encoded)[0]

    return {"predicted_animal": prediction}
