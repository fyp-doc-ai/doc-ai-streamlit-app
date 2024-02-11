import streamlit as st
import pandas as pd
import plotly.express as px

def show_OCR_Results():
    st.title("Optical Character Recognition Model")

    # OCR Data Analysis
    st.header("Results")
    
    st.write("""
    In line with our methodology, we undertake a comprehensive evaluation of multiple Optical Character Recognition (OCR) tools. To ensure a thorough assessment, we train these OCR tools using a combination of synthetic and handwritten text data, as outlined in the Methodology section.
    """)
    st.write("""
    The training process involves exposing the OCR tools to both synthetic text, generated using handwritten fonts to mimic the appearance of genuine handwriting, and actual handwritten text. By training on this diverse dataset, we aim to equip the OCR tools with the capability to accurately recognize and interpret text across different styles and formats.
    """)
    st.write("""
    Following the training phase, we proceed to evaluate the performance of each OCR tool across three distinct types of data: printed text, synthetic handwriting, and actual handwritten text. This evaluation allows us to gauge the OCR tools' effectiveness in accurately transcribing text under various conditions and scenarios.
    """)    
    st.write("""
    The results of this evaluation, showcasing the performance metrics obtained for each OCR tool across the different types of data, are presented in below table. These metrics provide valuable insights into the OCR tools' overall performance in handling printed, synthetic handwriting, and handwritten text.
    """)
    st.write("""
    By systematically comparing the results obtained from different OCR tools across the varied datasets, we gain a comprehensive understanding of their strengths, weaknesses, and suitability for different text recognition tasks. This information serves as a crucial foundation for selecting the most appropriate OCR tool for specific use cases and guiding future optimization efforts in the field of text recognition.
    """)
    st.write("""
    In our evaluation of Optical Character Recognition (OCR) models, we employ a metric known as the Character Error Rate (CER). This metric serves as a quantitative measure of the accuracy of OCR models in transcribing text.
    """)    
    st.write("""
    The Character Error Rate (CER) is calculated based on the number of substitutions (S), deletions (D), and insertions (I) made by the OCR model when compared to the reference text. These operations represent the discrepancies between the OCR output and the actual text.
    """)

    cer_equation = r"""
    The Character Error Rate (CER) for a given reference text and its OCR output is defined as follows:

    $$ 
    \begin{align*}
    CER = \frac{S + D + I}{N} = \frac{S + D + I}{S + D + C}
    \end{align*}    
    $$

    $$
    \begin{align*}
    \text{ where,} \\
    & S \text{ is the number of substitutions,} \\
    & D \text{ is the number of deletions,} \\
    & I \text{ is the number of insertions,} \\
    & C \text{ is the number of correct characters,} \\
    & N \text{ is the total number of characters in the reference (} N = S + D + C \text{).} \\
    \end{align*}
    $$

    The formula calculates the ratio of the total errors (substitutions, deletions, and insertions) to the total number of characters in the reference text.

    The components are further detailed as:
    $$
    \begin{align*}
    & S + D \text{ represents the total number of errors (substitutions and deletions),} \\
    & S + D + C \text{ represents the total number of correct characters and errors.} \\
    \end{align*}
    $$

    In simpler terms, the CER is a ratio that measures the total number of errors made by the OCR model (substitutions, deletions, and insertions) relative to the total number of characters in the reference text. By quantifying these errors in relation to the reference text, the CER provides valuable insights into the accuracy and reliability of OCR models in transcribing text accurately.    
    """

    st.markdown(cer_equation, unsafe_allow_html=True)


    st.subheader("OCR Model Comparison")

# OCR Method Comparison Data
    ocr_method_data = {
        "Method": ["Google Cloud Vision (no training)", "TrOCR", "Tesseract (no training)", 
                   "Tesseract (fine-tuned synthetic)", "Tesseract (fine-tuned synthetic + handwritten)"],
        "Printed": [0.0291, 0.6974, 0.3314, 0.0625, 0.1520],
        "Synthetic": [0.4598, 0.5860, 0.6325, 0.3239, 0.3968],
        "Handwritten": [0.7614, 0.7241, 0.8304, 0.7586, 0.5201]
    }

    ocr_method_df = pd.DataFrame(ocr_method_data)

    # YOLOv8 Method Comparison Data
    yolo_method_data = {
        "Method": ["YOLOv8"],
        "Precision": [0.487],
        "Recall": [0.246],
        "F1": [0.326]
    }

    yolo_method_df = pd.DataFrame(yolo_method_data)


    st.write("""
    This comparison evaluates the performance of various OCR methods across different document types. The table provides precision, recall, and F1 score for each method. Notable methods include Google Cloud Vision, TrOCR, and Tesseract with different training scenarios. The bar charts offer a visual representation of each method's performance across printed, synthetic, and handwritten documents.
    """)

    st.table(ocr_method_df)

    fig_bar_ocr = px.bar(ocr_method_df.melt(id_vars="Method"), x="Method", y="value", color="variable",
                        facet_col="variable", barmode="group", labels={"value": "Metrics", "variable": "Metrics"})
    fig_bar_ocr.update_layout(title="OCR Method Metrics Comparison", yaxis_title="Metrics")
    
    st.plotly_chart(fig_bar_ocr)

    st.table(yolo_method_df)

    fig_bar_yolo = px.bar(yolo_method_df.melt(id_vars="Method"), x="Method", y="value", color="variable",
                         facet_col="variable", barmode="group", labels={"value": "Metrics", "variable": "Metrics"})
    fig_bar_yolo.update_layout(title="YOLOv8 Method Metrics Comparison", yaxis_title="Metrics")
    st.plotly_chart(fig_bar_yolo)

    st.markdown("[Read More](#)") 

if __name__ == "__main__":
    show_OCR_Results()
