import streamlit as st
import pandas as pd

def load_and_process_data(country, file_path_prefix):
    F_ad_Prob_Mod_Sev_values = []

    for year in range(2014, 2018):
        file_name = f"{file_path_prefix}_{year}.xlsx"
        file_url = f"https://github.com/8Moro8/Moro/blob/main/{file_name}"
        
        try:
            pandas_df = pd.read_excel(file_url, engine='openpyxl')  # Указываем движок явно
            F_ad_Prob_Mod_Sev = (pandas_df['Prob_Mod_Sev'] * pandas_df['wt']).sum() / pandas_df['wt'].sum()
            F_ad_Prob_Mod_Sev_values.append(float(F_ad_Prob_Mod_Sev))
        except Exception as e:
            st.error(f"Ошибка при обработке файла {file_name}: {e}")

    return F_ad_Prob_Mod_Sev_values

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
