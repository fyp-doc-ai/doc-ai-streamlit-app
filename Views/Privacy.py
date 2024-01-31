# PrivacyInformation.py

import streamlit as st

def show_privacy_information():
    st.title("Privacy Information - SRIDOC")

    st.write("""
    At SRIDOC, we are committed to ensuring the privacy and security of your data. This privacy information outlines the measures we take to preserve your privacy and maintain the security of your information. Please read the following carefully to understand how we handle your data.

    **Data Collection and Usage:**
    We collect minimal user data necessary for the functioning of our application. This may include personal information such as name and email, but we do not collect any data without your explicit consent. The information collected is used solely for providing and improving our services.

    **Security Measures:**
    We employ industry-standard security measures to protect your data from unauthorized access, disclosure, alteration, and destruction. Our infrastructure is designed to meet high-security standards, and we regularly update our systems to address emerging security threats.

    **Data Encryption:**
    All data transmitted between your device and our servers is encrypted using secure protocols. This ensures that your information remains confidential and protected during transfer.

    **User Authentication:**
    Access to your account and data is restricted through robust user authentication mechanisms. We implement secure login processes to verify the identity of users and prevent unauthorized access.

    **Third-Party Integrations:**
    We may use third-party services for specific functionalities within our application. These services adhere to strict privacy and security standards. Before integrating any third-party service, we thoroughly vet their practices to ensure alignment with our commitment to user privacy.

    **Data Ownership:**
    You own your data. We do not sell, rent, or lease your personal information to third parties. Your data is used exclusively for the purpose of providing and improving our services. You have the right to access, correct, or delete your data at any time.

    **Data Retention:**
    We retain user data only for as long as it is necessary to fulfill the purposes for which it was collected. Once the data is no longer needed, it is securely deleted from our systems.

    **Anonymous Analytics:**
    We may collect anonymized usage data for analytics purposes. This information helps us understand how users interact with our application, allowing us to enhance user experience. This data does not contain personally identifiable information.

    **Updates and Communication:**
    We may send occasional updates or important information related to our services. You have the option to opt-out of non-essential communications.

    **Compliance with Laws:**
    We comply with all applicable data protection laws and regulations. Our privacy practices are in accordance with global standards, including the General Data Protection Regulation (GDPR).

    **Continuous Improvement:**
    We are committed to continually improving our privacy and security practices. We regularly review and update our policies to adapt to evolving privacy challenges and technological advancements.

    **Contact Us:**
    If you have any questions or concerns regarding your privacy and data security, please contact us at privacy@sridoc.com.

    Thank you for entrusting SRIDOC with your data. We appreciate the trust you place in us and remain dedicated to safeguarding your privacy.
    """)

if __name__ == "__main__":
    show_privacy_information()
