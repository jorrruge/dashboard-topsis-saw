import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# File paths
data_responden_path = 'Data Kuesioner Responden.xlsx'
bobot_ahp_topsis_saw_path = 'BOBOT AHP + MAU HITUNG TOPSIS SAW.xlsx'

# Load data
data_responden = pd.ExcelFile(data_responden_path)
bobot_topsis_saw = pd.ExcelFile(bobot_ahp_topsis_saw_path)

# Read specific sheets
data_responden_sheet1 = data_responden.parse(data_responden.sheet_names[0])
bobot_topsis_saw_sheet1 = bobot_topsis_saw.parse(bobot_topsis_saw.sheet_names[0])

# Sidebar input for selecting criteria
st.sidebar.header("Simulasi Perhitungan")
selected_criteria = st.sidebar.selectbox(
    "Pilih Kriteria untuk Simulasi:",
    ["Biaya Transaksi", "Keamanan", "Reputasi Platform", "Kemudahan Penggunaan", "Likuiditas", "Dukungan Pelanggan"]
)

# AHP Weights
ahp_weights = {
    "Biaya Transaksi": 0.39,
    "Keamanan": 0.25,
    "Reputasi Platform": 0.16,
    "Kemudahan Penggunaan": 0.11,
    "Likuiditas": 0.06,
    "Dukungan Pelanggan": 0.03
}

# Filtered Data
st.title("Dashboard Analisis Cryptocurrency Exchange")

st.header("Tabel Data Kuesioner Responden")
st.dataframe(data_responden_sheet1)

st.header("Tabel Perhitungan TOPSIS dan SAW")
st.dataframe(bobot_topsis_saw_sheet1)

# Visualization
st.header("Visualisasi Data")
criteria_values = bobot_topsis_saw_sheet1.iloc[2:5, 3:9]  # Example slicing for criteria visualization
criteria_values.columns = ["Binance", "Indodax", "Tokocrypto"]
criteria_values.index = ["Biaya Transaksi", "Keamanan", "Reputasi Platform"]

fig, ax = plt.subplots(figsize=(8, 5))
criteria_values.T.plot(kind='bar', ax=ax)
plt.title("Perbandingan Nilai Alternatif Berdasarkan Kriteria")
plt.ylabel("Nilai")
st.pyplot(fig)

# Simulation
st.header("Simulasi Ranking Berdasarkan Kriteria")
if selected_criteria in ahp_weights:
    criteria_rank = bobot_topsis_saw_sheet1[["Unnamed: 22", selected_criteria]].iloc[2:5]
    criteria_rank.columns = ["Alternatif", "Nilai"]
    criteria_rank = criteria_rank.sort_values(by="Nilai", ascending=False)
    st.write(f"Ranking Berdasarkan Kriteria {selected_criteria}:")
    st.dataframe(criteria_rank)
else:
    st.write("Kriteria tidak ditemukan dalam data.")

st.write("Silakan pilih kriteria lain di sidebar untuk melihat simulasi ranking.")
