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

# Загрузка данных
countries = ['Казахстан', 'Кыргызстан', 'Таджикистан', 'Узбекистан']
country = st.selectbox('Выберите страну', countries)

file_path_prefixes = {
    'Казахстан': 'kaz',
    'Кыргызстан': 'kgz',
    'Таджикистан': 'tjk',
    'Узбекистан': 'uzb'
}
file_path_prefix = file_path_prefixes[country]

F_ad_Prob_Mod_Sev_values = load_and_process_data(country, file_path_prefix)

# Отображение результатов
st.title(country)
st.line_chart(F_ad_Prob_Mod_Sev_values)
