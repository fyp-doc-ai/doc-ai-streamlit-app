import streamlit as st

def show_feedback_form():
    st.title("SRIDOC Feedback Form")

    st.write("We value your feedback! Please take a moment to share your thoughts with us.")

    # Feedback form fields
    feedback = st.text_area("Your Feedback", placeholder="Enter your feedback here...")

    rating = st.selectbox("Rate your experience", options=[1, 2, 3, 4, 5])

    name = st.text_input("Your Name", placeholder="Enter your name")

    email = st.text_input("Your Email", placeholder="Enter your email address")

    # Submit button
    if st.button("Submit Feedback"):
        submit_feedback(feedback, rating, name, email)

def submit_feedback(feedback, rating, name, email):
    # Add your logic to handle the submitted feedback (e.g., store it in a database)
    st.success("Thank you for your feedback!")

if __name__ == "__main__":
    show_feedback_form()
