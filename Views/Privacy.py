import streamlit as st

def show_privacy_information():
    # Privacy Information...
    st.title("Privacy Information")

    st.write("""
    At SRIDOC, we prioritize your privacy and are dedicated to ensuring the security of your data. Our comprehensive privacy guidelines are designed to provide clarity, transparency, and user control. Below, we delve into the details of our privacy practices across various facets:

    **1. Data Collection and Usage:**
    - We prioritize collecting the least amount of user data necessary for a smooth application experience.
    - Personal information, such as names and email addresses, is acquired only with explicit consent from users.
    - The collected data serves the sole purpose of providing services and continual improvement.
    - User data is not shared, sold, or leased to third parties.

    **2. Security Measures:**
    - Our security protocols adhere to industry standards, implementing robust measures to safeguard against unauthorized access, disclosure, and data alterations.
    - We maintain a state-of-the-art infrastructure, routinely updated to stay ahead of emerging security threats.
    - Regular security audits are conducted to ensure the highest level of protection for user data.

    **3. Data Encryption:**
    - All data transmitted between user devices and our servers undergoes encryption using secure protocols.
    - This meticulous encryption process ensures the highest level of confidentiality during data transfer.
    - We use industry-approved encryption algorithms to provide robust protection for your data.

    **4. User Authentication:**
    - Access to user accounts and data is tightly controlled through advanced user authentication mechanisms.
    - Secure login processes are implemented to verify user identities, providing protection against any unauthorized access attempts.
    - Multi-factor authentication options are available to enhance user account security.

    **5. Third-Party Integrations:**
    - We may use third-party services for specific functionalities within our application.
    - These services adhere to strict privacy and security standards and are thoroughly vetted before integration.

    **6. Data Ownership:**
    - Users own their data. We do not claim ownership of any user-generated content within the application.
    - Users have the right to access, correct, or delete their data at any time.

    **7. Data Retention:**
    - User data is retained only for as long as it is necessary to fulfill the purposes for which it was collected.
    - Once the data is no longer needed, it is securely deleted from our systems.

    **8. Anonymous Analytics:**
    - We may collect anonymized usage data for analytics purposes to improve user experience.
    - This data does not contain personally identifiable information.

    **9. Updates and Communication:**
    - Users may receive occasional updates or important information related to our services.
    - Users have the option to opt-out of non-essential communications.

    **10. Compliance with Laws:**
    - SRIDOC diligently adheres to all applicable data protection laws and regulations.
    - Our privacy practices align with global standards, including the General Data Protection Regulation (GDPR).

    **11. Continuous Improvement:**
    - We are committed to continually improving our privacy and security practices.
    - Regular reviews and updates to policies are conducted to adapt to evolving privacy challenges and technological advancements.

    For any questions or concerns about your privacy and data security, our dedicated team is available at privacy@sridoc.com.
    We deeply appreciate the trust you place in SRIDOC and remain steadfast in our commitment to ensuring the utmost privacy and security of your data.
    """)




if __name__ == "__main__":
    show_privacy_information()
