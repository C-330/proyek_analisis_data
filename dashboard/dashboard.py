import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

load = pd.read_csv("dashboard/main_data.csv")

day_df = pd.DataFrame(load)

holiReg = day_df.groupby(by="weekday").agg({
    "holiday": "sum",
    "registered": "mean"
}).reset_index()

days = ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu']
holiReg['weekday'] = holiReg['weekday'].apply(lambda x: days[x])

seasonYr_df = day_df[day_df['season'] == 2].groupby(by="yr").agg({
    "season": "nunique",
    "registered": "mean"
})

st.title('Dashboard Penyewaan Sepeda')

st.subheader('Pengaruh Hari Libur Terhadap Penyewaan Sepeda Tiap Hari')
fig1, ax1 = plt.subplots(figsize=(10, 5))

color = 'tab:blue'
ax1.set_xlabel('Hari dalam Minggu')
ax1.set_ylabel('Jumlah Hari Libur', color=color)
ax1.bar(holiReg['weekday'], holiReg['holiday'], color=color, alpha=0.6, label='Jumlah Hari Libur')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Rata-rata Penyewaan Sepeda', color=color)
ax2.plot(holiReg['weekday'], holiReg['registered'], color=color, marker='o', label='Rata-rata Penyewaan Sepeda')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Pengaruh Hari Libur Terhadap Penyewaan Sepeda Tiap Hari')
fig1.tight_layout()
st.pyplot(fig1)

st.subheader('Rata-Rata Penyewaan Sepeda Musim Gugur')
fig2, ax2 = plt.subplots(figsize=(5, 5))
ax2.bar(seasonYr_df.index, seasonYr_df['registered'], color='blue')

ax2.set_xlabel('Tahun (0: 2011, 1: 2012)')
ax2.set_ylabel('Rata-rata Sepeda Disewa')
ax2.set_title('Rata-Rata Persewaan Tiap Musim Gugur Selama Dua Tahun Terakhir')


st.title('Dashboard Penyewaan Sepeda')


with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    st.write("Selamat datang di dashboard penyewaan sepeda.")
    st.write("Analisis data penyewaan sepeda berdasarkan hari dan musim.")
    st.write("---")  

st.pyplot(fig2)

st.caption('Data Sumber: https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset')

