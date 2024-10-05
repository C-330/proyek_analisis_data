import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

load = pd.read_csv("dashboard/main_data.csv")

day_df = pd.DataFrame(load)

day_df['is_weekend'] = day_df['weekday'].apply(lambda x: 1 if x in [0, 6] else 0)

grouped_df = day_df.groupby('is_weekend').agg({
    'registered': 'sum'
}).reset_index()

total_rentals = grouped_df['registered'].sum()
grouped_df['percentage'] = (grouped_df['registered'] / total_rentals) * 100
grouped_df['is_weekend'] = grouped_df['is_weekend'].apply(lambda x: 'Weekend' if x == 1 else 'Workday')

st.title('Dashboard Penyewaan Sepeda')

st.subheader('Persentase Penyewaan Sepeda Selama Akhir Pekan vs Hari Kerja')
fig1, ax1 = plt.subplots(figsize=(8, 5))
ax1.bar(grouped_df['is_weekend'], grouped_df['percentage'], color=['lightblue', 'lightgreen'])

ax1.set_xlabel('Kategori')
ax1.set_ylabel('Persentase dari sepeda rental (%)')
ax1.set_title('Persentase Penyewaan Sepeda Selama Akhir Pekan vs Hari Kerja')

st.pyplot(fig1)

seasonYr_df = day_df[day_df['season'] == 2].groupby(by="yr").agg({
    "season": "nunique",
    "registered": "mean"
})

st.subheader('Rata-Rata Penyewaan Sepeda Musim Gugur')
fig2, ax2 = plt.subplots(figsize=(5, 5))
ax2.bar(seasonYr_df.index, seasonYr_df['registered'], color='blue')

ax2.set_xlabel('Tahun (0: 2011, 1: 2012)')
ax2.set_ylabel('Rata-rata Sepeda Disewa')
ax2.set_title('Rata-Rata Persewaan Tiap Musim Gugur Selama Dua Tahun Terakhir')

with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    st.write("Selamat datang di dashboard penyewaan sepeda.")
    st.write("Analisis data penyewaan sepeda berdasarkan hari dan musim.")
    st.write("---")  

st.pyplot(fig2)

st.caption('Data Sumber: https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset')
