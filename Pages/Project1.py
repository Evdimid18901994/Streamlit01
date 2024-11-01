import streamlit as st
import pandas as pd
import numpy as np
import streamlit_pandas as sp
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

        all_widgets = sp.create_widgets(df)
        res = sp.filter_df(df, all_widgets)
        st.write(res)

