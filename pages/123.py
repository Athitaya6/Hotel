import streamlit as st 
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        option=["Home", "Thoery", "Prediction"],
    )
