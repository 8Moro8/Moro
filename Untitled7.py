#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np
import dask.dataframe as dd
import streamlit as st
import matplotlib.pyplot as plt


# In[16]:


def load_and_process_data(country, file_path_prefix):
    pandas_df_2014 = pd.read_stata(file_path_prefix + '_2014_FIES_v01_EN_M_v01_A_OCS (1).dta')
    pandas_df_2015 = pd.read_stata(file_path_prefix + '_2015_FIES_v01_EN_M_v01_A_OCS (1).dta')
    pandas_df_2016 = pd.read_stata(file_path_prefix + '_2016_FIES_v01_EN_M_v01_A_OCS (1).dta')
    pandas_df_2017 = pd.read_stata(file_path_prefix + '_2017_FIES_v01_EN_M_v01_A_OCS (1).dta')

    numeric_columns_2014 = pandas_df_2014.select_dtypes(include=[np.number]).columns
    pandas_df_2014[numeric_columns_2014] = pandas_df_2014[numeric_columns_2014].fillna(0)

    numeric_columns_2015 = pandas_df_2015.select_dtypes(include=[np.number]).columns
    pandas_df_2015[numeric_columns_2015] = pandas_df_2015[numeric_columns_2015].fillna(0)

    numeric_columns_2016 = pandas_df_2016.select_dtypes(include=[np.number]).columns
    pandas_df_2016[numeric_columns_2016] = pandas_df_2016[numeric_columns_2016].fillna(0)

    numeric_columns_2017 = pandas_df_2017.select_dtypes(include=[np.number]).columns
    pandas_df_2017[numeric_columns_2017] = pandas_df_2017[numeric_columns_2017].fillna(0)

    dask_df_2014 = dd.from_pandas(pandas_df_2014, npartitions=1)
    dask_df_2015 = dd.from_pandas(pandas_df_2015, npartitions=1)
    dask_df_2016 = dd.from_pandas(pandas_df_2016, npartitions=1)
    dask_df_2017 = dd.from_pandas(pandas_df_2017, npartitions=1)

    dask_df_2014.compute().to_excel(file_path_prefix + '_2014.xlsx', index=False)
    dask_df_2015.compute().to_excel(file_path_prefix + '_2015.xlsx', index=False)
    dask_df_2016.compute().to_excel(file_path_prefix + '_2016.xlsx', index=False)
    dask_df_2017.compute().to_excel(file_path_prefix + '_2017.xlsx', index=False)

    F_ad_Prob_Mod_Sev_2014 = (dask_df_2014['Prob_Mod_Sev'] * dask_df_2014['wt']).sum().compute() / dask_df_2014['wt'].sum().compute()
    F_ad_Prob_Mod_Sev_2015 = (dask_df_2015['Prob_Mod_Sev'] * dask_df_2015['wt']).sum().compute() / dask_df_2015['wt'].sum().compute()
    F_ad_Prob_Mod_Sev_2016 = (dask_df_2016['Prob_Mod_Sev'] * dask_df_2016['wt']).sum().compute() / dask_df_2016['wt'].sum().compute()
    F_ad_Prob_Mod_Sev_2017 = (dask_df_2017['Prob_Mod_Sev'] * dask_df_2017['wt']).sum().compute() / dask_df_2017['wt'].sum().compute()

    F_ad_Prob_Mod_Sev_values = [
        float(F_ad_Prob_Mod_Sev_2014),
        float(F_ad_Prob_Mod_Sev_2015),
        float(F_ad_Prob_Mod_Sev_2016),
        float(F_ad_Prob_Mod_Sev_2017)
    ]

    return F_ad_Prob_Mod_Sev_values


# In[17]:


st.title("Анализ данных Центральной Азии")


# In[18]:


plt.figure(figsize=(10, 6))


# In[19]:


F_ad_Prob_Mod_Sev_kaz_values = load_and_process_data("Казахстан", r'C:\Users\sekre\Downloads\kaz\KAZ')
plt.plot(range(2014, 2018), F_ad_Prob_Mod_Sev_kaz_values, marker='o', linestyle='-', label='Казахстан')


# In[20]:


F_ad_Prob_Mod_Sev_uzb_values = load_and_process_data("Узбекистан", r'C:\Users\sekre\Downloads\uzb\UZB')
plt.plot(range(2014, 2018), F_ad_Prob_Mod_Sev_uzb_values, marker='o', linestyle='-', label='Узбекистан')


# In[21]:


F_ad_Prob_Mod_Sev_tjk_values = load_and_process_data("Таджикистан", r'C:\Users\sekre\Downloads\tjk\TJK')
plt.plot(range(2014, 2018), F_ad_Prob_Mod_Sev_tjk_values, marker='o', linestyle='-', label='Таджикистан')


# In[22]:


F_ad_Prob_Mod_Sev_kgz_values = load_and_process_data("Кыргызстан", r'C:\Users\sekre\Downloads\kgz\KGZ')
plt.plot(range(2014, 2018), F_ad_Prob_Mod_Sev_kgz_values, marker='o', linestyle='-', label='Кыргызстан')


# In[23]:


plt.title('Центральная Азия')
plt.xticks(range(2014, 2018))
plt.yticks(np.arange(0, 0.31, 0.05))
plt.legend()
plt.grid(True)


# In[24]:


st.pyplot(plt)


# In[ ]:




