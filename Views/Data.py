import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show_data_analysis_page():
    st.title("Data Analysis - SRIDOC")

    # Load dummy data (replace with your actual data)
    ocr_data = {
        "Dataset": ["Typed Sinhala", "Synthetic Sinhala", "Handwritten Sinhala"],
        "Data Count": [1000, 1500, 800],
        "Accuracy": [0.85, 0.92, 0.78]
    }
    token_data = {
        "Dataset": ["Sinhala Handwritten", "Synthetic Character"],
        "Data Count": [1200, 1000],
        "Accuracy": [0.75, 0.88]
    }

    ocr_df = pd.DataFrame(ocr_data)
    token_df = pd.DataFrame(token_data)

    # OCR Data Analysis
    st.header("OCR Data Analysis")
    st.subheader("Dataset Distribution")

    fig, ax = plt.subplots()
    sns.barplot(x="Dataset", y="Data Count", data=ocr_df, ax=ax)
    st.pyplot(fig)

    st.subheader("Accuracy Comparison")

    fig, ax = plt.subplots()
    sns.barplot(x="Dataset", y="Accuracy", data=ocr_df, ax=ax)
    st.pyplot(fig)

    # Token Classification Data Analysis
    st.header("Token Classification Data Analysis")
    st.subheader("Dataset Distribution")

    fig, ax = plt.subplots()
    sns.barplot(x="Dataset", y="Data Count", data=token_df, ax=ax)
    st.pyplot(fig)

    st.subheader("Accuracy Comparison")

    fig, ax = plt.subplots()
    sns.barplot(x="Dataset", y="Accuracy", data=token_df, ax=ax)
    st.pyplot(fig)

if __name__ == "__main__":
    show_data_analysis_page()
