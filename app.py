import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Loan Approval Predictor", layout="wide")

model = pickle.load(open("model.pkl", "rb"))
encoder= pickle.load(open("label_encoder.pkl", "rb"))

st.markdown(
    """
    <style>
    .main {
        background-color: #0e1117;
        color: white;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💼 AI Loan Approval Prediction System")
st.write("Fill the details below to check loan approval status")

col1, col2, col3 = st.columns(3)

with col1:
    loan_id = st.number_input("Loan ID", step=1)
    no_of_dependents = st.number_input("Dependents", step=1)
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["Yes", "No"])

with col2:
    income_annum = st.number_input("Annual Income")
    loan_amount = st.number_input("Loan Amount",min_value=1000)
    loan_term = st.number_input("Loan Term")
    cibil_score = st.number_input("CIBIL Score")

with col3:
    residential_assets_value = st.number_input("Residential Assets Value")
    commercial_assets_value = st.number_input("Commercial Assets Value")
    luxury_assets_value = st.number_input("Luxury Assets Value")
    bank_asset_value = st.number_input("Bank Asset Value")

if st.button("Predict Loan Status"):

    input_df = pd.DataFrame([{
        "loan_id": loan_id,
        "no_of_dependents": no_of_dependents,
        "education": education.strip(),
        "self_employed": self_employed.strip(),
        "income_annum": income_annum,
        "loan_amount": loan_amount,
        "loan_term": loan_term,
        "cibil_score": cibil_score,
        "residential_assets_value": residential_assets_value,
        "commercial_assets_value": commercial_assets_value,
        "luxury_assets_value": luxury_assets_value,
        "bank_asset_value": bank_asset_value
    }])

    prediction = model.predict(input_df)
    result = encoder.inverse_transform(prediction)[0]

    proba = model.predict_proba(input_df)[0]

    st.subheader("📊 Prediction Result")

    if result == "Approved":
        st.success(f"✅ Loan Approved")
    else:
        st.error(f"❌ Loan Rejected")

