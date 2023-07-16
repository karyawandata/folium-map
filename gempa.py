import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

# Membaca file CSV
df = pd.read_csv("gempa.csv")

# Mengatur judul halaman
st.title("Data Gempa")

# Menampilkan tabel dengan kolom yang dipilih
st.write(df[["Magnitudo", "Lokasi", "Latitude", "Longitude"]])

# Create a map centered around the mean of latitude and longitude values
m = folium.Map(location=df[['Latitude', 'Longitude']].mean().to_list(), zoom_start=2)

# Add marker cluster to map
marker_cluster = MarkerCluster().add_to(m)

# Add data points to the map
for idx, row in df.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['Lokasi']).add_to(marker_cluster)

# Display map in Streamlit
folium_static(m, width=1000, height=800)
