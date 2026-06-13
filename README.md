# LoanWise-ML-API

An end-to-end Machine Learning application that predicts whether a loan application should be approved or rejected using a Random Forest Classifier. The model is deployed using FastAPI and provides real-time predictions through an interactive Swagger interface.

---

## Features

- Loan approval prediction using Machine Learning
- Random Forest Classifier
- FastAPI deployment
- Interactive Swagger UI
- Form-based input support
- One-Hot Encoding using Pandas
- Model persistence using Joblib
- Input validation with FastAPI
- Ready for deployment

---

## Tech Stack

### Machine Learning
- Python
- Scikit-learn
- Pandas
- NumPy

### Deployment
- FastAPI
- Uvicorn
- Joblib

### Documentation
- Swagger UI (FastAPI Docs)

---

## Dataset

This project uses the Loan Prediction dataset containing applicant information such as:

- Gender
- Marital Status
- Dependents
- Education
- Self Employment Status
- Applicant Income
- Co-applicant Income
- Loan Amount
- Loan Term
- Credit History
- Property Area

Target Variable:

- Loan Status
    - Approved
    - Rejected

---

## Machine Learning Workflow

1. Data Cleaning
2. Missing Value Handling
3. Exploratory Data Analysis
4. One-Hot Encoding
5. Train-Test Split
6. Decision Tree Training
7. Random Forest Training
8. Model Evaluation
9. Model Serialization using Joblib
10. FastAPI Deployment

---

## Model Evaluation

The following metrics were used to evaluate the models:

- Accuracy
- Confusion Matrix
- Precision
- Recall
- F1-Score
- Classification Report

Random Forest was selected as the final model due to its superior performance.

---

## API Workflow

User Input
↓
FastAPI Forms / Swagger UI
↓
DataFrame Conversion
↓
One-Hot Encoding
↓
Column Alignment
↓
Random Forest Model
↓
Prediction
↓
JSON Response

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/LoanWise-ML-API.git
```

Move into the project directory:

```bash
cd LoanWise-ML-API
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn main:app --reload
```

---

## API Documentation

After running the application, visit:

```
http://127.0.0.1:8000/docs
```

FastAPI automatically generates interactive API documentation using Swagger UI.

---

## Example Prediction Response

```json
{
    "loan_status": "Approved"
}
```

---

## Future Improvements

- Probability-based predictions
- Database logging using SQLAlchemy
- Docker support
- Cloud deployment
- Frontend dashboard
- Scikit-learn Pipelines
- Model monitoring

---

## Project Structure

```
LoanWise-ML-API/
│
├── main.py
├── schemas.py
├── loan_model.pkl
├── columns.pkl
├── requirements.txt
└── README.md
```

---

## Learning Outcomes

Through this project, I gained hands-on experience with:

- Building Machine Learning models
- Comparing Decision Trees and Random Forests
- Evaluating classification models
- Deploying ML models with FastAPI
- Handling real-world preprocessing challenges
- Designing production-oriented prediction APIs

---

## Author

Muhammad Afnan

BS Computer Science Student | Aspiring Data Scientist & AI Engineer
