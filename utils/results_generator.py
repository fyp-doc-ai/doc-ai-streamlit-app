import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import seaborn as sns
from PIL import Image, ImageDraw

def show_results(processed_data, uploaded_image):
    st.subheader("Results")

    # Load JSON data
    pred_relations = json.loads(processed_data["pred_relations"])
    entities = json.loads(processed_data["entities"])
    input_ids = json.loads(processed_data["input_ids"])
    bboxes = json.loads(processed_data["bboxes"])
    token_labels = json.loads(processed_data["token_labels"])

    # Create DataFrames
    pred_relations_df = pd.DataFrame(pred_relations)
    entities_df = pd.DataFrame(entities, columns=["start", "end", "type", "type_id"])
    input_ids_df = pd.DataFrame(input_ids)
    token_labels_df = pd.DataFrame(token_labels, columns=["label"])

    # Flatten the list of bounding boxes
    flattened_bboxes = [box for boxes in bboxes for box in boxes]
    bboxes_df = pd.DataFrame(flattened_bboxes, columns=["x1", "y1", "x2", "y2"])

    # Generate bar plot for token labels frequency
    st.subheader("Token Labels Frequency")
    sns.set_theme()
    palette = sns.color_palette("pastel")
    label_counts = token_labels_df["label"].value_counts()
    fig, ax = plt.subplots()
    bars = ax.bar(label_counts.index, label_counts.values, color=palette)

    # Label each bar with the correct category
    label_names = {
        0: 'O',
        1: 'B-HEADER',
        2: 'I-HEADER',
        3: 'B-QUESTION',
        4: 'I-QUESTION',
        5: 'B-ANSWER',
        6: 'I-ANSWER'
    }

    plt.xticks(list(label_names.keys()), [label_names[idx] for idx in label_counts.index], rotation=45, ha="right")

    for bar, count in zip(bars, label_counts.values):
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, round(count, 2), ha='center', va='bottom')

    # Display the plot in Streamlit
    st.pyplot(fig)

    st.subheader("Entity Type Counts:")
    entity_type_counts = entities_df["type"].value_counts()
    st.bar_chart(entity_type_counts)

    # Display tables
    st.subheader("Predicted Relations")
    st.table(pred_relations_df)

    # Create figure and axes
    fig, ax = plt.subplots()

    # Display the image
    ax.imshow(uploaded_image)

    # Add bounding boxes to the image
    for _, row in bboxes_df.iterrows():
        rect = patches.Rectangle((row["x1"], row["y1"]), row["x2"] - row["x1"], row["y2"] - row["y1"],
                                 linewidth=1, edgecolor='r', facecolor='none')
        ax.add_patch(rect)

    # Display the plot in Streamlit
    st.pyplot(fig)

    # Merge dataframes
    merged_df = pd.merge(pred_relations_df, entities_df, left_on=['head_id'], right_on=['end'], how='left', suffixes=('_head', '_entity'))
    merged_df = pd.merge(merged_df, entities_df, left_on=['tail_id'], right_on=['end'], how='left', suffixes=('_tail', '_entity'))

    # Display the final dataframe
    st.subheader("Merged Dataframe")
    st.table(merged_df)

