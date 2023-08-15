import streamlit as st
import time
from PIL import Image
from utils.image_processing import process_image
from utils.results_generator import show_results
from utils.spinner import loading_spinner

def main():
    st.set_page_config(page_title="DocAI", page_icon=":memo:")
    
    st.title("Document AI")

    uploaded_file = st.file_uploader("Upload a scanned image or document", type=["jpg", "png"])

    if uploaded_file is not None:

        if st.button("View Results"):
            with st.spinner(text="In progress..."):
                processed_data = process_image(uploaded_file)
                st.session_state.processed_data = processed_data
                msg = st.toast('Gathering data...')
                time.sleep(1)
                msg.toast('Processing...')
                time.sleep(4)
                msg.toast('Ready!')
                time.sleep(1)

            uploaded_image = Image.open(uploaded_file)
            st.image(uploaded_image, caption="Uploaded Image/Document", use_column_width=True)    
            show_results(processed_data)

if __name__ == "__main__":
    main()
