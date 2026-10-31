import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Credit Risk Assessment", page_icon="📊", layout="centered")
st.title("Risk Analytics: Credit Default Prediction Engine")
st.caption("A data-driven underwriting tool built with Python.")
st.markdown("---")

st.sidebar.header("Applicant Parameters")
income = st.sidebar.slider("Annual Income (₹ LPA)", 2.0, 40.0, 12.0, 0.5)
loan_amount = st.sidebar.slider("Requested Loan (₹ LPA)", 1.0, 30.0, 6.0, 0.5)
cibil_score = st.sidebar.slider("CIBIL Score", 300, 900, 720, 5)
age = st.sidebar.slider("Age", 21, 65, 32, 1)

dti_ratio = (loan_amount / income) * 100
log_odds = (dti_ratio * 0.05) - ((cibil_score - 300) / 120) + (age * 0.01) - 0.5
probability_of_default = 1 / (1 + np.exp(-log_odds))

st.subheader("Credit Evaluation Summary")
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Debt-to-Income (DTI) Ratio", value=f"{round(dti_ratio, 1)}%")
with col2:
    st.metric(label="Calculated Default Risk", value=f"{round(probability_of_default * 100, 1)}%")

st.markdown("### Underwriting Decision")
if probability_of_default > 0.65 or cibil_score < 550:
    st.error("🚨 **Application Rejected:** Profile exceeds risk tolerances.")
elif probability_of_default > 0.35 or dti_ratio > 60:
    st.warning("⚠️ **Refer to Manual Underwriting:** Moderate risk profile.")
else:
    st.success("✅ **Automated Approval:** Low-risk profile.")
