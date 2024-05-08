import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import dask.dataframe as dd

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

# Выбор файла
file_name = st.selectbox('Выберите файл Excel', list(excel_urls.keys()))

# Загрузка данных
def load_data(file_url):
    return pd.read_excel(file_url, engine='openpyxl')

# Загрузка данных и вычисление F_ad_Prob_Mod_Sev
def process_data(df):
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    df[numeric_columns] = df[numeric_columns].fillna(0)
    dask_df = dd.from_pandas(df, npartitions=1)
    F_ad_Prob_Mod_Sev = (dask_df['Prob_Mod_Sev'] * dask_df['wt']).sum() / dask_df['wt'].sum()
    return float(F_ad_Prob_Mod_Sev)

# Обработка данных и построение графика
df = load_data(excel_urls[file_name])
F_ad_Prob_Mod_Sev_values = [process_data(df[df.columns[1:]]) for _ in range(2014, 2018)]  # Одно значение для каждого года

# Построение графика
years = range(2014, 2018)
plt.figure(figsize=(10, 6))
plt.title('Казахстан')
plt.plot(years, F_ad_Prob_Mod_Sev_values, marker='o', linestyle='-')
plt.xticks(years)
plt.yticks(np.arange(0, 0.31, 0.05))
plt.grid(True)

# Вывод графика в Streamlit
st.pyplot(plt)
