import streamlit as st
import pandas as pd
import numpy as np

class Project1:
    def __int__(self):
        pass
    def app(self):
        st.write('Creation of Dataframe')

        def load_data(file):
            if file is not None:
                data = pd.read_csv(file)
                return data
            return None

        upload = st.file_uploader("Choose your csv file")
        if upload is not None:
            df = load_data(upload)
            st.dataframe(df, height=400, width=600)
        else:
            st.warning("Please upload a CSV file")

        st.markdown("""<style>
            h1 {
                color: green;
                font-size: 18px;
                text-align: center;
            }
        </style>""", unsafe_allow_html=True)