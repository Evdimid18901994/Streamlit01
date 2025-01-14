import streamlit as st
from Pages import Home, Project1, Project2, Project3
from streamlit_navigation_bar import st_navbar
import os
from PIL import Image
import pandas as pd
import numpy as np
import cv2

# Attempt to load the image correctly
try:
    image = Image.open('img/barca.png')
except FileNotFoundError:
    st.error("Image not found. Please check the image path.")
    image = None  # Fallback if image is not found

if image:
    st.set_page_config(initial_sidebar_state="collapsed", page_icon=image)
else:
    st.set_page_config(initial_sidebar_state="collapsed")

# Google Analytics Script
google_analytics_script = """
<script async src="https://www.googletagmanager.com/gtag/js?id=G-1GNCCCBG59"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-1GNCCCBG59');
</script>
"""

# Inject the Google Analytics script into the page
st.markdown(google_analytics_script, unsafe_allow_html=True)

logo_path = os.path.join(os.path.dirname(__file__), "img", "barca.svg")
pages = [" ",'Home','Project1', 'Project2', 'Project3']

styles = {
    "nav": {
        "background-color": "royalblue",
        "display": "flex",
        "justify-content": "center"
    },
    "img": {
        "position": "absolute",
        "left": "-20px",
        "font-size": "15px",
        "top": "4px",
        "width": "100px",
        "height": "40px",
    },
    "span": {
        "display": "block",
        "color": "white",
        "padding": "0.2rem 0.725rem",
        "font-size": "14px"
    },

    "active": {
        "background-color": "white",
        "color": "black",
        "font-weight": "normal",
        "padding": "14px",
    }
}

options = {
    "show_menu": False,
    "show_sidebar": True,
}

page = st_navbar(pages,
    styles=styles,
    logo_path=logo_path,
    options=options)

if page == 'Home':
    Home.Home().app()
elif page == "Project1":
    Project1.Project1().app()
elif page == "Project2":
    Project2.Project2().app()
elif page == "Project3":
    Project3.Project3().app()
else:
    Home.Home().app()
