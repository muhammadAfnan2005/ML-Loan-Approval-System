import joblib 
from fastapi import FastAPI, Form
import pandas as pd
from model import LoanRequest
from typing import Literal

app = FastAPI(
    title = "Loan Status Predictor",
    description = "An ML-powered service for real-time risk assessment."
)

model = joblib.load("loan_prediction.pkl")
training_columns = joblib.load("columns.pkl")

@app.get("/", tags = ["Home"])
def home():
    return {
        "message": "Loan Prediction API is running"
    }


@app.post("/predict", tags = ["Predictor"])
def predict(
    Gender: Literal["Male", "Female"] = Form(...),
    Married: Literal["Yes", "No"] = Form(...),
    Dependents: int = Form(...),
    Education: Literal["Graduate", "Not Graduate"] = Form(...),
    Self_Employed: Literal["Yes", "No"] = Form(...),
    ApplicantIncome: float = Form(...),
    CoapplicantIncome: float = Form(...),
    LoanAmount: float = Form(...),
    Loan_Amount_Term: float = Form(...),
    Credit_History: Literal["0", "1"] = Form(...),
    Property_Area: Literal["Urban", "Semiurban", "Rural"] = Form(...)
):

    input_data = {
    "Gender": Gender,
    "Married": Married,
    "Dependents": Dependents,
    "Education": Education,
    "Self_Employed": Self_Employed,
    "ApplicantIncome": ApplicantIncome,
    "CoapplicantIncome": CoapplicantIncome,
    "LoanAmount": LoanAmount,
    "Loan_Amount_Term": Loan_Amount_Term,
    "Credit_History": int(Credit_History),
    "Property_Area": Property_Area
    }

    input_df = pd.DataFrame([input_data])
    input_df = pd.get_dummies(input_df)

    for column in training_columns:
        if column not in input_df.columns:
            input_df[column] = 0

    input_df = input_df[training_columns]

    prediction = model.predict(input_df)

    result = (
        "Approved"
        if prediction[0] == 1
        else "Rejected"
    )

    return {
        "Loan Status" : result
    }