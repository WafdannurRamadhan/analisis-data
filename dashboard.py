import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Preprocessing
day_df.drop(["windspeed"], axis=1, inplace=True)
hour_df.drop(["windspeed"], axis=1, inplace=True)

# Analysis
factor = day_df.groupby('weathersit')['cnt'].mean().reset_index()
weekday = day_df.groupby(by='workingday')['cnt'].mean().reset_index()

# Streamlit app
st.title('Analisis Penggunaan Sepeda')

st.write('### Data Hari')
st.write(day_df.head())

st.write('### Data Jam')
st.write(hour_df.head())

st.write('### Jumlah Duplikasi Data Hari: ', day_df.duplicated().sum())
st.write('### Jumlah Duplikasi Data Jam: ', hour_df.duplicated().sum())

st.write('### Statistik Deskriptif Data Hari')
st.write(day_df.describe(include="all"))

st.write('### Statistik Deskriptif Data Jam')
st.write(hour_df.describe(include='all'))

st.write('## Diagram Peminjaman Sepeda berdasarkan Kondisi Cuaca')
fig, ax = plt.subplots(figsize=(8,6))
sns.barplot(x='weathersit',
            y='cnt',
            palette=['red', 'blue', 'green'],
            data=factor,
            ax=ax)
plt.title('Diagram Peminjaman Sepeda berdasarkan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Jumlah Peminjaman Sepeda')
st.pyplot(fig)

st.write('## Perbandingan Pengguna Sepeda di Hari Kerja dan Akhir Pekan')
plt.figure(figsize=(8, 6))
sns.barplot(x='workingday',
            y='cnt',
            palette=['red', 'green'],
            data=weekday)
plt.title('Perbandingan Pengguna sepeda di Weekdays dan Weekend')
plt.xlabel('Perbedaan Hari')
plt.ylabel('Jumlah Pengguna Sepeda')
st.pyplot()
