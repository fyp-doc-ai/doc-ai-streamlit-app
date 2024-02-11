import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


def show_LiLT_Results():
    st.title("Document Understanding Model")

    # OCR Model Comparison
    st.header("Results")

    st.write(
        """
Our document understanding task involves two sub-tasks: Semantic Entity Recognition (SER) and Relationship Extraction (RE). To address these tasks effectively, we train two separate models based on the LiLT architecture, each tailored to handle its respective sub-task.
For Semantic Entity Recognition (SER), the model is trained to classify different elements within documents, such as questions, answers, and headers. Meanwhile, the Relationship Extraction (RE) model focuses on identifying and delineating connections or relationships between entities within the documents.

    """
    )

    st.write("""
To train these models, we utilize the curated forms dataset created during the data collection phase. This dataset serves as the training data, providing the models with labeled examples to learn from. Through the training process, the models acquire the ability to recognize and classify semantic entities and extract relationships between them.
By training and evaluating these models, we aim to assess their capability to accurately recognize semantic entities and extract relationships within documents. This information is crucial for determining the models' suitability for real-world document understanding tasks and guiding further optimization efforts.

    """)

    st.write("""
To comprehensively assess the performance of our models when applied to Sinhala data, we adopt a two-step approach. Initially, we train the models exclusively using English data to establish a baseline understanding of their capabilities. Subsequently, we evaluate the models' performance on Sinhala data in a zero-shot transfer scenario, where the models are tasked with processing Sinhala documents without any explicit training on the Sinhala language.
It's important to note that there are no existing official results available for models utilizing XLM-R when applied to Sinhala data. Therefore, we conduct our own training and evaluation process to generate results for comparison.
    """)

    st.write(
        """
During the training phase, both models are trained for 10,000 steps, with a batch size of 8. This extensive training process ensures that the models have sufficient exposure to the English dataset, allowing them to learn and refine their understanding of document semantics and relationships.

    """
    )

    st.write(
        """
Once the training is completed, we proceed to evaluate the models' performance on Sinhala data. This zero-shot transfer evaluation tests the models' ability to generalize their learned knowledge from English to Sinhala without any explicit training on the Sinhala language.

    """
    )

    st.write(
        """
The results of this evaluation task are presented in below table, providing insights into how effectively the models can adapt to processing Sinhala documents based on their prior training on English data. These results serve as a valuable benchmark for assessing the models' cross-linguistic transfer capabilities and guiding future optimization efforts for multilingual document understanding tasks.

    """
    )

    st.subheader("Zero-shot transfer results")

    zero_shot_data = {
        "Task": ["SER", "RE"],
        "Precision (English FUNSD)": [0.7252, 0.3264],
        "Recall (English FUNSD)": [0.7718, 0.4864],
        "F1 (English FUNSD)": [0.7478, 0.3906],
        "Precision (Sinhala)": [0.4541, 0.3247],
        "Recall (Sinhala)": [0.6820, 0.4172],
        "F1 (Sinhala)": [0.5452, 0.3652],
    }

    zero_shot_df = pd.DataFrame(zero_shot_data)
    st.table(zero_shot_df)

    fig = px.bar(
        zero_shot_df,
        x="Task",
        y=[
            "Precision (English FUNSD)",
            "Recall (English FUNSD)",
            "F1 (English FUNSD)",
            "Precision (Sinhala)",
            "Recall (Sinhala)",
            "F1 (Sinhala)",
        ],
        # title="Zero-shot Transfer Results",
        labels={"value": "Metrics", "variable": "Task"},
        barmode="group",
    )

    st.plotly_chart(fig)


    st.write("""
In the next phase of our evaluation, we embark on training both models using exclusively Sinhala data. This step is crucial as it allows us to gauge the models' performance when trained specifically on Sinhala language documents.
    """)

    st.write("""
Following the training phase, we proceed to evaluate the models' performance based on their ability to process and understand Sinhala documents. This evaluation provides valuable insights into how well the models can handle Sinhala text after being trained on a Sinhala-specific dataset.
    """)

    st.write("""
Subsequently, we delve into a re-training process using the models from the previous zero-shot transfer experiment. This re-training involves fine-tuning the models using additional Sinhala data. By doing so, we aim to capitalize on the knowledge and understanding acquired by the models during the zero-shot transfer phase, further enhancing their performance on Sinhala documents.
    """)

    st.write("""
Once the re-training is completed, we conduct another round of evaluation to assess the impact of fine-tuning the models with Sinhala data. This evaluation allows us to compare the performance of the models before and after re-training, providing insights into the effectiveness of the re-training process in improving their proficiency in processing Sinhala text.
    """)

    st.write("""
The evaluation results of these experiments are summarized in Table 4, offering a comprehensive overview of the models' performance across different training and re-training scenarios. These results serve as a valuable reference for understanding the models' adaptability and performance in handling Sinhala language documents, ultimately guiding further refinement and optimization efforts.
    """)

    st.subheader("Document understanding results")


    document_results_data = {
        "Task": ["SER", "RE"],
        "Precision (Sin)": [0.7247, 0.3388],
        "Recall (Sin)": [0.7770, 0.5497],
        "F1 (Sin)": [0.7499, 0.4192],
        "Precision (Eng+Sin)": [0.7386, 0.4858],
        "Recall (Eng+Sin)": [0.7967, 0.6821],
        "F1 (Eng+Sin)": [0.7665, 0.5675]
    }

    document_results_df = pd.DataFrame(document_results_data)
    st.table(document_results_df)
    
    fig = px.bar(document_results_df, x="Task", y=["Precision (Sin)", "Recall (Sin)", "F1 (Sin)", 
                                                   "Precision (Eng+Sin)", "Recall (Eng+Sin)", "F1 (Eng+Sin)"],
                #  title="Document Understanding Results",
                 labels={"value": "Metrics", "variable": "Task"},
                 barmode="group")
    
    st.plotly_chart(fig)


    st.write("""
In addition to our experimentation with the zero-shot transfer and fine-tuning methods for the RE (Relationship Extraction) task using Sinhala data, we expanded our investigation to include languages such as Italian, Japanese, and Chinese. This broader exploration allowed us to assess the effectiveness of these methods across a diverse range of languages and linguistic structures. By applying the zero-shot transfer method, we aimed to evaluate how well the models trained on English data could adapt to processing documents in Italian, Japanese, and Chinese languages without explicit training in those languages.
    """)

    st.write("""
Furthermore, by employing the fine-tuning method, we sought to enhance the models' performance on RE tasks in these languages by providing additional training using datasets specific to each language. Through these experiments, we aimed to gain insights into the transferability and adaptability of our models across different languages and to identify strategies for optimizing their performance in multilingual document understanding tasks. Below table shows the results of these experiments.
    """)

    st.subheader("Language Performance")

    # Language performance data
    language_performance_data = {
        "Language": ["Italian", "Japanese", "Chinese"],
        "Precision (Trained)": [0.4301, 0.4372, 0.3910],
        "Recall (Trained)": [0.7109, 0.6574, 0.6703],
        "F1 (Trained)": [0.5359, 0.5251, 0.4939],
        "Precision (Zero-shot)": [None, 0.1690, 0.1621],
        "Recall (Zero-shot)": [None, 0.3377, 0.1986],
        "F1 (Zero-shot)": [None, 0.2252, 0.1785],
        "Precision (After Fine-tuning)": [0.4572, None, 0.4194],
        "Recall (After Fine-tuning)": [0.6026, None, 0.5165],
        "F1 (After Fine-tuning)": [0.5200, None, 0.4629],
    }

    language_performance_df = pd.DataFrame(language_performance_data)
    st.table(language_performance_df)

    fig = px.bar(language_performance_df, x="Language", y=["Precision (Trained)", "Recall (Trained)", "F1 (Trained)", 
                                                           "Precision (Zero-shot)", "Recall (Zero-shot)", "F1 (Zero-shot)",
                                                           "Precision (After Fine-tuning)", "Recall (After Fine-tuning)", "F1 (After Fine-tuning)"],
                 title="Language Performance Metrics",
                 labels={"value": "Metrics", "variable": "Language"},
                 barmode="group")
    
    st.plotly_chart(fig)

    st.write(
        """
    The inclusion of layout information plays a crucial role in facilitating multilingual document understanding. Layout information provides valuable contextual cues and structural clues within documents, which aid in the interpretation and extraction of text regardless of the language used. This allows our method to effectively navigate and comprehend documents written in various languages, thereby enabling robust performance in multilingual settings.
    """
    )
    st.write(
        """
    Overall, the successful performance of our method in multilingual scenarios underscores the importance of leveraging layout information as a foundational element in document understanding. By harnessing layout information, our approach demonstrates versatility and adaptability, making it well-suited for handling diverse linguistic contexts and facilitating efficient document processing across different languages.
    """
    )

    st.markdown("[Read More](#)") 

if __name__ == "__main__":
    show_LiLT_Results()
