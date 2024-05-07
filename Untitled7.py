import pandas as pd
import numpy as np
import dask.dataframe as dd
import streamlit as st
import matplotlib.pyplot as plt

def load_and_process_data(country, file_path_prefix):
    import pandas as pd
    import requests
    from io import BytesIO

    base_url = 'https://github.com/8Moro8/Moro/blob/main/'

    F_ad_Prob_Mod_Sev_values = []

    for year in range(2014, 2018):
        file_name = f"{file_path_prefix}_{year}.xlsx"
        file_url = base_url + file_name
        response = requests.get(file_url)
        
        if response.status_code == 200:
            excel_data = response.content
            pandas_df = pd.read_excel(BytesIO(excel_data))
            F_ad_Prob_Mod_Sev = (pandas_df['Prob_Mod_Sev'] * pandas_df['wt']).sum() / pandas_df['wt'].sum()
            F_ad_Prob_Mod_Sev_values.append(float(F_ad_Prob_Mod_Sev))

    return F_ad_Prob_Mod_Sev_values

st.title("Анализ данных Центральной Азии")

plt.figure(figsize=(10, 6))

F_ad_Prob_Mod_Sev_kaz_values = load_and_process_data("Казахстан", r'C:\Users\sekre\Downloads\kaz\KAZ')
plt.plot(range(2014, 2018), F_ad_Prob_Mod_Sev_kaz_values, marker='o', linestyle='-', label='Казахстан')

F_ad_Prob_Mod_Sev_uzb_values = load_and_process_data("Узбекистан", r'C:\Users\sekre\Downloads\uzb\UZB')
plt.plot(range(2014, 2018), F_ad_Prob_Mod_Sev_uzb_values, marker='o', linestyle='-', label='Узбекистан')

F_ad_Prob_Mod_Sev_tjk_values = load_and_process_data("Таджикистан", r'C:\Users\sekre\Downloads\tjk\TJK')
plt.plot(range(2014, 2018), F_ad_Prob_Mod_Sev_tjk_values, marker='o', linestyle='-', label='Таджикистан')

F_ad_Prob_Mod_Sev_kgz_values = load_and_process_data("Кыргызстан", r'C:\Users\sekre\Downloads\kgz\KGZ')
plt.plot(range(2014, 2018), F_ad_Prob_Mod_Sev_kgz_values, marker='o', linestyle='-', label='Кыргызстан')

plt.title('Центральная Азия')
plt.xticks(range(2014, 2018))
plt.yticks(np.arange(0, 0.31, 0.05))
plt.legend()
plt.grid(True)

st.pyplot(plt)
