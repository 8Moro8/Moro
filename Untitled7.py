import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Значения для графиков
F_ad_Prob_Mod_Sev_kaz_values = [0.0737473506983265, 0.044529239425859325, 0.07208697980276833, 0.09025550050680399]
F_ad_Prob_Mod_Sev_uzb_values = [0.09872602667454446, 0.12482079148104783, 0.1033934827101725, 0.16342414956949367]
F_ad_Prob_Mod_Sev_tjk_values = [0.13234311608076732, 0.11086727498562164, 0.19598527440470287, 0.23921461895440915]
F_ad_Prob_Mod_Sev_kgz_values = [0.1875365079274166, 0.21059007745097164, 0.19581301002148638, 0.19449654750600165]
years = [2014, 2015, 2016, 2017]

# Вывод графиков по отдельности
def plot_country_graph(country, values, years):
    plt.figure(figsize=(10, 6))
    plt.title(country)
    plt.plot(years, values, marker='o', linestyle='-')
    plt.xticks(years)
    plt.yticks(np.arange(0, 0.31, 0.05))
    plt.grid(True)
    st.pyplot()

# Выбор графика с помощью кнопки
button = st.selectbox('Выберите график', ['Казахстан', 'Узбекистан', 'Таджикистан', 'Кыргызстан', 'Центральная Азия'])

if button == 'Казахстан':
    plot_country_graph('Казахстан', F_ad_Prob_Mod_Sev_kaz_values, years)
elif button == 'Узбекистан':
    plot_country_graph('Узбекистан', F_ad_Prob_Mod_Sev_uzb_values, years)
elif button == 'Таджикистан':
    plot_country_graph('Таджикистан', F_ad_Prob_Mod_Sev_tjk_values, years)
elif button == 'Кыргызстан':
    plot_country_graph('Кыргызстан', F_ad_Prob_Mod_Sev_kgz_values, years)
else:
    plt.figure(figsize=(10, 6))
    plt.plot(years, F_ad_Prob_Mod_Sev_kaz_values, marker='o', linestyle='-', label='Казахстан')
    plt.plot(years, F_ad_Prob_Mod_Sev_uzb_values, marker='o', linestyle='-', label='Узбекистан')
    plt.plot(years, F_ad_Prob_Mod_Sev_kgz_values, marker='o', linestyle='-', label='Кыргызстан')
    plt.plot(years, F_ad_Prob_Mod_Sev_tjk_values, marker='o', linestyle='-', label='Таджикистан')
    plt.title('Центральная Азия')
    plt.xticks(years)
    plt.yticks(np.arange(0, 0.3, 0.05))
    plt.legend()
    plt.grid(True)
    st.pyplot()
