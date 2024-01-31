# ModelComparisonPage.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def show_model_comparison_page():
    st.title("Model Comparison - SRIDOC")

    # Placeholder for references
    references = """
    References:
    [1] Reference for OCR models.
    [2] Reference for LiLT models.
    [3] Reference for Streamlit.
    [4] Reference for Matplotlib.
    [5] Reference for Seaborn.
    """

    # OCR Model Comparison Data (replace with actual metrics)
    ocr_model_data = {
        "Model": ["Tesseract", "Google Vision", "TrOCR", "MMOCR", "YOLO"],
        "Accuracy": [0.85, 0.92, 0.78, 0.89, 0.77],
        "Precision": [0.82, 0.91, 0.76, 0.88, 0.75],
        "Recall": [0.87, 0.93, 0.79, 0.90, 0.78]
    }

    ocr_model_df = pd.DataFrame(ocr_model_data)

    # LiLT Model Comparison Data (replace with actual metrics)
    lilt_model_data = {
        "Language": ["English", "Italian", "Chinese", "Sinhala"],
        "Accuracy": [0.91, 0.89, 0.88, 0.86],
        "Precision": [0.88, 0.85, 0.87, 0.84],
        "Recall": [0.92, 0.91, 0.89, 0.88]
    }

    lilt_model_df = pd.DataFrame(lilt_model_data)

    # OCR Model Comparison
    st.header("OCR Model Comparison")

    st.write("""
    OCR (Optical Character Recognition) is a crucial component in SRIDOC's document digitization process. In this comparison, we evaluate five prominent OCR models: Tesseract, Google Vision, TrOCR, MMOCR, and YOLO [1]. The radar chart provides a comprehensive view of each model's accuracy, precision, and recall. Tesseract and Google Vision stand out with high accuracy, while TrOCR excels in precision. YOLO, known for object detection, demonstrates competitive performance in OCR tasks [1].

    Additionally, the line chart tracks the performance trend of each model across accuracy, precision, and recall. This dynamic visualization aids in understanding the consistency of model metrics over different evaluation criteria [1].

    For more information on OCR models and their capabilities, refer to [1] and [3].
    """)

    st.subheader("Metrics Radar Chart")

    # Create a radar chart for OCR models
    fig_radar_ocr, ax_radar_ocr = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    
    categories = list(ocr_model_df.columns[1:])
    values = ocr_model_df.loc[0].drop("Model").values.flatten().tolist()
    values += values[:1]

    angles = [n / float(len(categories)) * 2 * np.pi for n in range(len(categories))]
    angles += angles[:1]

    ax_radar_ocr.fill(angles, values, color="skyblue", alpha=0.25)
    ax_radar_ocr.set_yticklabels([])
    ax_radar_ocr.set_xticks(angles[:-1])
    ax_radar_ocr.set_xticklabels(categories)

    st.pyplot(fig_radar_ocr)

    st.subheader("Metrics Line Chart")

    # Create a line chart for OCR models
    fig_line_ocr, ax_line_ocr = plt.subplots(figsize=(8, 4))
    sns.lineplot(x="Model", y="Accuracy", data=ocr_model_df, marker='o', label="Accuracy", ax=ax_line_ocr)
    sns.lineplot(x="Model", y="Precision", data=ocr_model_df, marker='o', label="Precision", ax=ax_line_ocr)
    sns.lineplot(x="Model", y="Recall", data=ocr_model_df, marker='o', label="Recall", ax=ax_line_ocr)
    ax_line_ocr.set(title="OCR Model Metrics Over Models", ylabel="Metrics")
    ax_line_ocr.legend(loc="upper left")

    st.pyplot(fig_line_ocr)

    # LiLT Model Comparison
    st.header("LiLT Model Comparison")

    st.write("""
    LiLT (Language Identification and Language Transfer) is a multilingual model employed in SRIDOC for language-specific tasks. Initially trained on English, Italian, and Chinese languages, LiLT demonstrates impressive metrics [2]. The radar chart highlights LiLT's accuracy, precision, and recall when applied to Sinhala language documents. LiLT exhibits consistent and robust performance across different evaluation criteria [2].

    The line chart complements the radar chart by showcasing the trend in LiLT's metrics as it transitions from training on various languages to adapting to Sinhala. This analysis aids in understanding LiLT's adaptability and efficiency in handling diverse linguistic challenges [2].

    For more details on LiLT models and their language transfer capabilities, refer to [2] and [3].
    """)

    st.subheader("Metrics Radar Chart")

    # Create a radar chart for LiLT models
    fig_radar_lilt, ax_radar_lilt = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    
    categories = list(lilt_model_df.columns[1:])
    values = lilt_model_df.loc[0].drop("Language").values.flatten().tolist()
    values += values[:1]

    angles = [n / float(len(categories)) * 2 * np.pi for n in range(len(categories))]
    angles += angles[:1]

    ax_radar_lilt.fill(angles, values, color="lightcoral", alpha=0.25)
    ax_radar_lilt.set_yticklabels([])
    ax_radar_lilt.set_xticks(angles[:-1])
    ax_radar_lilt.set_xticklabels(categories)

    st.pyplot(fig_radar_lilt)

    st.subheader("Metrics Line Chart")

    # Create a line chart for LiLT models
    fig_line_lilt, ax_line_lilt = plt.subplots(figsize=(8, 4))
    sns.lineplot(x="Language", y="Accuracy", data=lilt_model_df, marker='o', label="Accuracy", ax=ax_line_lilt)
    sns.lineplot(x="Language", y="Precision", data=lilt_model_df, marker='o', label="Precision", ax=ax_line_lilt)
    sns.lineplot(x="Language", y="Recall", data=lilt_model_df, marker='o', label="Recall", ax=ax_line_lilt)
    ax_line_lilt.set(title="LiLT Model Metrics Over Languages", ylabel="Metrics")
    ax_line_lilt.legend(loc="upper left")

    st.pyplot(fig_line_lilt)

    st.markdown(references, unsafe_allow_html=True)

if __name__ == "__main__":
    show_model_comparison_page()
