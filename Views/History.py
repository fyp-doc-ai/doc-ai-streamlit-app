import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
import os
from utils.display_entities import displayEntities
from PIL import Image


def load_results_from_file(file_path):
    # Load saved results from the specified file
    with open(file_path, "r") as file:
        saved_results = json.load(file)
    return saved_results


def load_image_from_file(image_path):
    # Load image from the specified file
    return Image.open(image_path)


def view_history_results():
    st.subheader("History Results")

    # Specify the folder where history results are stored
    folder_path = "history_results"

    # List all files in the folder
    history_files = [f for f in os.listdir(folder_path) if f.endswith(".json")]

    # Display a selectbox to choose the history file
    selected_file = st.selectbox("Select a history file:", history_files)

    if selected_file:
        file_path = os.path.join(folder_path, selected_file)
        saved_results = load_results_from_file(file_path)

        decoded_pred_relations = saved_results["decoded_pred_relations"]
        entities = saved_results["entities"]
        bboxes = saved_results["bboxes"]
        token_labels = saved_results["token_labels"]
        decoded_entities = saved_results["decoded_entities"]

        uploaded_image_path = saved_results["uploaded_image_path"]
        uploaded_image = load_image_from_file(uploaded_image_path)

        # Create DataFrames
        pred_relations_df = pd.DataFrame(
            decoded_pred_relations, columns=["Question", "Answer"]
        )
        entities_df = pd.DataFrame(entities, columns=["start", "end", "label"])
        token_labels_df = pd.DataFrame(token_labels, columns=["label"])

        # Generate bar plot for token labels frequency
        st.subheader("Token Labels Frequency")
        sns.set_theme()
        palette = sns.color_palette("pastel")
        label_counts = token_labels_df["label"].value_counts()
        fig, ax = plt.subplots()
        bars = ax.bar(label_counts.index, label_counts.values, color=palette)

        # Label each bar with the correct category
        id2label = {
            0: "O",
            1: "B-HEADER",
            2: "I-HEADER",
            3: "B-QUESTION",
            4: "I-QUESTION",
            5: "B-ANSWER",
            6: "I-ANSWER",
        }

        plt.xticks(
            list(id2label.keys()),
            [id2label[idx] for idx in label_counts.index],
            rotation=45,
            ha="right",
        )

        for bar, count in zip(bars, label_counts.values):
            yval = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                yval,
                round(count, 2),
                ha="center",
                va="bottom",
            )

        # Display the plot in Streamlit
        st.pyplot(fig)

        # Display Identified entities
        output_img = displayEntities(bboxes, token_labels, id2label, uploaded_image)
        st.image(output_img)

        st.subheader("Entity Type Counts:")
        entities_df.replace({0: "HEADER", 1: "QUESTION", 2: "ANSWER"})
        entity_type_counts = entities_df["label"].value_counts()
        st.bar_chart(entity_type_counts)

        # Display identified entity table
        decoded_entity_df = pd.DataFrame(
            decoded_entities, columns=["Entity Type", "Entity"]
        )
        st.subheader("Identified entities")

        # Use data editor to make the table editable and dynamic
        st.data_editor(
            decoded_entity_df,
            key="identified_entities",
            use_container_width=True,
            num_rows="dynamic"
        )

        # Display tables
        st.subheader("Predicted Relations")

        # Use data editor to make the table editable and dynamic
        st.data_editor(
            pred_relations_df,
            key="predicted_relations",
            use_container_width=True,
            num_rows="dynamic"
        )

    else:
        st.warning("No history files found.")
