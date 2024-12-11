import streamlit as st
from Pages import Home, Project1, Project2, Project3
from streamlit_navigation_bar import st_navbar as navbar
from PIL import Image
import pandas as pd
import numpy as np


image = Image.open('img/db.png')
st.set_page_config(initial_sidebar_state="collapsed", page_icon=image)

pages = ['Home','Project1', 'Project2', 'Project3']
styles = {
    "nav":{
        "background-color": "yellow",
        "display": "flex",
        "justify-content": "center",
    },
    "img": {
        "position": "absolute",
        "left": "-20px",
        "font-size": "15px",
        "top": "4px",
        "width": "100px",
        "height": "40px",
    },
    "div": {
    "max-width": "32rem",
     },
    "span": {
        "display": "block",
        "color": "rgb(49, 51, 63)",
        "padding": "0.4375rem 0.625rem",
        "font-size": "14px",
    },
    "active": {
        "background-color": "white",
        "color": "black",
        "font-weight": "normal",
        "padding": "14px",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    }

}

page = navbar(pages, styles=styles)

if page == 'Home':
    Home.Home().app()
elif page == "Project1":
    Project1.Project1().app()
elif page == "Project2":
    Project2.Project2().app()
elif page =="Project3":
    Project3.Project3().app()
else:
    Home.Home().App()
st.title('hi')
