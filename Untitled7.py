import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
@st.cache  # Кэширование данных для повышения производительности
def load_data(file_url):
    return pd.read_excel(file_url, engine='openpyxl')

df = load_data(excel_urls[file_name])

# Создание списка значений F_Prob_Mod_Sev для каждого года с 2014 по 2017
F_Prob_Mod_Sev_values = []
for year in (2014, 2015, 2016, 2017):
    F_Prob_Mod_Sev = (df['Prob_Mod_Sev'] * df['wt']).sum() / df['wt'].sum()
    F_Prob_Mod_Sev_values.append(F_Prob_Mod_Sev)

# Построение графика
years = range(2014, 2018)

plt.figure(figsize=(10, 6))
plt.title('Казахстан')
plt.plot(years, F_ad_Prob_Mod_Sev_kaz_values, marker='o', linestyle='-')
plt.xticks(years)
plt.yticks(np.arange(0, 0.31, 0.05))
plt.grid(True)
plt.show()
