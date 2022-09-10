import streamlit as st
import pandas as pd 
import numpy as np 
import importlib
from tkinter import N
from datetime import datetime
option = st.sidebar.selectbox(
    'Menu:',
    ('Keamanan','Kejahatan','Penanganan')
)

if option == 'Keamanan' or option == '':
    st.write("""# KEAMANAN DIGITAL """) #menampilkan halaman utama
    
    st.caption("Amateurhack \n 13 Agustus 2022")
    
    from PIL import Image
    image = Image.open("C:\streamlit\photo\pic1.jpg")
    st.image(image, caption="Sumber: patrolisiber.id")

    st.markdown('''"Ketahuilah, bahwa Indonesia menduduki peringkat **_PERTAMA_** se-Asia Tenggara dan ke 60 dunia dalam hal bahaya yang di timbulkan oleh penjelajah internet (Internet surfing)" hal ini di ungkapkan oleh perusahaan Cyber security Kapensky.''')
    st.markdown('''Pada tahun 2020, pertumbuhan pengguna teknologi digital di Indonesia meningkat tajam dibandingkan pertumbuhan jumlah penduduk, dimana penggunaan gadget yang terus meningkat dalam kehidupan sehari-hari. 
    Badan Pengkajian dan Penerapan Teknologi (BPPT) mengatakan, kemajuan Teknologi Informasi dan Komunikasi (TIK) sangat berperan dalam meningkatkan kecepatan dan efisiensi di berbagai layanan. Namun di sisi yang lain juga memberikan resiko penyalahgunaan teknologi informasi dan komunikasi dalam bentuk cyber threat untuk hal-hal yang merusak atau membahayakan. ''')

    col1, col2 = st.columns(2)
    col1.metric("Population 2000", "205.132.458 jiwa")
    col2.metric("Population 2021", "276.361.783 jiwa", '71.229.352')
    col1.metric("Pengguna internet 2000", "2.000.000 jiwa")
    col2.metric("pengguna internet 2021", "212.354.070 jiwa", "210.354.070")
    col2.metric("Penetration rate pada populasi", "76.8 %")
    st.caption("sumber : https://www.internetworldstats.com")

    st.write("""Berdasarkan laporan data anomali trafik BSSN (2021), sepanjang tahun 2020, Indonesia mengalami serangan siber mencapai angka 495,3 juta atau meningkat 41 persen dari tahun sebelumnya 2019 yang sebesar 290,3 juta. 
Anomali trafik tertinggi terjadi pada tanggal 10 desember 2020 dengan jumlah mencapai 7.311.606 anomali. 
Trojan menjadi anomali dengan jumlah tertinggi. Dimana Indonesia juga merupakan negara dengan serangan tertinggi yang menjadi tujuan dari anomali yang berasal dari negara Indonesia sendiri (dengan alamat IP Indonesia). 
Dari laporan tersebut juga dideteksi terjadinya email phishing sebanyak 2.549 kasus dengan peningkatan jumlah kasus email phishing terjadi di bulan Maret - Mei 2020, 79.439 akun yang mengalami data breach,
dan sebanyak 9.749 mengalami web defacement dimana sektor akademik menjadi sektor dengan kasus terbanyak pada tahun 2020.""")
    st.write("""Sementara pada Januari hingga Juli 2021 anomaly traffic/serangan siber telah mencapai 741,4 juta, dimana kategori anomali terbanyak yakni malware, denial of service (mengganggu ketersediaan layanan), dan trojan activity; dan tren serangan siber yang terjadi didominasi oleh serangan ransomware (malware yang meminta tebusan) dan indeks data leaks (kebocoran data). 
Dalam periode tersebut, sektor pemerintah merupakan sektor tertinggi yang mengalami kebocoran data akibat malware pencuri informasi yakni dengan sebaran 45,5%, yang kemudian disusul oleh sektor keuangan (21,8%), telekomunikasi (10,4%), penegakan hukum (10,1%), transportasi (10,1%), dan BUMN lainnya (2,1%).""")
    
elif option == 'Kejahatan':
    st.write("""## LAPORAN KEJAHATAN SIBER PADA JULI 2019 - JULI 2022""")

    from PIL import Image
    image = Image.open("C:\streamlit\photo\grafik 2.jpg")
    st.image(image, caption="Sumber: patrolisiber.id")

    st.write("""## 3 KEJAHATAN SIBER TERTINGGI""")
    st.markdown(''' 1. Email Phising''')

    from PIL import Image
    image = Image.open("C:\streamlit\photo\phising.jpg")
    st.image(image, caption="Email Phising")

    st.markdown(''' **_Phising_** adalah upaya untuk mendapatkan informasi data seseorang dengan teknik pengelabuan. 
Data yang menjadi sasaran phising adalah data pribadi (nama, usia, alamat), data akun (username dan password), 
dan data finansial (informasi kartu kredit, rekening).''')
    st.write("""**_Email Phishing_** adalah salah satu tindak kejahatan dunia maya yang bertujuan untuk mengelabui seseorang atau organisasi tertentu melalui email. 
Tujuannya, agar target memberikan informasi penting yang sifatnya rahasia atau sensitif. Umumnya, phishing dilakukan melalui email maupun website yang tampilannya menyerupai halaman login suatu website terkenal.""")
    st.write("""Email phising lebih sulit di deteksi, karena alamat email dan nama email dapat dibuat seolah-olah sama, dengan menggunakan tehnik spoofing. 
Dimana teknik spoofing biasanya berupa pengiriman pesan menggunakan alamat IP yang seolah-olah dikirim dari port computer yang aman ke suatu computer.""")
    st.markdown(''' 2. Web Defacement''') 

    from PIL import Image
    image = Image.open("C:\streamlit\photo\web defacement.jpg")
    st.image(image, caption="Web Defacement")

    st.write("**_Deface website atau web defacement_** adalah serangan cyber yang menyasar suatu website, dengan memodifikasi tampilannya baik sebagian atau seluruhnya. Serangan ini cukup **_“obvious”_**, pasalnya pelaku biasanya akan meninggalkan jejak. \n Contohnya, font website diganti, muncul iklan mengganggu, hingga perubahan konten halaman secara keseluruhan. Tidak hanya itu, **_deface website_** sering dilakukan untuk pengujian awal keamanan website. Peretas bisa saja pencurian data, dan sebagainya.")
    st.markdown(''' 3. Malware''')

    from PIL import Image
    image = Image.open("C:\streamlit\photo\malware.jpg")
    st.image(image, caption="Malware")

    st.write("""Malware adalah perangkat lunak yang dibuat dengan tujuan memasuki dan terkadang merusak sistem komputer, jaringan, atau server tanpa diketahui oleh pemiliknya. 
Istilah malware diambil dari gabungan potongan dua kata yaitu **_malicious_** “berniat jahat” dan **_software_** “perangkat lunak”. 
salah satu serangan yang diakibatkan oleh Malware ialah Indeks **_Data Leaks_** (Kebocoran Data).""")
    st.write("""Malware menjadi salah satu ancaman yang paling besar dalam insiden keamanan informasi. 
Berdasarkan riset dari Verizon Data Breach Investiogation Report 2017, aktivitas insiden yang melibatkan malware menduduki peringkat kedua. 
Pada riset tersebut juga menyebutkan bahwa aktivitas insiden malware menyebabkan kehilangan data dan kerugian finansial yang cukup signifikan. 
Malware dapat disebarkan melalui beberapa metode yaitu melalui jaringan internet, email, pesan pribadi, atau halaman situs web. Tidak hanya perangkat komputer saja, server situs web juga banyak menjadi korban dari malware.""")

elif option == 'Penanganan':
    st.write("""## CARA MELINDUNGI""")
    st.write(''' **1. Email Phising**''') 
    st.write('''* Menggunakan perangkat lunak anti phising''')
    st.write('''* Lakukan edukasi pengguna''')
    st.write('''* Hindari pengguna jaringan public''')
    st.write('''* Hati-hati dengan tautan dipersingkat''')
    st.write('''* Verifikasi kredensial ssl, waspadalah terhadap pop up''')
    st.write(''' ''')
    st.markdown(''' **2. Web Defacement**''')
    st.write("""Terdapat 2 (dua) cara bagi institusi/perorangan untuk meletakan suatu halaman web, yaitu meletakan pada server yang dikelola sendiri atau meletakan halaman webnya pada web hosting. Bagi yang meletakkan halaman webnya pada web hosting, maka apabila terjadi web deface harus melakukan koordinasi dengan pihak web hosting. 
Koordinasi ini ditujukan untuk memudahkan penanganan dari web yang telah ter-deface.""")

    st.markdown(''' **3. Malware**''')
    st.write("""Malware dapat menjadi sebab yang berbahaya untuk situs web. Tidak hanya mengganggu sistem 
    yang berjalan, malware juga dapat mencuri data-data yang penting, mengubahnya, dan bahkan mengendalikan sistem yang ada. Meskipun 
    malware sangat mudah menyebar di dalam sistem, hal itu dapat dicegah terlebih dahulu. **Caranya adalah melakukan pemindaian 
    malware secara berkala dan melakukan pengecekan jika terdapat file yang mencurigakan.**""")
