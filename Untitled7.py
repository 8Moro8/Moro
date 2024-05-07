import pandas as pd
import numpy as np
import dask.dataframe as dd
import streamlit as st
import matplotlib.pyplot as plt

def load_and_process_data(country, file_path_prefix):
    pandas_df_2014 = pd.read_excel(file_path_prefix + '_2014.xlsx')
    pandas_df_2015 = pd.read_excel(file_path_prefix + '_2015.xlsx')
    pandas_df_2016 = pd.read_excel(file_path_prefix + '_2016.xlsx')
    pandas_df_2017 = pd.read_excel(file_path_prefix + '_2017.xlsx')

    F_ad_Prob_Mod_Sev_2014 = (pandas_df_2014['Prob_Mod_Sev'] * pandas_df_2014['wt']).sum() / pandas_df_2014['wt'].sum()
    F_ad_Prob_Mod_Sev_2015 = (pandas_df_2015['Prob_Mod_Sev'] * pandas_df_2015['wt']).sum() / pandas_df_2015['wt'].sum()
    F_ad_Prob_Mod_Sev_2016 = (pandas_df_2016['Prob_Mod_Sev'] * pandas_df_2016['wt']).sum() / pandas_df_2016['wt'].sum()
    F_ad_Prob_Mod_Sev_2017 = (pandas_df_2017['Prob_Mod_Sev'] * pandas_df_2017['wt']).sum() / pandas_df_2017['wt'].sum()

    F_ad_Prob_Mod_Sev_values = [
        float(F_ad_Prob_Mod_Sev_2014),
        float(F_ad_Prob_Mod_Sev_2015),
        float(F_ad_Prob_Mod_Sev_2016),
        float(F_ad_Prob_Mod_Sev_2017)
    ]

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
