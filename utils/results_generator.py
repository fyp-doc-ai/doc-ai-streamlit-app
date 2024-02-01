import streamlit as st
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go
from utils.display_entities import displayEntities
import datetime
import os

def show_results(processed_data, uploaded_image):
    st.subheader("Results")
    id2label = {0: 'O', 1: 'B-HEADER', 2: 'I-HEADER', 3: 'B-QUESTION', 4: 'I-QUESTION', 5: 'B-ANSWER', 6: 'I-ANSWER'}

    # Load JSON data
    decoded_pred_relations = json.loads(processed_data["decoded_pred_relations"])
    entities = json.loads(processed_data["entities"])
    bboxes = json.loads(processed_data["bboxes"])
    token_labels = json.loads(processed_data["token_labels"])
    decoded_entities = json.loads(processed_data["decoded_entities"])

    # Create DataFrames
    pred_relations_df = pd.DataFrame(decoded_pred_relations, columns=["Question", "Answer"])
    entities_df = pd.DataFrame(entities, columns=["start", "end", "label"])
    token_labels_df = pd.DataFrame(token_labels, columns=["label"])

    # Plot Token Labels Frequency using Plotly
    st.subheader("Token Labels Frequency")
    label_counts = token_labels_df["label"].value_counts().reset_index()
    label_counts.columns = ["Label", "Count"]

    fig = px.bar(label_counts, x="Label", y="Count", text="Count", title="Token Labels Frequency")
    fig.update_traces(marker_color='skyblue', marker_line_color='black', opacity=0.8, textposition='outside')
    fig.update_layout(xaxis=dict(tickmode='array', tickvals=list(range(7)), ticktext=['O', 'B-HEADER', 'I-HEADER', 'B-QUESTION', 'I-QUESTION', 'B-ANSWER', 'I-ANSWER']))

    # Display the plot in Streamlit
    st.plotly_chart(fig)

    # Display Identified entities
    output_img = displayEntities(bboxes, token_labels, id2label, uploaded_image)

    # Display the image with a specified width to handle large sizes
    st.image(output_img, use_column_width='auto') 

    st.subheader("Entity Type Counts:")
    entities_df.replace({0: "HEADER", 1: "QUESTION", 2: "ANSWER"})
    entity_type_counts = entities_df["label"].value_counts().reset_index()
    entity_type_counts.columns = ["Label", "Count"]

    # Plot Entity Type Counts using Plotly
    fig_entity_type_counts = px.bar(entity_type_counts, x="Label", y="Count", text="Count", title="Entity Type Counts")
    fig_entity_type_counts.update_traces(marker_color='orange', marker_line_color='black', opacity=0.8, textposition='outside')

    # Display the plot in Streamlit
    st.plotly_chart(fig_entity_type_counts)

    # Display identified entity table
    decoded_entity_df = pd.DataFrame(decoded_entities, columns=['Entity Type', 'Entity'])
    st.subheader("Identified entities")

    st.data_editor(decoded_entity_df, key="identified_entities", num_rows='dynamic')
    st.subheader("Predicted Relations")

    # Use data editor to make the table editable and dynamic
    st.data_editor(pred_relations_df, key="predicted_relations", num_rows='dynamic')

    try:
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        folder_path = "history_results"
        os.makedirs(folder_path, exist_ok=True)

        # Save the image separately
        image_path = f"{folder_path}/img_{current_datetime}.jpg"
        save_image(uploaded_image, image_path)

        file_name = f"{folder_path}/hr_{current_datetime}.json"
        
        results_data = {
            "decoded_pred_relations": json_serializable(decoded_pred_relations),
            "entities": json_serializable(entities),
            "bboxes": json_serializable(bboxes),
            "token_labels": json_serializable(token_labels),
            "decoded_entities": json_serializable(decoded_entities),
            "uploaded_image_path": image_path,  # Save the image path instead of the image
        }

        with open(file_name, "w") as file:
            json.dump(results_data, file)
            st.success(f"Results and image saved successfully in {folder_path}")

    except Exception as e:
        st.error(f"Results not saved successfully in {folder_path}. Error: {str(e)}")

def json_serializable(data):
    if isinstance(data, (list, dict, str, int, float, bool, type(None))):
        return data
    elif hasattr(data, 'tolist'):  # convert numpy arrays to list
        return data.tolist()
    elif hasattr(data, '__dict__'):  # convert objects to their __dict__ representation
        return data.__dict__
    else:
        return str(data)  # convert other data types to string

def save_image(image, path):
    image.save(path, "JPEG")