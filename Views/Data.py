import streamlit as st
import pandas as pd
import plotly.express as px

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
    
    st.write("""
    The OCR Data Analysis section provides insights into the performance and distribution of datasets used for Optical Character Recognition (OCR) within SRIDOC. Understanding the characteristics of these datasets is crucial for optimizing OCR model training and evaluation.
    """)

    st.subheader("Dataset Distribution")

    st.write("""
    The bar chart above illustrates the distribution of different OCR datasets, including Typed Sinhala, Synthetic Sinhala, and Handwritten Sinhala. The dataset counts are represented on the y-axis, while each dataset category is shown on the x-axis. This visualization aids in identifying the volume of data available for each OCR dataset, guiding decisions on dataset prioritization and resource allocation.
    """)

    fig_ocr_data_count = px.bar(ocr_df, x="Dataset", y="Data Count", title="Dataset Distribution")
    st.plotly_chart(fig_ocr_data_count)

    st.subheader("Accuracy Comparison")

    st.write("""
    The pie chart above compares the accuracy of OCR across different datasets. Each dataset category is represented as a segment in the pie chart, with the corresponding accuracy values. This visual representation provides a quick overview of OCR accuracy across diverse dataset types, helping identify strengths and potential areas for improvement in the OCR pipeline.
    """)

    fig_ocr_accuracy_pie = px.pie(ocr_df, names="Dataset", values="Accuracy", title="Accuracy Pie Chart")
    st.plotly_chart(fig_ocr_accuracy_pie)

    # Token Classification Data Analysis
    st.header("Token Classification Data Analysis")

    st.write("""
    The Token Classification Data Analysis section delves into the characteristics of datasets used for token classification tasks within SRIDOC. Token classification involves identifying and categorizing individual elements (tokens) within a document, and understanding the dataset distribution and accuracy is essential for optimizing model performance.
    """)

    st.subheader("Dataset Distribution")

    st.write("""
    The radar chart above showcases the distribution of data across different token classification datasets, including Sinhala Handwritten and Synthetic Character. Each dataset category is represented as a point on the radar chart, and the distance from the center indicates the data count. This unique visualization provides a comprehensive overview of the distribution of token classification datasets, aiding in understanding the relative sizes of each dataset.
    """)

    fig_token_data_count_radar = px.line_polar(token_df, r=token_df["Data Count"].tolist() + [token_df["Data Count"].iloc[0]],
                                              theta=token_df["Dataset"].tolist() + [token_df["Dataset"].iloc[0]])
    st.plotly_chart(fig_token_data_count_radar)

    st.subheader("Accuracy Comparison")

    st.write("""
    The scatter plot above depicts the relationship between data count and accuracy for token classification datasets. Each point on the scatter plot represents a dataset, with its position determined by both the data count and accuracy. This visualization enables a nuanced understanding of how data distribution correlates with accuracy, aiding in strategic decisions for dataset augmentation and model training.
    """)

    fig_token_accuracy_scatter = px.scatter(token_df, x="Data Count", y="Accuracy", color="Dataset", title="Scatter Plot")
    st.plotly_chart(fig_token_accuracy_scatter)

    # Additional Plots (Replace with your actual data and analysis)
    st.header("Additional Plots")

    st.write("""
    The Additional Plots section provides supplementary visualizations to offer a more comprehensive view of data-related aspects within SRIDOC. These additional plots cover various perspectives, including pie charts, bar charts, and line charts, to capture diverse dimensions of the underlying data.
    """)

    st.subheader("Pie Chart")

    st.write("""
    The pie chart above presents a breakdown of data count across different OCR datasets. Each dataset category is represented as a segment in the pie chart, providing a visual snapshot of the proportion of data contributed by each category. Pie charts are effective for conveying relative proportions, facilitating quick comparisons between dataset components.
    """)

    fig_pie = px.pie(ocr_df, names="Dataset", values="Data Count", title="Pie Chart")
    st.plotly_chart(fig_pie)

    st.subheader("Bar Chart")

    st.write("""
    The bar chart above offers a comparison of OCR accuracy across different datasets. Each bar corresponds to a dataset category, and the height of the bar represents the corresponding accuracy value. Bar charts are valuable for visualizing variations in accuracy metrics, supporting informed decision-making for model improvement and optimization.
    """)

    fig_bar_additional = px.bar(ocr_df, x="Dataset", y="Accuracy", title="Additional Bar Chart")
    st.plotly_chart(fig_bar_additional)

    st.subheader("Line Chart")

    st.write("""
    The line chart above tracks the relationship between dataset count and accuracy for OCR datasets. Each line represents a different dataset category, providing a dynamic representation of how changes in dataset count relate to variations in accuracy. Line charts are effective for identifying trends and patterns over a continuum of values, aiding in strategic planning for dataset collection and model enhancement.
    """)

    fig_line_additional = px.line(ocr_df, x="Dataset", y="Data Count", title="Additional Line Chart")
    st.plotly_chart(fig_line_additional)

if __name__ == "__main__":
    show_data_analysis_page()
