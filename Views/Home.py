import streamlit as st
import time
import requests
from PIL import Image
from io import BytesIO
from utils.image_processing import process_image
from utils.results_generator import show_results
from utils.spinner import loading_spinner
from streamlit_option_menu import option_menu


def view_home():

    st.markdown("<p style='text-align: center; color: grey; font-size: small; font-style: italic;'> Introducing our cutting-edge mobile application, equipped with the latest models for digitizing and extracting question-answer pairs from forms in both English and Sinhala languages. Our advanced framework ensures optimal outcomes, leveraging state-of-the-art models to deliver the highest accuracy.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: grey; font-size: small; font-style: italic;'> Additionally, the application provides users with the ability to offer valuable feedback, contributing to continuous improvement. We prioritize the full privacy of your data through innovative techniques like federated learning, ensuring a secure and personalized experience. Welcome to a new era of form digitization and extraction, where efficiency meets privacy in the palm of your hand.</p>", unsafe_allow_html=True)

    row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
    with row0_1:
        st.title('Document Digitizer')

    uploaded_file = st.file_uploader("Upload a scanned image or document for the extraction:", type=["jpg", "png"])
    st.text('Please note that this desktop version does not have an option to capture an image')

    if uploaded_file is not None:

        # Prepare image data for the API call
        image_data = BytesIO(uploaded_file.read())
        uploaded_image = Image.open(uploaded_file)
        st.image(uploaded_image, caption="Uploaded Image/Document", use_column_width=True)

        if st.button("Process this Image"):
            with st.spinner(text="In process..."):

                # Make API call
                files = {"file": ("image.jpg", image_data, "image/jpeg")}
                response = requests.post("https://kavg-sri-doc.hf.space", files=files)

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
    view_home()
