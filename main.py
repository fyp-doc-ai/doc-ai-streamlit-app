import streamlit as st
import time
import requests
from PIL import Image
from io import BytesIO
from utils.image_processing import process_image
from utils.results_generator import show_results
from utils.spinner import loading_spinner
from streamlit_lottie import st_lottie


def main():
    st.set_page_config(page_title="SRIDOC", page_icon="Logo.png")

    col1, col2, col3 = st.columns(3)
    col2.image("Logo.png", width=120)
    st.markdown("<h4 style='text-align: center; color: grey;'>Comprehensive Handwritten Document Digitization Solution!</h4>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: grey; font-size: small; font-style: italic;'> Introducing our cutting-edge mobile application, equipped with the latest models for digitizing and extracting question-answer pairs from forms in both English and Sinhala languages. Our advanced framework ensures optimal outcomes, leveraging state-of-the-art models to deliver the highest accuracy.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: grey; font-size: small; font-style: italic;'> Additionally, the application provides users with the ability to offer valuable feedback, contributing to continuous improvement. We prioritize the full privacy of your data through innovative techniques like federated learning, ensuring a secure and personalized experience. Welcome to a new era of form digitization and extraction, where efficiency meets privacy in the palm of your hand.</p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    # Icon for model or processing
    col1.image("model_icon.png", width=50)
    col1.button("Learn More")

    # Icon for user feedback
    col2.image("feedback_icon.png", width=50)
    col2.button("Provide Feedback")

    # Icon for privacy
    col3.image("privacy_icon.png", width=50)
    col3.button("Privacy Information")

    uploaded_file = st.file_uploader("Upload a scanned image or document for the extraction:", type=["jpg", "png"])

    if uploaded_file is not None:

        # Prepare image data for the API call
        image_data = BytesIO(uploaded_file.read())
        uploaded_image = Image.open(uploaded_file)
        st.image(uploaded_image, caption="Uploaded Image/Document", use_column_width=True)

        if st.button("Process this Image"):
            with st.spinner(text="In process..."):

                # Make API call
                files = {"file": ("image.jpg", image_data, "image/jpeg")}
                response = requests.post("http://127.0.0.1:8000/submit-doc", files=files)

                # Simulate processing time
                time.sleep(2)

                # Process the API response
                if response.status_code == 200:
                    processed_data = response.json()
                    st.session_state.processed_data = processed_data
                    st.success("API call successful!")
                    show_results(processed_data=processed_data, uploaded_image=uploaded_image)
                
                else:
                    st.error(f"API call failed with status code {response.status_code}")


if __name__ == "__main__":
    main()
