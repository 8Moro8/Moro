import streamlit as st
import pandas as pd
import plotly as pt

excel_urls = {
    'kaz_2014': 'https://github.com/8Moro8/Moro/blob/main/kaz_2014.xlsx'
    'kaz_2015': 'https://github.com/8Moro8/Moro/blob/main/kaz_2015.xlsx'
    'kaz_2016': 'https://github.com/8Moro8/Moro/blob/main/kaz_2016.xlsx'
    'kaz_2017': 'https://github.com/8Moro8/Moro/blob/main/kaz_2017.xlsx'
    'kgz_2014': 'https://github.com/8Moro8/Moro/blob/main/kgz_2014.xlsx'
    'kgz_2015': 'https://github.com/8Moro8/Moro/blob/main/kgz_2015.xlsx'
    'kgz_2016': 'https://github.com/8Moro8/Moro/blob/main/kgz_2016.xlsx'
    'kgz_2017': 'https://github.com/8Moro8/Moro/blob/main/kgz_2017.xlsx'
    'tjk_2014': 'https://github.com/8Moro8/Moro/blob/main/tjk_2014.xlsx'
    'tjk_2015': 'https://github.com/8Moro8/Moro/blob/main/tjk_2015.xlsx'
    'tjk_2016': 'https://github.com/8Moro8/Moro/blob/main/tjk_2016.xlsx'
    'tjk_2017': 'https://github.com/8Moro8/Moro/blob/main/tjk_2017.xlsx'
    'uzb_2014': 'https://github.com/8Moro8/Moro/blob/main/uzb_2014.xlsx'
    'uzb_2015': 'https://github.com/8Moro8/Moro/blob/main/uzb_2015.xlsx'
    'uzb_2016': 'https://github.com/8Moro8/Moro/blob/main/uzb_2016.xlsx'
    'uzb_2017': 'https://github.com/8Moro8/Moro/blob/main/uzb_2017.xlsx'
}

# Выбор файла
file_name = st.selectbox('Выберите файл Excel', list(excel_urls.keys()))

# Загрузка данных
@st.cache  # Кэширование данных для повышения производительности
def load_data(file_url):
    return pd.read_excel(file_url, engine='openpyxl')

    F_ad_Prob_Mod_Sev = (pandas_df['Prob_Mod_Sev'] * pandas_df['wt']).sum() / pandas_df['wt'].sum()
    F_ad_Prob_Mod_Sev_values.append(float(F_ad_Prob_Mod_Sev))

df = load_data(excel_urls[file_name])

# Отображение данных
st.write(df)
