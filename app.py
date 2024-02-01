import streamlit as st

st.set_page_config(page_title="SRIDOC", page_icon="Logo.png", layout="wide")


from Views import Dashboard, Home, Data, Documentation, Download, Feedback, Privacy
from streamlit_option_menu import option_menu

row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((3, 1, 2, 1, 3))
with row0_spacer2:
    st.image("Logo.png")
    st.markdown("<h5 style='text-align: center; color: grey;'>Comprehensive Handwritten Document Digitization Solution!</h5>", unsafe_allow_html=True)


selected = option_menu(None, ["Home", "Dashboard", 'Analysis', 'Documentation', 'Download', 'Feedback', 'Privacy'],                        
    icons=['house', 'bar-chart-line-fill', 'activity', 'list-task', 'cloud-download', 'chat-dots', 'shield-lock'],
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
            "container": {"padding": "0!important"},
            "icon": {"color": "orange"}, 
            "nav-link": {"margin":"0px", "--hover-color": "#eee"},
        })



if selected == 'Dashboard':
    Dashboard.show_model_comparison_page()

elif selected == 'Analysis':
    Data.show_data_analysis_page()

elif selected == 'Documentation':
    Documentation.show_documentation()

elif selected == 'Download':
    Download.show_download_page()

elif selected == 'Feedback':
    Feedback.show_feedback_form()

elif selected == 'Privacy':
    Privacy.show_privacy_information()

else:
    Home.view_home()

