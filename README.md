Loan Prediction System using Machine Learning

Project Overview

This project is a Machine Learning-based web application that predicts whether a loan application will be approved or not based on applicant details such as income, credit history, education, and employment status.

Objective

To automate the loan approval process using a trained ML model and reduce manual decision-making errors in financial institutions.

Dataset Features

* Applicant Income

Coapplicant Income

Loan Amount

* Credit History

Education

Employment Status

* Property Area

Model Used

Random Forest Classifier

Tech Stack

Python

Pandas, NumPy

Scikit-learn

Streamlit

Pickle

Workflow

1. Data Preprocessing

2. Feature Engineering

3. Pipeline Creation (Preprocessing + Model)

4. Model Training using Random Forest

5. Model Saving using Pickle

6. Streamlit Web App for Real-time Prediction

How to Run

pip install -r requirements.txt
streamlit run app.py
📌 Future Improvements
Hyperparameter tuning for better performance
Cloud deployment (Render / AWS)
UI/UX improvements
Authentication system