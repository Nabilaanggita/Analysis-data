import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('Dashboard/data_siap (1).csv')

# membuat bar navigasi
nav_buttons = st.columns(4)
beranda_button = nav_buttons[0].button("Beranda")
bulan_button = nav_buttons[1].button("Bulan")
weathersit_button = nav_buttons[2].button("Weathersit")
tambahan_button = nav_buttons[3].button("Tambahan")
selected_button = None
if beranda_button:
    selected_button = "Beranda"
elif bulan_button:
    selected_button = "Bulan"
elif weathersit_button:
    selected_button = "Weathersit"
elif tambahan_button:
    selected_button = "Tambahan"
#membuat halaman beranda
if selected_button == "Beranda":
            st.title("Analisis Data Pengguna Sepeda")
            st.write("Selamat datang di analisis data pengguna sepeda!")
            st.write("pilih hasil visualisasi data pada button diatas")
            st.write("button bulan menjawab pertanyaan 1 Bagaimana performa pengguna jasa sewa sepeda tiap bulannya?")
            st.write("button weathersit menjawab pertanyaan 2 Bagaimana cuaca mempengaruhi kondisi perjalanan dan pengalaman pengguna saat bersepeda? ")

            st.write("Pilih jenis analisis data yang anda inginkan .")
            st.image('Dashboard/naik_sepeda.jpg', use_column_width=True)  
            st.header("Pencarian Data jumlah pelanggan")                
            st.header("Filter Data yang diinginkan")
            bulan_filter = st.selectbox("Pilih Bulan", df["mnth"].unique())
            tahun_filter = st.selectbox("Pilih Tahun", df["yr"].unique())
            cuaca_filter = st.selectbox("Pilih Cuaca", df["weathersit"].unique())
            df_filtered = df[(df["mnth"] == bulan_filter) & (df["yr"] == tahun_filter) & (df["weathersit"] == cuaca_filter)]               
            st.write("jumlahData yang sesuai:")
            sum_cnt = df_filtered["cnt"].sum()
            sum_casual = df_filtered["casual"].sum()
            sum_registered = df_filtered["registered"].sum()
            st.write("Data yang difilter:")
            st.write(df_filtered[["cnt", "casual", "registered"]])
            st.write("Total Penyewa:", sum_cnt)
            st.write("Total Casual:", sum_casual)
            st.write("Total Registered:", sum_registered)

        

elif selected_button == "Bulan":
            # Membuat kolom baru untuk tanggal
            df['dteday'] = pd.to_datetime(df['dteday'])
            df['weekday'] = df['dteday'].dt.day_name()
            df['mnth'] = df['dteday'].dt.month_name()
            df['yr'] = df['dteday'].dt.year

            # Membuat dashboard
            st.title("Analisis Data Pengguna Sepeda tiap bulannya")
            st.write("Bagaimana performa pengguna jasa sewa sepeda tiap bulannya?")

            # Pertanyaan 1: Bagaimana performa pengguna jasa sewa sepeda tiap bulannya?
            st.header("Performa Pengguna Jasa Sewa Sepeda Tiap Bulannya")
            st.write("Grafik persewaan sepeda tiap bulannya pada tahun 2011-2012")
            plt.figure(figsize=(10,6))
            sns.lineplot(x="dteday", y="cnt", data=df, color='blue')
            plt.xlabel("Tanggal")
            plt.ylabel("Total penyewa")
            plt.title("grafik persewaan sepeda tiap bulannya pada tahun 2011-2012")
            plt.tight_layout()
            plt.show() 


            # Tabel data bulan
            mean_df = df.groupby(by="mnth").agg({
                "mnth": "nunique",
                "cnt": ["mean", "std", "max", "min"]
            })
            mean_df = mean_df.reset_index()
            mean_df.columns = ["_".join(col) for col in mean_df.columns.values]

            # Grafik rata-rata pengguna sepeda tiap bulannya
            plt.figure(figsize=(10,6))
            sns.lineplot(x=mean_df.index, y=mean_df["cnt_mean"], color='blue')
            sns.lineplot(x=mean_df.index, y=mean_df["cnt_std"], color='red')
            sns.lineplot(x=mean_df.index, y=mean_df["cnt_max"], color='green')
            sns.lineplot(x=mean_df.index, y=mean_df["cnt_min"], color='yellow')
            plt.xlabel("bulan")
            plt.ylabel("Total penyewa")
            plt.title("rata grafik persewaan sepeda tiap bulannya pada tahun 2011-2012")
            plt.tight_layout()
            plt.show()


            # Data urut terbanyak penyewa berdasarkan bulan
            st.write("Data Urut Terbanyak Penyewa Berdasarkan Bulan")
            st.write(df.groupby(by="mnth").nunique().sort_values(by='cnt', ascending=False))

            # Data urut terkecil penyewa berdasarkan bulan
            st.write("Data Urut Terkecil Penyewa Berdasarkan Bulan")
            st.write(df.groupby(by="mnth").nunique().sort_values(by='cnt', ascending=True))
            st.write("peforma pengguna naik turun namun cenderung meningkat . grafik tiap bulannya mengalami naik turun.terjadi penurunan yang sangat drastis pda bulan april. setelah saya analisis lebih lanjut dikarenakan faktor cuaca. kemudian pda saat bulan berikutnya meningkat terjadi penurunan namun tidak sedrastis pada bulan pertama.")


elif selected_button== "Weathersit":
            st.write("Bagaimana cuaca mempengaruhi kondisi perjalanan dan pengalaman pengguna saat bersepeda?")
            # Pertanyaan 2: Bagaimana cuaca mempengaruhi kondisi perjalanan dan pengalaman pengguna saat bersepeda?
            plt.figure(figsize=(10,6))
            sns.barplot(x="weathersit", y="cnt", data=df)
            plt.xlabel("weathersit")
            plt.ylabel("Total pesepeda")
            plt.title("hitung Pesepeda berdasarkan cuaca")
            plt.xticks(rotation=15, ha='right')
            plt.tight_layout()  # Adjust spacing to prevent labels from being cut off
            plt.show()
            # Data urut terbanyak penyewa berdasarkan weathersit
            st.write("Data Urut Terbanyak Penyewa Berdasarkan Cuaca")
            st.write(df.groupby(by="weathersit").nunique().sort_values(by='cnt', ascending=False))

            # Data urut terkecil penyewa berdasarkan weathersit
            st.write("Data Urut Terkecil Penyewa Berdasarkan Cuaca")
            st.write(df.groupby(by="weathersit").nunique().sort_values(by='cnt', ascending=True))
            st.write("cuaca sangat berpengaaruh terhadap peminat pengguna sepeda Ketika cuaca sangat buruk, hanya ada sedikit peminat pengguna sepeda. Ini mungkin karena mereka tidak ingin mengambil risiko terjadi sesuatu yang buruk. ini hal wajar bahwa penurunan permintaan selama cuaca buruk dan cuaca adalah faktor eksternal yang mungkin kita tidak bisa atur. Menggunakan sepeda saat cuaca buruk dapat meningkatkan risiko kecelakaan atau kerusakan pada sepeda.")

elif selected_button == "Tambahan":
            st.header("Analisis Data")
            st.write(df)
            
            # menampilkan data berdasarkan yr, mnth, season, weathersit, hum, temp, atemp, dan windspeed
            st.write("Data Berdasarkan Tahun (yr):")
            st.write(df.groupby('yr')[['cnt', 'registered', 'casual']].sum())

            st.write("Data Berdasarkan Bulan (mnth):")
            st.write(df.groupby('mnth')[['cnt', 'registered', 'casual']].sum())

            st.write("Data Berdasarkan Musim (season):")
            st.write(df.groupby('season')[['cnt', 'registered', 'casual']].sum())

            st.write("Data Berdasarkan Cuaca (weathersit):")
            st.write(df.groupby('weathersit')[['cnt', 'registered', 'casual']].sum())

            st.write("Data Berdasarkan Kelembaban (hum):")
            st.write(df.groupby('hum')[['cnt', 'registered', 'casual']].sum())

            st.write("Data Berdasarkan Suhu (temp):")
            st.write(df.groupby('temp')[['cnt', 'registered', 'casual']].sum())

            st.write("Data Berdasarkan Suhu Terasa (atemp):")
            st.write(df.groupby('atemp')[['cnt', 'registered', 'casual']].sum())

            st.write("Data Berdasarkan Kecepatan Angin (windspeed):")
            st.write(df.groupby('windspeed')[['cnt', 'registered', 'casual']].sum())


