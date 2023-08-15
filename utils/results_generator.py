import streamlit as st

def show_results(processed_data):
    st.subheader("Results")

    st.write("Extracted Text:")
    st.write(processed_data["extracted_text"])

    st.subheader("Generated Graphs")
    st.write("Placeholder for graphs")