import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def show_model_comparison_page():
    st.title("Model Comparison - SRIDOC")

    # Placeholder for references
    references = """
    References:
    [1] Reference for OCR models.
    [2] Reference for LiLT models.
    [3] Reference for Streamlit.
    [4] Reference for Plotly.
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

    st.subheader("Metrics Radar Chart - OCR Models")
    st.write("""
    The Metrics Radar Chart visually compares the performance of various OCR models, including Tesseract, Google Vision, TrOCR, MMOCR, and YOLO. Each spoke in the radar chart represents a metric (Accuracy, Precision, Recall), and the length of the spokes illustrates the corresponding metric values for each model. Tesseract and Google Vision exhibit high accuracy, while TrOCR excels in precision. This chart provides a holistic view of each model's strengths across different evaluation criteria [1].
    """)

    # Create a radar chart for OCR models using Plotly
    fig_radar_ocr = px.line_polar(ocr_model_df, r=ocr_model_df.iloc[0, 1:].values.tolist() + [ocr_model_df.iloc[0, 1]], theta=ocr_model_df.columns[1:].tolist() + [ocr_model_df.columns[1]])
    fig_radar_ocr.update_layout(polar=dict(radialaxis=dict(visible=False)))
    
    st.plotly_chart(fig_radar_ocr)

    st.subheader("Metrics Line Chart - OCR Models")
    st.write("""
    The Metrics Line Chart illustrates the trend of OCR model performance across Accuracy, Precision, and Recall. Each line represents a specific metric, and the x-axis displays the OCR models. This dynamic chart allows for a quick comparison of the models' consistency in performance over different evaluation criteria. It is evident that Tesseract and Google Vision maintain high levels of accuracy throughout the evaluation [1].
    """)


    # Create a line chart for OCR models using Plotly
    fig_line_ocr = px.line(ocr_model_df, x="Model", y=["Accuracy", "Precision", "Recall"], markers=True, labels={"value": "Metrics", "variable": "Metrics"})
    fig_line_ocr.update_layout(title="OCR Model Metrics Over Models", yaxis_title="Metrics")
    
    st.plotly_chart(fig_line_ocr)

    st.subheader("Metrics Bar Chart - OCR Models")
    st.write("""
    The Metrics Bar Chart provides a grouped comparison of OCR model metrics, including Accuracy, Precision, and Recall. Each bar represents a specific metric, and the different colors within each bar indicate the performance of individual models. This chart offers a detailed view of the models' comparative strengths and weaknesses across various evaluation criteria. Tesseract and Google Vision stand out for their high accuracy, while TrOCR excels in precision [1].
    """)

    # Create a bar chart for OCR models using Plotly
    fig_bar_ocr = px.bar(ocr_model_df, x="Model", y=["Accuracy", "Precision", "Recall"], barmode="group", labels={"value": "Metrics", "variable": "Metrics"})
    fig_bar_ocr.update_layout(title="OCR Model Metrics Comparison", yaxis_title="Metrics")
    
    st.plotly_chart(fig_bar_ocr)

    # LiLT Model Comparison
    st.header("LiLT Model Comparison")

    st.write("""
    LiLT (Language Identification and Language Transfer) is a multilingual model employed in SRIDOC for language-specific tasks. Initially trained on English, Italian, and Chinese languages, LiLT demonstrates impressive metrics [2]. The radar chart highlights LiLT's accuracy, precision, and recall when applied to Sinhala language documents. LiLT exhibits consistent and robust performance across different evaluation criteria [2].

    The line chart complements the radar chart by showcasing the trend in LiLT's metrics as it transitions from training on various languages to adapting to Sinhala. This analysis aids in understanding LiLT's adaptability and efficiency in handling diverse linguistic challenges [2].

    For more details on LiLT models and their language transfer capabilities, refer to [2] and [3].
    """)

    st.subheader("Metrics Radar Chart - LiLT Models")
    st.write("""
    The Metrics Radar Chart for LiLT models showcases the performance metrics for language identification and transfer. English, Italian, Chinese, and Sinhala languages are evaluated for Accuracy, Precision, and Recall. The radar chart illustrates LiLT's adaptability across languages, with consistent and robust performance. The longer spokes indicate higher metric values, emphasizing LiLT's effectiveness in language-specific tasks [2].
    """)


    # Create a radar chart for LiLT models using Plotly
    fig_radar_lilt = px.line_polar(lilt_model_df, r=lilt_model_df.iloc[0, 1:].values.tolist() + [lilt_model_df.iloc[0, 1]], theta=lilt_model_df.columns[1:].tolist() + [lilt_model_df.columns[1]])
    fig_radar_lilt.update_layout(polar=dict(radialaxis=dict(visible=False)))
    
    st.plotly_chart(fig_radar_lilt)

    st.subheader("Metrics Line Chart - LiLT Models")
    st.write("""
    The Metrics Line Chart for LiLT models depicts the transition in model performance metrics as LiLT adapts from training on English, Italian, and Chinese to handling Sinhala language documents. The x-axis represents different languages, and each line represents a specific metric (Accuracy, Precision, Recall). This dynamic chart provides insights into LiLT's efficiency in language transfer tasks and its ability to maintain consistent performance across diverse linguistic challenges [2].
    """)

    # Create a line chart for LiLT models using Plotly
    fig_line_lilt = px.line(lilt_model_df, x="Language", y=["Accuracy", "Precision", "Recall"], markers=True, labels={"value": "Metrics", "variable": "Metrics"})
    fig_line_lilt.update_layout(title="LiLT Model Metrics Over Languages", yaxis_title="Metrics")
    
    st.plotly_chart(fig_line_lilt)

    st.subheader("Metrics Bar Chart - LiLT Models")
    st.write("""
    The Metrics Bar Chart for LiLT models presents a grouped comparison of Accuracy, Precision, and Recall across different languages. Each bar represents a specific metric, and the grouped bars allow for a quick comparison of LiLT's performance across languages. This chart underscores LiLT's consistent and competitive metrics across diverse languages, showcasing its effectiveness in language identification and transfer tasks [2].
    """)

    # Create a bar chart for LiLT models using Plotly
    fig_bar_lilt = px.bar(lilt_model_df, x="Language", y=["Accuracy", "Precision", "Recall"], barmode="group", labels={"value": "Metrics", "variable": "Metrics"})
    fig_bar_lilt.update_layout(title="LiLT Model Metrics Comparison", yaxis_title="Metrics")
    
    st.plotly_chart(fig_bar_lilt)

    st.subheader("Overall Metrics Heat Map")

    # Combine OCR and LiLT metrics for an overall comparison
    overall_metrics_df = pd.concat([ocr_model_df.set_index("Model"), lilt_model_df.set_index("Language")], axis=0)

    # Create a heat map for overall metrics using Plotly
    fig_heatmap = px.imshow(overall_metrics_df, labels=dict(index="Model/Language", variable="Metrics", value="Value"), color_continuous_scale="Viridis")
    fig_heatmap.update_layout(title="Overall Metrics Heat Map")
    
    st.plotly_chart(fig_heatmap)

    st.subheader("Raw Metrics Data")

    # Display raw metrics data in a table
    st.write("OCR Model Metrics:")
    st.write(ocr_model_df)

    st.write("LiLT Model Metrics:")
    st.write(lilt_model_df)

    st.markdown(references, unsafe_allow_html=True)

if __name__ == "__main__":
    show_model_comparison_page()
