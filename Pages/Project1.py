import streamlit as st
import pandas as pd
import numpy as np
  # Декоратор для кэширования

class Project1:
    def __init__(self):
        pass
    def app(self):
        st.title('Creation of DataFrame')

        def load_data(file):
            if file is not None:
                data = pd.read_csv(file)
                return data
            return None

        upload = st.file_uploader("choose csv file")
        if upload is not None:
            df = load_data(upload)
            st.dataframe(df, height=400, width=600)
        else:
            st.warning("Please upload a CSV file")


        st.markdown("""<style> 
                    main {
                        background-color: green !important;
                    }
                    h1 {
                    color: green;
                    font-size:18px;
                    text-align:center;
                    }
                    </style>""", unsafe_allow_html=True)






