streamlit==0.86
pandas==1.3
plotly==5.3

import streamlit as st
import pandas as pd
import plotly.express as px


file_paths = {
    'Kazakhstan 2014': 'https://github.com/8Moro8/Moro/blob/main/kaz_2014.xlsx',
    'Kazakhstan 2015': 'https://github.com/8Moro8/Moro/blob/main/kaz_2015.xlsx',
    'Kazakhstan 2016': 'https://github.com/8Moro8/Moro/blob/main/kaz_2016.xlsx',
    'Kazakhstan 2017': 'https://github.com/8Moro8/Moro/blob/main/kaz_2017.xlsx'
}

@st.cache
def load_data(file_path):
    return pd.read_excel(file_path)

st.title('Анализ данных о продовольственной безопасности')

selected_dataset = st.selectbox('Выберите набор данных:', list(file_paths.keys()))

data = load_data(file_paths[selected_dataset])

st.write('Первые несколько строк данных:')
st.write(data.head())

st.write('Визуализация данных:')
fig = px.line(data, x=data.index, y='Prob_Mod_Sev', title='Продовольственная безопасность в Казахстане по годам')
st.plotly_chart(fig)
