import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.markdown("<h1 style='text-align: center; color: red; font-family: Times New Roman;'>Данная страница представляет тренды продовольственной безопасности центральной Азии</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: left; font-family: Times New Roman;'>Чтобы увидеть график с тенденцией нажмите на соответствующую кнопку</h1>", unsafe_allow_html=True)
st.title("←--------------------------------")

F_ad_Prob_Mod_Sev_kaz_values = [0.0737473506983265, 0.044529239425859325, 0.07208697980276833, 0.09025550050680399]
F_ad_Prob_Mod_Sev_uzb_values = [0.09872602667454446, 0.12482079148104783, 0.1033934827101725, 0.16342414956949367]
F_ad_Prob_Mod_Sev_tjk_values = [0.13234311608076732, 0.11086727498562164, 0.19598527440470287, 0.23921461895440915]
F_ad_Prob_Mod_Sev_kgz_values = [0.1875365079274166, 0.21059007745097164, 0.19581301002148638, 0.19449654750600165]
years = [2014, 2015, 2016, 2017]

def plot_country_graph(country, values, years):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(years, values, marker='o', linestyle='-')
    ax.set_title(country)
    ax.set_xticks(years)
    ax.set_yticks(np.arange(0, 0.31, 0.05))
    ax.grid(True)
    st.pyplot(fig)

st.sidebar.header("Выберите страну")
kaz_button = st.sidebar.button('Казахстан')
uzb_button = st.sidebar.button('Узбекистан')
tjk_button = st.sidebar.button('Таджикистан')
kgz_button = st.sidebar.button('Кыргызстан')
all_countries_button = st.sidebar.button('Все страны')

chart_placeholder = st.empty()

if kaz_button:
    plot_country_graph('Казахстан', F_ad_Prob_Mod_Sev_kaz_values, years)
elif uzb_button:
    plot_country_graph('Узбекистан', F_ad_Prob_Mod_Sev_uzb_values, years)
elif tjk_button:
    plot_country_graph('Таджикистан', F_ad_Prob_Mod_Sev_tjk_values, years)
elif kgz_button:
    plot_country_graph('Кыргызстан', F_ad_Prob_Mod_Sev_kgz_values, years)
elif all_countries_button:
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(years, F_ad_Prob_Mod_Sev_kaz_values, marker='o', linestyle='-', label='Казахстан')
    ax.plot(years, F_ad_Prob_Mod_Sev_uzb_values, marker='o', linestyle='-', label='Узбекистан')
    ax.plot(years, F_ad_Prob_Mod_Sev_kgz_values, marker='o', linestyle='-', label='Кыргызстан')
    ax.plot(years, F_ad_Prob_Mod_Sev_tjk_values, marker='o', linestyle='-', label='Таджикистан')
    ax.set_title('Центральная Азия')
    ax.set_xticks(years)
    ax.set_yticks(np.arange(0, 0.3, 0.05))
    ax.legend()
    ax.grid(True)
    chart_placeholder.pyplot(fig)
