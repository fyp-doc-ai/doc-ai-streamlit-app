import streamlit as st

# Function to display a loading spinner
def loading_spinner(session_state):

    if session_state:
        st.write("<div style='display: flex; justify-content: center;'><div class='loader'></div></div>", unsafe_allow_html=True)

        st.write(
            """
            <style>
            .loader {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #3498db;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            animation: spin 1s linear infinite;
            }

            @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.empty()