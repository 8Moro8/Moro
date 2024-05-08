import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

excel_urls = {
    'kaz_2014': 'https://github.com/8Moro8/Moro/raw/main/kaz_2014.xlsx',
    'kaz_2015': 'https://github.com/8Moro8/Moro/raw/main/kaz_2015.xlsx',
    'kaz_2016': 'https://github.com/8Moro8/Moro/raw/main/kaz_2016.xlsx',
    'kaz_2017': 'https://github.com/8Moro8/Moro/raw/main/kaz_2017.xlsx',
    'kgz_2014': 'https://github.com/8Moro8/Moro/raw/main/kgz_2014.xlsx',
    'kgz_2015': 'https://github.com/8Moro8/Moro/raw/main/kgz_2015.xlsx',
    'kgz_2016': 'https://github.com/8Moro8/Moro/raw/main/kgz_2016.xlsx',
    'kgz_2017': 'https://github.com/8Moro8/Moro/raw/main/kgz_2017.xlsx',
    'tjk_2014': 'https://github.com/8Moro8/Moro/raw/main/tjk_2014.xlsx',
    'tjk_2015': 'https://github.com/8Moro8/Moro/raw/main/tjk_2015.xlsx',
    'tjk_2016': 'https://github.com/8Moro8/Moro/raw/main/tjk_2016.xlsx',
    'tjk_2017': 'https://github.com/8Moro8/Moro/raw/main/tjk_2017.xlsx',
    'uzb_2014': 'https://github.com/8Moro8/Moro/raw/main/uzb_2014.xlsx',
    'uzb_2015': 'https://github.com/8Moro8/Moro/raw/main/uzb_2015.xlsx',
    'uzb_2016': 'https://github.com/8Moro8/Moro/raw/main/uzb_2016.xlsx',
    'uzb_2017': 'https://github.com/8Moro8/Moro/raw/main/uzb_2017.xlsx'
}

# Функция для расчета F_ad_Prob_Mod_Sev
def calculate_F_ad_Prob_Mod_Sev(df):
    return (df['Prob_Mod_Sev'] * df['wt']).sum() / df['wt'].sum()

# Выбор файла
file_name = st.selectbox('Выберите файл Excel', list(excel_urls.keys()))

# Загрузка данных
@st.cache  # Кэширование данных для повышения производительности
def load_data(file_url):
    return pd.read_excel(file_url, engine='openpyxl')

df = load_data(excel_urls[file_name])

# Список для хранения значений F_ad_Prob_Mod_Sev для каждого года
F_ad_Prob_Mod_Sev_values = []

# Расчет F_ad_Prob_Mod_Sev для каждого года
for year in range(2014, 2018):
    df_year = df[df['Year'] == year]
    F_ad_Prob_Mod_Sev_values.append(calculate_F_ad_Prob_Mod_Sev(df_year))

# Построение графика
years = range(2014, 2018)
plt.figure(figsize=(10, 6))
plt.title(file_name)
plt.plot(years, F_ad_Prob_Mod_Sev_values, marker='o', linestyle='-')
plt.xticks(years)
plt.yticks(np.arange(0, 0.31, 0.05))
plt.grid(True)
