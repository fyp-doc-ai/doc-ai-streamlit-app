import streamlit as st

def show_download_page():
    st.title("Download SRIDOC Mobile App")

    # Some information about the download page
    st.markdown("""
    Welcome to the SRIDOC download page! Here, you can find the latest versions of our application.
    Follow the guide below to download and install SRIDOC on your device.
    """)

    # Guide to download
    st.header("How to Download and Install SRIDOC")

    st.markdown("""
    1. Choose the version you want to download from the list below.
    2. Click on the APK download icon to initiate the download.
    3. Once downloaded, install the application on your device.
    4. Open SRIDOC and start digitizing your handwritten documents!
    """)

    # List of versions
    st.header("Versions")

    versions = ["1.0.0", "1.1.0", "1.2.0"]  # Add your actual versions
    selected_version = st.selectbox("Select Version", versions)
    
    download_button = st.button(f"Download SRIDOC {selected_version}")

    # Animation
    st.header("SRIDOC in Action")
    st.video("sridoc_animation.mp4", start_time=0)

    # Add more content as needed...

if __name__ == "__main__":
    show_download_page()