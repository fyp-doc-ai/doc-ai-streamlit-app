import streamlit as st

st.set_page_config(page_title="SRIDOC", page_icon="Logo.png", layout="wide")


from Views import LILT, Home, OCR, Documentation, Download, Feedback, Privacy, History
from streamlit_option_menu import option_menu

row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((3, 1, 2, 1, 3))
with row0_spacer2:
    st.image("Logo.png")
st.markdown("<h5 style='text-align: center; color: grey;'>Comprehensive Handwritten Document Digitization Solution!</h5>", unsafe_allow_html=True)


selected = option_menu(None, ["Home", "LILT", 'OCR', 'Docs', 'APK', 'Feedback', 'Privacy', 'History'],                        
    icons=['house', 'bar-chart-line-fill', 'activity', 'list-task', 'cloud-download', 'chat-dots', 'shield-lock', 'clock-history'],
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
            "container": {"padding": "0!important"},
            "icon": {"color": "orange", "font-size": "12px"}, 
            "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"font-size": "12px"},
        })


if selected == 'LILT':
    LILT.show_LiLT_Results()

elif selected == 'OCR':
    OCR.show_OCR_Results()

elif selected == 'Docs':
    Documentation.show_documentation()

elif selected == 'APK':
    Download.show_download_page()

elif selected == 'Feedback':
    Feedback.show_feedback_form()

elif selected == 'Privacy':
    Privacy.show_privacy_information()

elif selected == 'History':
    History.view_history_results()

else:
    Home.view_home()

