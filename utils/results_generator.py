import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
from utils.display_entities import displayEntities

def show_results(processed_data, uploaded_image):
    st.subheader("Results")

    # Load JSON data
    # pred_relations = json.loads(processed_data["pred_relations"])
    decoded_pred_relations = json.loads(processed_data["decoded_pred_relations"])
    entities = json.loads(processed_data["entities"])
    # input_ids = json.loads(processed_data["input_ids"])
    bboxes = json.loads(processed_data["bboxes"])
    token_labels = json.loads(processed_data["token_labels"])
    decoded_entities = json.loads(processed_data["decoded_entities"])

    # Create DataFrames
    pred_relations_df = pd.DataFrame(decoded_pred_relations, columns=["Question", "Answer"])
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
        0: 'O',
        1: 'B-HEADER',
        2: 'I-HEADER',
        3: 'B-QUESTION',
        4: 'I-QUESTION',
        5: 'B-ANSWER',
        6: 'I-ANSWER'
    }

    plt.xticks(list(id2label.keys()), [id2label[idx] for idx in label_counts.index], rotation=45, ha="right")

    for bar, count in zip(bars, label_counts.values):
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, round(count, 2), ha='center', va='bottom')

    # Display the plot in Streamlit
    st.pyplot(fig)

    # Display Identified entities
    output_img = displayEntities(bboxes, token_labels, id2label, uploaded_image)
    st.image(output_img)

    st.subheader("Entity Type Counts:")
    entities_df.replace({0:"HEADER", 1:"QUESTION", 2:"ANSWER"})
    entity_type_counts = entities_df["label"].value_counts()
    st.bar_chart(entity_type_counts)

    # Display identified entity table
    decoded_entity_df = pd.DataFrame(decoded_entities, columns=['Entity Type', 'Entity'])
    st.subheader("Identified entities")
    st.table(decoded_entity_df)

    # Display tables
    st.subheader("Predicted Relations")
    st.table(pred_relations_df)
    # # Merge dataframes
    # merged_df = pd.merge(pred_relations_df, entities_df, left_on=['head_id'], right_on=['end'], how='left', suffixes=('_head', '_entity'))
    # merged_df = pd.merge(merged_df, entities_df, left_on=['tail_id'], right_on=['end'], how='left', suffixes=('_tail', '_entity'))

    # # Display the final dataframe
    # st.subheader("Merged Dataframe")
    # st.table(merged_df)

