from matplotlib import pyplot as plt
import pandas as pd
import streamlit as st

# Menu utama
menu_utama = st.sidebar.radio("Menu Utama", ["Beranda", "Data Grafik", "Tentang"])

if menu_utama == "Beranda":
    st.title('Aplikasi Streamlit Ujian Akhir Semester')
    st.write("Selamat datang di halaman beranda. Didalam aplikasi ini kami mempunyai 3 jenis data yang berbeda yang nanti nya dapat diakses dengan mudah, diantaranya:")
    st.write("1. Data MLBB Heroes:")
    image = st.image('hero.jpg')
    st.write("2. Data MPL ID Season 10:")
    image = st.image('mpl.jpg')
    st.write("3. Data Rice Production Indonesia")
    image = st.image('rice.jpg')

elif menu_utama == "Data Grafik":
    submenu_tentang = st.sidebar.radio("Pilih Submenu", ["Data Mlbb", "Data MPL", "Rice Production Indonesia"])

    if submenu_tentang == "Data Mlbb":
        st.title('Data Grafik Mlbb')
        st.write("Tentang Data Grafik Mlbb")
        df1=pd.read_csv('Mlbb_Heroes.csv')
        st.write(df1)

# Memungkinkan pengguna untuk memilih data yang ingin ditampilkan
        data_terpilih = st.selectbox("Pilih Data Hero:", df1['Name'].unique())

# Filter data berdasarkan pilihan pengguna
        data_filtered = df1[df1['Name'] == data_terpilih]

# Membuat grafik batang "Menang" dan "Kalah" berdasarkan data yang dipilih
        fig, ax = plt.subplots(figsize=(8, 6))
        bars = ax.bar(['Esport_Wins', 'Esport_Loss'], [data_filtered['Esport_Wins'].values[0], data_filtered['Esport_Loss'].values[0]], color=['blue', 'red'])

# Menambahkan label angka pada setiap bar
        for bar in bars:
                height = bar.get_height()
                ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

        ax.set_xlabel('Status')
        ax.set_ylabel('Jumlah')
        ax.set_title(f'Grafik Menang dan Kalah untuk Data: {data_terpilih}')
# Menampilkan grafik dalam aplikasi Streamlit
        st.pyplot(fig) 

        # Membuat grafik batang "Menang" dan "Kalah" berdasarkan data yang dipilih
        fig, ax = plt.subplots(figsize=(8, 6))
        bars = ax.bar(['HP'], [data_filtered['Hp'].values[0]], color=['red'])

# Menambahkan label angka pada setiap bar
        for bar in bars:
                height = bar.get_height()
                ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 2),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

        ax.set_xlabel('Status')
        ax.set_ylabel('Jumlah')
        ax.set_title(f'Grafik Menang dan Kalah untuk Data: {data_terpilih}')
        st.pyplot(fig)


        st.write("Visi dari aplikasi kami adalah...")

    elif submenu_tentang == "Data MPL":
        st.title('Data Grafik MPL ID S10')
        st.write("Tentang Data Grafik MPL ID S10")
        df2=pd.read_csv('MPL_ID_S10.csv')
        st.write(df2)
        selected_heroes = st.multiselect('Pilih hero untuk ditampilkan:', df2['Hero'].unique())
# Filter data berdasarkan pilihan hero
        filtered_data = df2[df2['Hero'].isin(selected_heroes)]

# Buat grafik batang
        fig, ax = plt.subplots(figsize=(10, 6))

# Iterate through selected heroes and create bar plots
        for hero in selected_heroes:
                hero_data = filtered_data[filtered_data['Hero'] == hero]
                ax.bar(hero_data['T_wins'], label=f'{hero} (Win)', alpha=0.7, height = 20)
                ax.bar(hero_data['T_lose'], label=f'{hero} (Lose)', alpha=0.7, height = 17.5)
        ax.set_xlabel('Jumlah Menang dan Kalah')
        ax.set_ylabel('Tinggi Grafik')
        ax.set_title('Grafik Kemenangan dan Kekalahan Hero')
        ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Menampilkan grafik dalam aplikasi Streamlit
        st.pyplot(fig)


    elif submenu_tentang == "Rice Production Indonesia":
        st.title('Data Grafik Rice Production Indonesia')
        st.write("Tentang Data Grafik Rice Production Indonesia")
        df3=pd.read_csv('Rice Production Indonesia 2020-2022.csv')
        st.write(df3)
        data_grouped = df3.groupby(['Year'])[['Production.(ton)']].max()

# Menampilkan hasil panen tertinggi per tahun   
        st.markdown(f"<p style='font-size: 15px;'>Tabel Tahun dan Hasil Produksi</h2>", unsafe_allow_html=True)
        st.write(data_grouped)
        st.markdown(f"<p style='font-size: 15px;'>Menurut Tabel diatas maka dapat Di jelaskan bahwa Jawa Timur merupkan Provinsi yang memili produksi tertinggi selama 3 tahun kemarin</h2>", unsafe_allow_html=True)
        plt.figure(figsize=(10, 6))
        color = 'orange'
        plt.bar(df3['Provinsi'].astype(str), df3['Production.(ton)'], color=color)
        plt.xlabel('Provinsi')
        plt.ylabel('Production.(ton)')
        plt.title('Grafik Hasil Panen Berdasarkan Provinsi dan Tahun 2020-2022')
        plt.xticks(rotation=40, ha='right')
# Menampilkan grafik dalam aplikasi Streamlit
        st.pyplot(plt)
        st.write("Dari data grafik yang ditampilkan diatas dapat diketahui Jawa Timur memiliki hasil produksi dari tahun 2020 - 2022 paling tinggi daripada Provinsi - Provinsi yang lain ")
        
        provinsi_yang_tersedia = df3['Provinsi'].unique()
        provinsi_yang_dipilih = st.multiselect('Pilih Provinsi', provinsi_yang_tersedia)

# Menentukan kolom tahun sebagai indeks
        df3.set_index('Year', inplace=True)

# Membuat grafik garis untuk provinsi-provinsi yang dipilih
        plt.figure(figsize=(10, 6))

        for provinsi in provinsi_yang_dipilih:
                data_provinsi = df3[df3['Provinsi'] == provinsi]
                plt.plot(data_provinsi.index, data_provinsi['Productivity(kw/ha)'], marker='o', linestyle='-', label=provinsi)

# Menambahkan label sumbu
        plt.xlabel('Tahun')
        plt.ylabel('Produktivitas')
# Menambahkan legenda untuk provinsi
        plt.legend()
# Menampilkan grafik di Streamlit
        plt.grid(True)
        st.pyplot(plt)
# Menambahkan grid ke grafik
        
        st.write("Sejarah aplikasi kami dimulai pada tahun...")

elif menu_utama == "Tentang":
    st.title('Tentang Aplikasi')
    st.write("Aplikasi streamlit ini menampilkan 3 jenis data yang berbeda, kemudian data tersebut ditampilkan dalam sebuah grafik yang nantinya agar mudah dibaca. Data yang ditampilkan dalam aplikasi streamlit ini diantaranya Data Mlbb, Data MPL, dan Data Rice Production Indonesia.")
