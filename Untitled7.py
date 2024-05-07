import pandas as pd
import requests
from io import BytesIO
import streamlit as st

def load_and_process_data(country, file_path_prefix):

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

st.title(countries)
st.line_chart(F_ad_Prob_Mod_Sev_values)
