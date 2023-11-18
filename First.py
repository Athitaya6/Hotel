import json
import time
import requests

import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
  
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/4d8c2000-072b-467d-873c-9343cd137fa6/6utFz2fXUu.json"
lottie_url_Welcome = "https://lottie.host/290016a6-d650-4a32-85c7-4d77b0a892ca/4rNL8XZeZt.json"
lottie_hello = load_lottieurl(lottie_url_hello)
lottie_Welcome = load_lottieurl(lottie_url_Welcome)


st_lottie(lottie_hello, key="hello")

if st.button("Welcome"):
    with st_lottie_spinner(lottie_url_Welcome, key="Welcome"):
        time.sleep(5)
    st.balloons()
    