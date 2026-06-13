# ML-Loan-Approval-System

An end-to-end Machine Learning application that predicts whether a loan application should be approved or rejected using a Random Forest Classifier. The trained model is deployed using FastAPI and supports real-time predictions through an interactive Swagger interface.

## Overview

This project demonstrates the complete Machine Learning lifecycle, from data preprocessing and model training to API deployment.

The system accepts applicant information, applies the same preprocessing used during training, and predicts whether the loan should be approved.

---

## Features

- Loan approval prediction using Machine Learning
- Random Forest Classifier
- FastAPI deployment
- Interactive Swagger documentation
- Form-based user input through Swagger UI
- One-Hot Encoding using Pandas
- Model persistence using Joblib
- Automatic request validation
- Real-time predictions

---

## Technologies Used

### Machine Learning
- Python
- Scikit-learn
- Pandas
- NumPy

### API Development
- FastAPI
- Uvicorn
- Pydantic

### Model Persistence
- Joblib

---

## Dataset

The project uses a Loan Prediction dataset containing applicant information such as:

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

### Target Variable

Loan Status:

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

The following metrics were used:

- Accuracy
- Confusion Matrix
- Precision
- Recall
- F1-Score
- Classification Report

After comparison, Random Forest was selected as the final model.

---

## API Workflow

```
User Input
    ↓
Swagger Form Interface
    ↓
FastAPI
    ↓
DataFrame Conversion
    ↓
One-Hot Encoding
    ↓
Column Alignment
    ↓
Random Forest Prediction
    ↓
Response Returned
```

---

## Project Structure

```
ML-Loan-Approval-System/
│
├── main.py
├── model.py
├── loan_prediction.pkl
├── columns.pkl
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ML-Loan-Approval-System.git
```

Move into the project directory:

```bash
cd ML-Loan-Approval-System
```

Run the application:

```bash
uvicorn main:app --reload
```

---

## API Documentation

After starting the server, open:

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

- Prediction probabilities
- Database logging using SQLAlchemy
- Docker support
- Cloud deployment
- Frontend dashboard
- Scikit-learn Pipelines
- Model monitoring

---

## What I Learned

This project helped me gain practical experience in:

- Building classification models
- Comparing Decision Trees and Random Forests
- Evaluating machine learning models
- Handling preprocessing during deployment
- Deploying models using FastAPI
- Creating production-style prediction APIs

---

## Author

**Muhammad Afnan**

BS Computer Science Student  
Aspiring Data Scientist and AI Engineer
