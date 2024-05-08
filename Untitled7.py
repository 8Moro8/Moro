import streamlit as st
import pandas as pd
import numpy as np
import dask.dataframe as dd
import matplotlib.pyplot as plt

kaz_2014 = 'https://github.com/8Moro8/Moro/raw/main/KAZ_2014_FIES_v01_EN_M_v01_A_OCS%20(1).dta'
kaz_2015 = 'https://github.com/8Moro8/Moro/raw/main/KAZ_2015_FIES_v01_EN_M_v01_A_OCS%20(1).dta'
kaz_2016 = 'https://github.com/8Moro8/Moro/raw/main/KAZ_2016_FIES_v01_EN_M_v01_A_OCS%20(1).dta'
kaz_2017 = 'https://github.com/8Moro8/Moro/raw/main/KAZ_2017_FIES_v01_EN_M_v01_A_OCS%20(1).dta'

pandas_df_kaz_2014 = pd.read_stata(kaz_2014)
pandas_df_kaz_2015 = pd.read_stata(kaz_2015)
pandas_df_kaz_2016 = pd.read_stata(kaz_2016)
pandas_df_kaz_2017 = pd.read_stata(kaz_2017)

numeric_columns_kaz_2014 = pandas_df_kaz_2014.select_dtypes(include=[np.number]).columns
pandas_df_kaz_2014[numeric_columns_kaz_2014] = pandas_df_kaz_2014[numeric_columns_kaz_2014].fillna(0)

numeric_columns_kaz_2015 = pandas_df_kaz_2015.select_dtypes(include=[np.number]).columns
pandas_df_kaz_2015[numeric_columns_kaz_2015] = pandas_df_kaz_2015[numeric_columns_kaz_2015].fillna(0)

numeric_columns_kaz_2016 = pandas_df_kaz_2016.select_dtypes(include=[np.number]).columns
pandas_df_kaz_2016[numeric_columns_kaz_2016] = pandas_df_kaz_2016[numeric_columns_kaz_2016].fillna(0)

numeric_columns_kaz_2017 = pandas_df_kaz_2017.select_dtypes(include=[np.number]).columns
pandas_df_kaz_2017[numeric_columns_kaz_2017] = pandas_df_kaz_2017[numeric_columns_kaz_2017].fillna(0)

dask_df_kaz_2014 = dd.from_pandas(pandas_df_kaz_2014, npartitions=1)
dask_df_kaz_2015 = dd.from_pandas(pandas_df_kaz_2015, npartitions=1)
dask_df_kaz_2016 = dd.from_pandas(pandas_df_kaz_2016, npartitions=1)
dask_df_kaz_2017 = dd.from_pandas(pandas_df_kaz_2017, npartitions=1)

F_ad_Prob_Mod_Sev_kaz_2014 = (dask_df_kaz_2014['Prob_Mod_Sev'] * dask_df_kaz_2014['wt']).sum() / dask_df_kaz_2014['wt'].sum()
F_ad_Prob_Mod_Sev_kaz_2015 = (dask_df_kaz_2015['Prob_Mod_Sev'] * dask_df_kaz_2015['wt']).sum() / dask_df_kaz_2015['wt'].sum()
F_ad_Prob_Mod_Sev_kaz_2016 = (dask_df_kaz_2016['Prob_Mod_Sev'] * dask_df_kaz_2016['wt']).sum() / dask_df_kaz_2016['wt'].sum()
F_ad_Prob_Mod_Sev_kaz_2017 = (dask_df_kaz_2017['Prob_Mod_Sev'] * dask_df_kaz_2017['wt']).sum() / dask_df_kaz_2017['wt'].sum()

F_ad_Prob_Mod_Sev_kaz_values = [0.0737473506983265, 0.044529239425859325, 0.07208697980276833, 0.09025550050680399]

years = np.arange(2014, 2018)

plt.figure(figsize=(10, 6))
plt.title('Казахстан')
plt.plot(years, F_ad_Prob_Mod_Sev_kaz_values, marker='o', linestyle='-')
plt.xticks(years)
plt.yticks(np.arange(0, 0.31, 0.05))
plt.grid(True)
plt.show()

print("Years:", years)
print("F_ad_Prob_Mod_Sev_kaz_values:", F_ad_Prob_Mod_Sev_kaz_values)

uzb_2014 = 'https://github.com/8Moro8/Moro/raw/main/UZB_2014_FIES_v01_EN_M_v01_A_OCS%20(1).dta'
uzb_2015 = 'https://github.com/8Moro8/Moro/raw/main/UZB_2015_FIES_v01_EN_M_v01_A_OCS%20(1).dta'
uzb_2016 = 'https://github.com/8Moro8/Moro/raw/main/UZB_2016_FIES_v01_EN_M_v01_A_OCS%20(1).dta'
uzb_2017 = 'https://github.com/8Moro8/Moro/raw/main/UZB_2017_FIES_v01_EN_M_v01_A_OCS%20(1).dta'

pandas_df_uzb_2014 = pd.read_stata(uzb_2014)
pandas_df_uzb_2015 = pd.read_stata(uzb_2015)
pandas_df_uzb_2016 = pd.read_stata(uzb_2016)
pandas_df_uzb_2017 = pd.read_stata(uzb_2017)

numeric_columns_uzb_2014 = pandas_df_uzb_2014.select_dtypes(include=[np.number]).columns
pandas_df_uzb_2014[numeric_columns_uzb_2014] = pandas_df_uzb_2014[numeric_columns_uzb_2014].fillna(0)

numeric_columns_uzb_2015 = pandas_df_uzb_2015.select_dtypes(include=[np.number]).columns
pandas_df_uzb_2015[numeric_columns_uzb_2015] = pandas_df_uzb_2015[numeric_columns_uzb_2015].fillna(0)

numeric_columns_uzb_2016 = pandas_df_uzb_2016.select_dtypes(include=[np.number]).columns
pandas_df_uzb_2016[numeric_columns_uzb_2016] = pandas_df_uzb_2016[numeric_columns_uzb_2016].fillna(0)

numeric_columns_uzb_2017 = pandas_df_uzb_2017.select_dtypes(include=[np.number]).columns
pandas_df_uzb_2017[numeric_columns_uzb_2017] = pandas_df_uzb_2017[numeric_columns_uzb_2017].fillna(0)

dask_df_uzb_2014 = dd.from_pandas(pandas_df_uzb_2014, npartitions=1)
dask_df_uzb_2015 = dd.from_pandas(pandas_df_uzb_2015, npartitions=1)
dask_df_uzb_2016 = dd.from_pandas(pandas_df_uzb_2016, npartitions=1)
dask_df_uzb_2017 = dd.from_pandas(pandas_df_uzb_2017, npartitions=1)

F_ad_Prob_Mod_Sev_uzb_2014 = (dask_df_uzb_2014['Prob_Mod_Sev'] * dask_df_uzb_2014['wt']).sum() / dask_df_uzb_2014['wt'].sum()
F_ad_Prob_Mod_Sev_uzb_2015 = (dask_df_uzb_2015['Prob_Mod_Sev'] * dask_df_uzb_2015['wt']).sum() / dask_df_uzb_2015['wt'].sum()
F_ad_Prob_Mod_Sev_uzb_2016 = (dask_df_uzb_2016['Prob_Mod_Sev'] * dask_df_uzb_2016['wt']).sum() / dask_df_uzb_2016['wt'].sum()
F_ad_Prob_Mod_Sev_uzb_2017 = (dask_df_uzb_2017['Prob_Mod_Sev'] * dask_df_uzb_2017['wt']).sum() / dask_df_uzb_2017['wt'].sum()

F_ad_Prob_Mod_Sev_uzb_values = [0.09872602667454446, 0.12482079148104783, 0.1033934827101725, 0.16342414956949367]

plt.figure(figsize=(10, 6))
plt.title('Узбекистан')
plt.plot(years, F_ad_Prob_Mod_Sev_uzb_values, marker='o', linestyle='-')
plt.xticks(years)
plt.yticks(np.arange(0, 0.31, 0.05))
plt.grid(True)
plt.show()

tjk_2014 = 'https://github.com/8Moro8/Moro/raw/main/TJK_2014_FIES_v01_EN_M_v01_A_OCS%20(1).dta'
tjk_2015 = 'https://github.com/8Moro8/Moro/raw/main/TJK_2015_FIES_v01_EN_M_v01_A_OCS%20(1).dta'
tjk_2016 = 'https://github.com/8Moro8/Moro/raw/main/TJK_2016_FIES_v01_EN_M_v01_A_OCS%20(1).dta'
tjk_2017 = 'https://github.com/8Moro8/Moro/raw/main/TJK_2017_FIES_v01_EN_M_v01_A_OCS%20(1).dta'

pandas_df_tjk_2014 = pd.read_stata(tjk_2014)
pandas_df_tjk_2015 = pd.read_stata(tjk_2015)
pandas_df_tjk_2016 = pd.read_stata(tjk_2016)
pandas_df_tjk_2017 = pd.read_stata(tjk_2017)

numeric_columns_tjk_2014 = pandas_df_tjk_2014.select_dtypes(include=[np.number]).columns
pandas_df_tjk_2014[numeric_columns_tjk_2014] = pandas_df_tjk_2014[numeric_columns_tjk_2014].fillna(0)

numeric_columns_tjk_2015 = pandas_df_tjk_2015.select_dtypes(include=[np.number]).columns
pandas_df_tjk_2015[numeric_columns_tjk_2015] = pandas_df_tjk_2015[numeric_columns_tjk_2015].fillna(0)

numeric_columns_tjk_2016 = pandas_df_tjk_2016.select_dtypes(include=[np.number]).columns
pandas_df_tjk_2016[numeric_columns_tjk_2016] = pandas_df_tjk_2016[numeric_columns_tjk_2016].fillna(0)

numeric_columns_tjk_2017 = pandas_df_tjk_2017.select_dtypes(include=[np.number]).columns
pandas_df_tjk_2017[numeric_columns_tjk_2017] = pandas_df_tjk_2017[numeric_columns_tjk_2017].fillna(0)

dask_df_tjk_2014 = dd.from_pandas(pandas_df_tjk_2014, npartitions=1)
dask_df_tjk_2015 = dd.from_pandas(pandas_df_tjk_2015, npartitions=1)
dask_df_tjk_2016 = dd.from_pandas(pandas_df_tjk_2016, npartitions=1)
dask_df_tjk_2017 = dd.from_pandas(pandas_df_tjk_2017, npartitions=1)

F_ad_Prob_Mod_Sev_tjk_2014 = (dask_df_tjk_2014['Prob_Mod_Sev'] * dask_df_tjk_2014['wt']).sum() / dask_df_tjk_2014['wt'].sum()
F_ad_Prob_Mod_Sev_tjk_2015 = (dask_df_tjk_2015['Prob_Mod_Sev'] * dask_df_tjk_2015['wt']).sum() / dask_df_tjk_2015['wt'].sum()
F_ad_Prob_Mod_Sev_tjk_2016 = (dask_df_tjk_2016['Prob_Mod_Sev'] * dask_df_tjk_2016['wt']).sum() / dask_df_tjk_2016['wt'].sum()
F_ad_Prob_Mod_Sev_tjk_2017 = (dask_df_tjk_2017['Prob_Mod_Sev'] * dask_df_tjk_2017['wt']).sum() / dask_df_tjk_2017['wt'].sum()

F_ad_Prob_Mod_Sev_tjk_values = [0.13234311608076732, 0.11086727498562164, 0.19598527440470287, 0.23921461895440915]

plt.figure(figsize=(10, 6))
plt.title('Таджикистан')
plt.plot(years, F_ad_Prob_Mod_Sev_tjk_values, marker='o', linestyle='-')
plt.xticks(years)
plt.yticks(np.arange(0, 0.31, 0.05))
plt.grid(True)
plt.show()

kgz_2014 = 'https://github.com/8Moro8/Moro/raw/main/KGZ_2014_FIES_v01_EN_M_v01_A_OCS%20(1).dta'
kgz_2015 = 'https://github.com/8Moro8/Moro/raw/main/KGZ_2015_FIES_v01_EN_M_v01_A_OCS%20(1).dta'
kgz_2016 = 'https://github.com/8Moro8/Moro/raw/main/KGZ_2016_FIES_v01_EN_M_v01_A_OCS%20(1).dta'
kgz_2017 = 'https://github.com/8Moro8/Moro/raw/main/KGZ_2017_FIES_v01_EN_M_v01_A_OCS%20(1).dta'

pandas_df_kgz_2014 = pd.read_stata(kgz_2014)
pandas_df_kgz_2015 = pd.read_stata(kgz_2015)
pandas_df_kgz_2016 = pd.read_stata(kgz_2016)
pandas_df_kgz_2017 = pd.read_stata(kgz_2017)

numeric_columns_kgz_2014 = pandas_df_kgz_2014.select_dtypes(include=[np.number]).columns
pandas_df_kgz_2014[numeric_columns_kgz_2014] = pandas_df_kgz_2014[numeric_columns_kgz_2014].fillna(0)

numeric_columns_kgz_2015 = pandas_df_kgz_2015.select_dtypes(include=[np.number]).columns
pandas_df_kgz_2015[numeric_columns_kgz_2015] = pandas_df_kgz_2015[numeric_columns_kgz_2015].fillna(0)

numeric_columns_kgz_2016 = pandas_df_kgz_2016.select_dtypes(include=[np.number]).columns
pandas_df_kgz_2016[numeric_columns_kgz_2016] = pandas_df_kgz_2016[numeric_columns_kgz_2016].fillna(0)

numeric_columns_kgz_2017 = pandas_df_kgz_2017.select_dtypes(include=[np.number]).columns
pandas_df_kgz_2017[numeric_columns_kgz_2017] = pandas_df_kgz_2017[numeric_columns_kgz_2017].fillna(0)

dask_df_kgz_2014 = dd.from_pandas(pandas_df_kgz_2014, npartitions=1)
dask_df_kgz_2015 = dd.from_pandas(pandas_df_kgz_2015, npartitions=1)
dask_df_kgz_2016 = dd.from_pandas(pandas_df_kgz_2016, npartitions=1)
dask_df_kgz_2017 = dd.from_pandas(pandas_df_kgz_2017, npartitions=1)

F_ad_Prob_Mod_Sev_kgz_2014 = (dask_df_kgz_2014['Prob_Mod_Sev'] * dask_df_kgz_2014['wt']).sum() / dask_df_kgz_2014['wt'].sum()
F_ad_Prob_Mod_Sev_kgz_2015 = (dask_df_kgz_2015['Prob_Mod_Sev'] * dask_df_kgz_2015['wt']).sum() / dask_df_kgz_2015['wt'].sum()
F_ad_Prob_Mod_Sev_kgz_2016 = (dask_df_kgz_2016['Prob_Mod_Sev'] * dask_df_kgz_2016['wt']).sum() / dask_df_kgz_2016['wt'].sum()
F_ad_Prob_Mod_Sev_kgz_2017 = (dask_df_kgz_2017['Prob_Mod_Sev'] * dask_df_kgz_2017['wt']).sum() / dask_df_kgz_2017['wt'].sum()

F_ad_Prob_Mod_Sev_kgz_values = [0.1875365079274166, 0.21059007745097164, 0.19581301002148638, 0.19449654750600165]

plt.figure(figsize=(10, 6))
plt.title('Кыргызстан')
plt.plot(years, F_ad_Prob_Mod_Sev_kgz_values, marker='o', linestyle='-')
plt.xticks(years)
plt.yticks(np.arange(0, 0.3, 0.05))
plt.grid(True)
plt.show()

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
plt.show()
