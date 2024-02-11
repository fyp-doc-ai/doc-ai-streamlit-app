import streamlit as st

def show_documentation():

    # Introduction
    st.title("1. Getting Started")

    st.write("""
    Welcome to the SRIDOC documentation, your comprehensive guide to mastering the functionalities and capabilities of our cutting-edge document digitization application. SRIDOC is designed to streamline the process of digitizing both handwritten and printed documents in the Sinhala language, offering state-of-the-art models for optimal results. Developed with privacy and efficiency in mind, SRIDOC provides a secure and user-friendly experience for individuals and organizations seeking advanced solutions for document management and digitization.
    """)

    # Installation
    st.title("2. Installation")

    st.write("""
    Getting started with SRIDOC is a straightforward process. Follow these simple steps to install the application on your device and begin your journey towards efficient document digitization. Download SRIDOC from our official website, ensuring you select the version compatible with your operating system. Follow the step-by-step installation instructions provided for your specific platform (Windows, macOS, or Linux). During the installation process, you have the opportunity to configure your preferences and settings, customizing the application based on your unique requirements. Once installed, launch SRIDOC, and you're ready to digitize your documents with ease.
    """)

    # Tutorials
    st.title("3. Tutorials")

    # Tutorial 1: Running the Application
    st.write("""
    **1. Running the Application:**
    - To run the application locally on your machine, follow these steps:
        - Clone the repository from [GitHub](https://github.com/your-username/your-repository).
        - Navigate to the project directory in your terminal.
        - Install the required dependencies by running: `pip install -r requirements.txt`.
        - Run the application using: `streamlit run your_app.py`.
        - Access the application in your web browser at `http://localhost:8501`.

    """)



    # Tutorial 2: Downloading the Mobile Application
    st.write("""
    **2. Downloading the Mobile Application:**
    - Visit the [Download Section](https://your-app-website.com/download) on our web application.
    - Choose the appropriate version for your mobile device (Android or iOS).
    - Follow the on-screen instructions for installation.
    - Once installed, open the mobile application and create an account to start document digitization.
    - Note: The application does not store documents in any server-side database; they remain in your mobile's local storage.

    """)


    st.write("""
    **3. Additional Tutorials:**
    - For more detailed instructions and examples, refer to our [README](https://github.com/your-username/your-repository/blob/main/README.md) on GitHub.
    - The README provides comprehensive documentation, including:
        - Setup instructions.
        - In-depth explanations of features.
        - Troubleshooting tips.
        - Contribution guidelines for developers.

    """)
    
    st.title("4. Research Papers")

    # Placeholder for Research Paper 1
    st.write("""
    **1. Title: Enhancing Handwritten Text Recognition in Multilingual Documents**
    - Authors: John Doe, Jane Smith
    - Conference/Journal: Proceedings of the International Conference on Document Analysis and Recognition (ICDAR)
    - [Link to Paper Placeholder 1]()
    """)

    # Placeholder for Research Paper 2
    st.write("""
    **2. Title: A Comparative Analysis of OCR Models for Document Understanding**
    - Authors: Alice Johnson, Robert Brown
    - Conference/Journal: Journal of Artificial Intelligence Research
    - [Link to Paper Placeholder 2]()
    """)

    # Placeholder for Survey Paper
    st.write("""
    **3. Title: Survey on Recent Advances in Document Understanding Technologies**
    - Authors: Emily Taylor, Michael Clark
    - Journal: ACM Computing Surveys
    - [Link to Survey Paper Placeholder]()
    """)


    st.write("""
# 5. Methodology

## 5.1. Creating Datasets

### 5.1.1. Data Collection
Our methodology commenced with an extensive survey of government and private organization websites, where we systematically gathered a diverse array of application forms representative of various administrative processes and sectors.

Subsequently, from this extensive collection of forms, we judiciously handpicked a subset to ensure the dataset's breadth and representativeness. This selective approach aimed to encompass a wide spectrum of form types, ranging from educational enrollment forms to healthcare registration documents, thereby capturing the diversity inherent in administrative documentation.

Having curated our selection of forms, our attention turned to the crucial task of data generation. To simulate real-world scenarios and ensure the authenticity of our dataset, we proceeded to manually fill out the selected forms using handwritten text. This process not only incorporated the dataset with genuine handwriting variations but also enabled us to replicate the complexities and idiosyncrasies commonly encountered in handwritten documentation.

Once the forms were filled out, we employed mobile phone cameras to capture high-resolution scans of the completed documents. This approach afforded us the flexibility and convenience of capturing images in diverse environments, ensuring the dataset's robustness and adaptability to real-world conditions.

With our scanned images in hand, the next phase of our methodology entailed manual annotation, a pivotal step in the dataset creation process. Drawing inspiration from established annotation frameworks such as the Form Understanding in Noisy Scanned Documents (FUNSD) dataset [9], we adhered to a standardized annotation format to systematically label and annotate the scanned images. This careful annotation process involved labeling key elements within the forms, thereby facilitating the training and evaluation of Sinhala form understanding models.

In essence, our methodology embodies a systematic and comprehensive approach to dataset creation, meticulously crafted to ensure the authenticity, diversity, and utility of the compiled dataset for advancing research and innovation in Sinhala form understanding.

### 5.1.2. Form Data Annotation
In our annotation process, we employed a specialized tool called the Banksy Annotation Tool [32], which was originally developed for annotation tasks. However, we modified this tool significantly to better suit our needs and align with the format used in the FUNSD dataset, a widely recognized standard in the field.

Our adaptation of the Banksy Annotation Tool allowed us to represent forms as a structured list of interconnected entities, following the format established by the FUNSD dataset [9]. This format enables clear identification and labeling of various elements within the forms, such as questions answers, and headers.

Throughout the modification process, we also incorporated additional functionalities to enhance the tool's usability and efficiency. These improvements include the ability to save and load intermediate results, error correction capabilities, etc. These improvements aim to streamline the annotation process, making it more intuitive and user-friendly for annotators.

The updated version of the Banksy Annotation Tool, now tailored to our specific requirements and equipped with enhanced features, is readily accessible to users through the [Banksy Annotation Tool repository on GitHub](https://github.com/fyp-doc-ai/Banksy-annotation-tool). This centralized platform provides a convenient and collaborative environment for annotators to efficiently annotate scanned form images according to the standardized FUNSD format.

### 5.1.3. OCR Data Collection
In our effort to create data for handwritten Optical Character Recognition (OCR), we employed two distinct approaches. The first method involved generating a synthetic handwritten dataset utilizing specialized handwritten fonts. This approach enabled us to fabricate a dataset that mimics certain attributes of genuine handwritten text. Across this method, we successfully generated a total of 10,000 images. To illustrate, a selection of examples from this synthetic dataset is showcased in Figure 3.

To delve further into this process, we employed handwritten fonts designed to replicate the appearance of human handwriting. By utilizing these fonts, we were able to simulate the variability and imperfections typically associated with handwritten characters, such as irregular shapes and slight variations in stroke thickness.

Each generated image within this synthetic dataset encapsulated these characteristics, contributing to the creation of a diverse and representative collection of handwritten text samples. Through this approach, we sought to provide a robust and varied dataset for training and evaluating handwritten OCR systems, thereby enhancing their accuracy and adaptability to real-world handwritten text recognition tasks.

In addition to generating synthetic handwritten data, we pursued another method to procure handwritten samples for Optical Character Recognition (OCR) applications. This method involved extracting handwritten portions from completed forms. To initiate this process, we meticulously cropped scanned images using bounding boxes delineated in the annotations. These bounding boxes acted as guides, indicating the areas within the scanned images containing handwritten text.

Following the extraction of handwritten segments, we embarked on a manual inspection phase to ensure the quality and relevance of the extracted images. During this inspection, we carefully examined each cropped image to verify its content. Specifically, we focused on identifying images containing exclusively handwritten characters, as opposed to those comprising solely numerical digits or English letters.

Upon careful examination, we curated a dataset comprising 457 images deemed suitable for handwritten OCR applications. These images encompass a variety of handwritten styles and variations, capturing the diversity inherent in real-world handwritten text. To provide a glimpse into this dataset, several examples of the extracted handwritten samples are shown in Figure 4.

This method of data acquisition not only enriches our dataset with authentic handwritten samples but also reflects the practical challenges encountered in OCR tasks, particularly when dealing with handwritten content from filled forms. By carefully curating this dataset, we aim to furnish OCR systems with robust training data, thereby enhancing their ability to accurately recognize and interpret handwritten text in diverse real-world scenarios.

## 5.2. Implementation of AI Models

### 5.2.1. OCR
AI models serve as the backbone of the proposed framework performing the document understanding tasks. The AI model workflow used in the framework is shown in the below figure.

We experimented with multiple methodologies and evaluated their performance on Sinhala Handwritten text recognition. We experimented with the TrOCR, the current state-of-the-art model for English handwriting recognition. We modified the existing TrOCR model by integrating a Sinhala monolingual language model [17] as its decoder to support Sinhala text recognition. Since this needs training the model from scratch we used synthetic handwriting that was generated using handwritten fonts. We trained the model using a dataset of 8000 images and evaluated its performance on 2000 images. The results obtained are presented in the Results section.

Furthermore, we experimented with finetuning the Tesseract [34] OCR tool using both synthetic and handwritten text. Since Tesseract already supports the Sinhala language we started from the existing trained model and fine-tuned it first with synthetic data and then with actual handwritten text data described in the Datasets section. The results of these fine-tuning experiments are described in the Results section.

Moreover, we experimented with a YOLO [38] object detection model to identify individual characters present in a given text. Specifically, we selected a pre-trained YOLOv8 model and fine-tuned it on synthetically generated handwritten text. The number of output classes is high due to the large number of characters available in the Sinhala language as a result of character modifiers.

CDistNet is a scene text recognition model that can be used to extract text from natural scenes. We experimented with fine-tuning the CDistNet to recognize Sinhala text from textline images but the experiments revealed that CDistNet cannot be utilized for the Sinhala language because of the character embeddings used in the semantic branch does not support Sinhala characters. It can be used by mapping each Sinhala character to an English character but the limited number of available English characters is an Issue. Another approach to try is to divide Sinhala text into three zones as described by Dharmapala et al. [22] and train three different CDistNet models for each zone. This process requires manual annotation of the text.

### 5.2.2. Document Understanding
Document understanding is a field that involves automating the process of interpreting and extracting useful information from different kinds of documents. This technology relies on both the text and layout of documents to understand, organize, and extract structured data from them.

In essence, document understanding tackles two primary tasks:

1. **Semantic Entity Recognition (SER):** This task involves classifying different elements within documents, such as questions, answers, and headers. By recognizing these semantic entities, document understanding systems can effectively categorize and organize the information contained within documents. For example, in a survey form, the system would identify questions posed to respondents, the corresponding answers provided, and any section headers guiding the flow of information. In the context of Sinhala Form Understanding, SER involves classifying the tokens extracted using OCR into one of four classes; QUESTION, ANSWER, HEADER, and OTHER.

2. **Relationship Extraction (RE):** In this task, document understanding systems focus on identifying the connections or relationships between different entities within the document. For instance, in an application form identifying the related answers and questions falls under this task. By discerning these relationships, document understanding systems can derive deeper insights from the content and facilitate more nuanced analysis. RE involves identifying the relationships between questions and answers present in the document image. In the inference stage, we first classify tokens using the SER model and then feed identified questions and answers into the RE model.

Within our framework, we implement the use of two distinct models to handle semantic entity recognition (SER) and relation extraction (RE) tasks. These models serve as essential components in our approach to document understanding.

In our approach, we began by carefully choosing an established document understanding model that doesn't rely on any specific language. We selected an existing language-independent document understanding model. Then we integrated the selected model with an existing language model that supports Sinhala.

The backbone of both our models is the LiLT architecture. This architecture is pivotal because it provides language independence, meaning it allows us to leverage pre-existing knowledge on layout information, enabling efficient handling of Sinhala documents without the need to train models from scratch [2].

By leveraging the LiLT architecture, our integrated models can efficiently interpret and extract information from Sinhala documents. This streamlined approach ensures that our framework is well-equipped to handle the complexities of Sinhala language documents, enabling users to work with such documents seamlessly without the burden of training models from scratch, thereby saving time and resources.

In our methodology, we opted to utilize a pre-trained model called XLM-R [16] as the text encoder for our models, rather than relying solely on a Sinhala-specific monolingual model like SinBERT [17]. This decision was made to cater to the multilingual nature of Sinhala documents, which often incorporate text in multiple languages, such as Sinhala, Tamil, and English.

XLM-R is a pre-trained model that has been trained on a diverse range of languages, allowing it to understand and process text from various linguistic backgrounds effectively. By leveraging XLM-R as our text encoder, we ensure that our models can handle the diverse linguistic compositions often found in Sinhala documents.

This approach offers several advantages. Firstly, it enables our models to comprehend and analyze documents that contain text in multiple languages, such as tri-lingual (Sinhala, Tamil, English) or bi-lingual (Sinhala, Tamil or Sinhala, English) formats. Secondly, by utilizing a pre-trained model like XLM-R, we can capitalize on the wealth of knowledge and linguistic patterns encoded within the model, thereby enhancing the overall performance and accuracy of our document understanding framework.

On top of the LiLT model described above, we use two different classification heads. RE model has a classification head on top of the LiLT model, that uses the biaffine attention operator [18] to predict whether there is a relation between each pair of input tokens. In summary, this is a binary classification task that determines the existence of a relation between two tokens. SER model uses a feed forward meural network as its classification head. Details about these classifiers are shown below.

**SER Head:**
- Dropout(p=0.1, inplace=False)
- Linear(in_features=768, out_features=7, bias=True)

**RE Head:**
- Dropout(p=0.1, inplace=False)
- Linear(in_features=768, out_features=7, bias=True)
- REDecoder:
  - Entity Embedding: Embedding(3, 768, scale_grad_by_freq=True)
  - Feedforward Head:
    - Linear(in_features=1536, out_features=768, bias=True)
    - ReLU()
    - Dropout(p=0.1, inplace=False)
    - Linear(in_features=768, out_features=384, bias=True)
    - ReLU()
    - Dropout(p=0.1, inplace=False)
  - Feedforward Tail:
    - Linear(in_features=1536, out_features=768, bias=True)
    - ReLU()
    - Dropout(p=0.1, inplace=False)
    - Linear(in_features=768, out_features=384, bias=True)
    - ReLU()
    - Dropout(p=0.1, inplace=False)
  - Relation Classifier: Biaffine Attention
    - Bilinear(in1_features=384, in2_features=384, out_features=2, bias=False)
    - Linear(in_features=768, out_features=2, bias=True)

An overview of our framework is shown in Figure 12. We have designed the framework to handle both handwritten and printed text recognition tasks separately. To accomplish this, we employ two separate models, each specializing in a specific type of text recognition.

First, we extract the handwritten parts of the scanned document image using a YOLO model [42]. This model has been trained on a dataset specifically curated for handwritten text [41] detection. Its primary function is to identify and extract the handwritten portions from the document accurately. Once these handwritten sections are isolated, they are then passed on to a dedicated OCR engine trained explicitly for handwritten text recognition. This specialized OCR engine is optimized to recognize and convert handwritten characters into digital text effectively.

On the other hand, for printed text recognition, we've opted to utilize Google Cloud Vision. This decision is informed by the performance metrics outlined in Table 4, which suggest that Google Cloud Vision performs exceptionally well in recognizing printed text. Given its high accuracy and reliability in this regard, we believe it's unnecessary to use the same model employed for handwritten text recognition to handle printed text as well.

By leveraging this dual-model approach, our framework can effectively handle both handwritten and printed text recognition tasks with optimized performance and accuracy. This ensures that regardless of the type of text present in the document, our framework is equipped to accurately extract and interpret the textual content, thereby facilitating efficient document understanding and processing.

## 5.3. Web and Mobile Apps
We designed both web and mobile applications as in Fig 13 to get an image/pdf (filled form) from the user and follow some series of steps to finally get an output. In these steps, the image gets preprocessed (to increase the readability and visibility), sent to the model server, displayed the response from the server, and finally save the result with the user feedbacks locally. The OCR, SER and Layout Analysis which will happen in the model server is explained under Implementation of AI Models (5.2).

We developed the mobile application using React-Native, Node.js, and MongoDB database with the same architecture as previously stated. It includes additional features to save, reload, alter the outputs as well as user management. We designed the web application to follow the same architecture with additional pages like documentation, model performance checking dashboard, data analysis dashboard, etc. Mobile applications can be downloaded as an APK from the web application's download directory. Streamlit is used to develop and deploy the web application. Each platform application’s user interface and features will be discussed here on.

### 5.3.1. Mobile Application
In the mobile application, users can create an account to initiate document digitization. They have the option to store their scanned documents in their mobile's local storage, and it's important to note that the application does not store these documents in any server-side database.

During the document digitization process, users can either take a picture or select one from their gallery. They can further edit the image by cropping, rotating, or blurring it. Following this, users need to provide a title for the document before proceeding to digitize it. Once the digitization process is complete, users have the flexibility to delete or add a question and answer pair, or they can choose to delete the entire document as well.

#### 5.3.1.1 Technical Stack
The application is built using React Native, a popular framework for cross-platform mobile development. React Native allows for the creation of native-like mobile applications using JavaScript and React. Its component-based architecture facilitates code reusability and efficient development.

#### 5.3.1.2 Backend Development
Node.js serves as the backend technology for handling user activities, excluding the OCR (Optical Character Recognition) process. Node.js is well-suited for building scalable and high-performance server-side applications. It provides a non-blocking, event-driven architecture, making it ideal for handling concurrent requests from mobile clients.

#### 5.3.1.3 User Interaction and Feedback
The application features a "Contact Us" page through which users can report bugs, provide feedback, or share their thoughts. When a user submits feedback or reports a bug, the backend system triggers an email notification to the administrator of the mobile application. This ensures that user concerns are promptly addressed, enhancing overall user satisfaction and application quality.

#### 5.3.1.4 State Management
Redux Toolkit is utilized for state management within the application. Redux Toolkit simplifies the process of managing application state by providing utilities for creating actions, reducers, and stores. By storing user documents in the local storage of the mobile device using Redux Toolkit, the application ensures efficient access to data and seamless offline functionality. Asynchronous access to the local storage enables smooth interaction with stored documents even when the device is offline.

#### 5.3.1.5 Camera and Image Editing
The application leverages Expo Camera for capturing images within the document digitization process. Expo Camera provides a versatile and user-friendly interface for interacting with the device's camera functionalities, enhancing the overall user experience during image capture.

Additionally, the image editing features, such as cropping, rotating, and blurring, are implemented using the Expo Image Manipulator. This tool streamlines the image editing process, allowing users to refine their captured images conveniently.

### 5.3.2. Web Application
The web application mirrors the functionality of its mobile counterpart, offering users a consistent experience across platforms. Users can create accounts, digitize documents, and manage their documents seamlessly. The web application, developed using Streamlit, provides an intuitive and user-friendly interface for efficient document digitization.

#### 5.3.2.1 Technical Stack
Streamlit serves as the primary technology for web application development. Streamlit is a powerful and user-friendly framework for creating web applications with minimal effort. Its simplicity and ease of use make it an ideal choice for rapidly prototyping and deploying data-centric applications.

#### 5.3.2.2 Deployment
The web application is deployed using Streamlit Sharing, Streamlit's official platform for hosting and sharing Streamlit applications. Streamlit Sharing simplifies the deployment process, allowing developers to share their applications with a global audience seamlessly.

#### 5.3.2.3 Model Performance Dashboard
The web application includes a dedicated dashboard for users to monitor the performance of the underlying models. This dashboard provides insights into the accuracy and efficiency of the OCR and document understanding models. Users can assess the performance metrics, including precision, recall, and F1 score, to gauge the reliability of the models in handling different types of documents.

#### 5.3.2.4 Data Analysis Dashboard
For users seeking deeper insights into the digitized documents, the web application offers a data analysis dashboard. This feature allows users to explore and visualize trends, patterns, and key metrics extracted from the digitized documents. The data analysis dashboard enhances the overall utility of the application by providing users with valuable insights derived from their digitized documents.

## 5.4. Model Server Implementation
The model server plays a central role in the document digitization process, serving as the backend responsible for executing the OCR, SER, and Layout Analysis tasks. The server is designed to handle image or PDF inputs, process them through the underlying models, and return structured outputs to the user interface.

### 5.4.1. Technical Stack
The model server is implemented using Flask, a lightweight and efficient web framework for Python. Flask facilitates the rapid development of web applications and microservices, making it well-suited for our model server requirements.

#### 5.4.2. OCR, SER, and Layout Analysis
The model server orchestrates the execution of OCR, SER, and Layout Analysis tasks. For OCR, we employ Tesseract for printed text recognition and a dedicated handwritten OCR model for handwritten text recognition. The SER model is responsible for semantic entity recognition, categorizing extracted tokens into predefined classes such as QUESTION, ANSWER, HEADER, and OTHER. Layout Analysis involves identifying the structure and layout of the document, distinguishing between different sections and elements.

#### 5.4.3. Model Interaction
Upon receiving image or PDF inputs from the web and mobile applications, the model server initiates the OCR process, extracting both printed and handwritten text from the document. The extracted text is then passed through the SER model to identify semantic entities and classify them into relevant categories. Simultaneously, the Layout Analysis task is performed to discern the structure of the document.

The interaction with the OCR, SER, and Layout Analysis models is seamlessly orchestrated within the model server, ensuring a coherent and efficient document digitization workflow.

## 5.5. Evaluation
To assess the performance of our proposed framework, we conducted comprehensive evaluations across different aspects of the document digitization process. The evaluation focused on OCR accuracy, SER efficiency, and the overall document understanding capability of the framework.

### 5.5.1. OCR Evaluation
We evaluated the performance of the OCR component by assessing its accuracy in recognizing both printed and handwritten text. The evaluation dataset comprised a diverse collection of scanned document images, featuring a variety of fonts, styles, and content.

For printed text recognition, we employed the Tesseract OCR tool, which is renowned for its accuracy in extracting text from images. To evaluate the OCR accuracy, we utilized precision, recall, and F1 score metrics, comparing the tool's output with ground truth annotations.

Additionally, we conducted a separate evaluation for handwritten text recognition using the modified TrOCR model. The evaluation criteria mirrored those used for printed text, with a focus on precision, recall, and F1 score metrics.

### 5.5.2. SER Evaluation
The evaluation of the Semantic Entity Recognition (SER) component centered on assessing its ability to accurately classify extracted tokens into predefined classes. The dataset for SER evaluation comprised annotated document images, with ground truth labels for each token.

To quantify the performance of the SER model, we employed precision, recall, and F1 score metrics. These metrics provided a comprehensive analysis of the model's proficiency in recognizing and categorizing semantic entities within document images.

### 5.5.3. Document Understanding Evaluation
The overarching evaluation of document understanding encompassed the combined performance of OCR, SER, and Layout Analysis components. This evaluation aimed to gauge the framework's ability to accurately interpret and extract meaningful information from diverse documents.

For this evaluation, we utilized a dataset comprising a representative selection of document images, spanning various domains and administrative processes. The evaluation criteria included precision, recall, and F1 score metrics, offering insights into the overall effectiveness of the document understanding framework.

## 5.6. Model Performance Analysis
The performance of the underlying AI models, including OCR, SER, and Layout Analysis, is critically analyzed to provide users with valuable insights into the capabilities and limitations of the document digitization framework.

### 5.6.1. OCR Performance Metrics
To comprehensively assess the performance of the OCR component, we present a detailed analysis of precision, recall, and F1 score metrics. These metrics offer quantitative insights into the accuracy of printed and handwritten text recognition.

### 5.6.2. SER Performance Metrics
The Semantic Entity Recognition (SER) component's performance is meticulously analyzed using precision, recall, and F1 score metrics. This analysis sheds light on the model's proficiency in classifying tokens into predefined categories.

### 5.6.3. Layout Analysis Performance
The Layout Analysis component's effectiveness is evaluated based on its ability to accurately identify and distinguish between different sections and elements within document images. Precision, recall, and F1 score metrics are employed to quantify the performance of Layout Analysis.

## 5.7. User Feedback and Iterative Improvement
User feedback plays a pivotal role in refining and optimizing the document digitization framework. Through user interactions with the web and mobile applications, we collect valuable feedback regarding the system's performance, usability, and overall user experience.

### 5.7.1. User Feedback Mechanism
The web and mobile applications incorporate a user-friendly feedback mechanism, allowing users to provide insights, report issues, or suggest improvements. This mechanism includes a "Contact Us" feature, enabling users to submit feedback seamlessly.

### 5.7.2. Feedback Analysis and Iterative Improvement
User feedback is systematically collected, analyzed, and utilized to drive iterative improvements in the document digitization framework. The feedback analysis process involves categorizing user inputs, identifying recurring themes or issues, and prioritizing enhancement areas.

The iterative improvement cycle involves revisiting the AI models, system architecture, and user interface based on the feedback received. This iterative approach ensures that the document digitization framework evolves to meet user expectations, address emerging challenges, and adapt to evolving requirements.

    """)



if __name__ == "__main__":
    show_documentation()
