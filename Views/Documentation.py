import streamlit as st

def show_documentation():
    st.title("SRIDOC Documentation")

    # Introduction
    st.header("Introduction")

    st.write("""
    Welcome to the SRIDOC documentation, your comprehensive guide to mastering the functionalities and capabilities of our cutting-edge document digitization application. SRIDOC is designed to streamline the process of digitizing both handwritten and printed documents in the Sinhala language, offering state-of-the-art models for optimal results. Developed with privacy and efficiency in mind, SRIDOC provides a secure and user-friendly experience for individuals and organizations seeking advanced solutions for document management and digitization.
    """)

    # Installation
    st.header("Installation")

    st.write("""
    Getting started with SRIDOC is a straightforward process. Follow these simple steps to install the application on your device and begin your journey towards efficient document digitization. Download SRIDOC from our official website, ensuring you select the version compatible with your operating system. Follow the step-by-step installation instructions provided for your specific platform (Windows, macOS, or Linux). During the installation process, you have the opportunity to configure your preferences and settings, customizing the application based on your unique requirements. Once installed, launch SRIDOC, and you're ready to digitize your documents with ease.
    """)

    # Tutorials
    st.header("Tutorials")

    st.write("""
    Dive deep into SRIDOC's capabilities with our step-by-step tutorials. Master the art of digitizing handwritten documents and extracting valuable information effortlessly. Our tutorials cover a range of topics to ensure you make the most out of SRIDOC's advanced features. Learn the fundamental steps to digitize handwritten documents effectively using SRIDOC. This tutorial provides a hands-on approach, guiding you through the entire process from document scanning to the generation of digital copies. Understand the nuances of information extraction with SRIDOC's advanced models. This tutorial explores the efficient extraction of question-answer pairs from forms, showcasing the powerful features available for form digitization.
    """)

    # Research Papers
    st.header("Research Papers")

    st.write("""
    SRIDOC is built on cutting-edge research and state-of-the-art models. Explore the research papers below to gain insights into the methodologies and innovations that power SRIDOC's document digitization capabilities. Delve into the first research paper, providing a concise overview of its objectives, methodologies, and key findings. This paper explores a specific topic, demonstrating how it contributes to the advancements in document digitization technology. Explore the second research paper, offering a detailed examination of its core concepts, methodologies, and implications. This paper explores another specific topic, showcasing how it enhances the overall functionality and accuracy of SRIDOC.
    """)

if __name__ == "__main__":
    show_documentation()
