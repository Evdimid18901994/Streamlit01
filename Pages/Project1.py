import streamlit as st
import pandas as pd
import numpy as np
  # Декоратор для кэширования

class Project1:
    def __init__(self):
        pass
    def app(self):


        st.write('Project1')
        def load_data():
            # Имитация длительной загрузки данных
            data = pd.DataFrame({'smth': [11, 28, np.nan, 48, 59, 101, 58, 32]})
            return data

        df = load_data()
        st.dataframe(df)


