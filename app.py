import streamlit as st
import pandas as pd
import plotly.express as px
import time

# Konfigurasi Halaman
st.set_page_config(
    page_title="Cerdas AI - Edukasi Publik",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS untuk mempercantik tampilan
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stAlert {
        border-radius: 10px;
    }
    .quiz-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigasi
with st.sidebar:
    st.title("🛡️ Cerdas AI")
    st.caption("Platform Edukasi Masyarakat & Manajemen Risiko AI")
    st.divider()
    
    menu = st.radio(
        "Pilih Modul Interaktif:",
        [
            "🏠 Beranda & Tren Ancaman",
            "🕵️‍♂️ Simulasi Deteksi Penipuan AI",
            "🔍 Cek Keamanan Link & Pesan",
            "🧭 Panduan Aman Menggunakan AI"
        ]
    )
    
    st.divider()
    st.info("💡 **Tips:** Gunakan aplikasi ini sebagai media edukasi interaktif untuk masyarakat umum agar terhindar dari kejahatan siber berbasis AI.")

# ==========================================
# MODUL 1: BERANDA & TREN ANCAMAN
# ==========================================
if menu == "🏠 Beranda & Tren Ancaman":
    st.title("Selamat Datang di Portal Edukasi AI Publik 👋")
    st.markdown("""
    Kecerdasan Buatan (**Artificial Intelligence / AI**) mempermudah kehidupan sehari-hari, namun juga dimanfaatkan oleh pelaku kejahatan siber. 
    Mari pelajari cara mengenali, mencegah, dan mengelola risiko AI di sekitar kita!
    """)
    
    st.subheader("📊 Tren Modus Kejahatan Digital Berbasis AI")
    
    # Data simulasi edukatif
    data_tren = pd.DataFrame({
        "Jenis Ancaman AI": [
            "Phishing Otomatis (Pesan/WA Palsu)",
            "Voice Cloning (Tiruan Suara Kerabat)",
            "Deepfake Video (Wajah Pejabat/Artis)",
            "Malware File APK Undangan/Resi"
        ],
        "Tingkat Risiko Masyarakat (%)": [85, 78, 70, 92],
        "Target Utama": ["Semua Kalangan", "Orang Tua / Lansia", "Pencari Investasi", "Pengguna Smartphone"]
    })
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig = px.bar(
            data_tren,
            x="Tingkat Risiko Masyarakat (%)",
            y="Jenis Ancaman AI",
            orientation="h",
            color="Tingkat Risiko Masyarakat (%)",
            color_continuous_scale="Reds",
            text="Tingkat Risiko Masyarakat (%)"
        )
        fig.update_layout(height=350, margin=dict(l=10, r=10, t=20, b=10))
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.markdown("### Mengapa Ini Penting?")
        st.warning("⚠️ **AI Tidak Lagi Kaku:** Dulu pesan penipuan penuh salah ketik. Kini AI membuat kalimat yang sangat meyakinkan dan sopan.")
        st.success("✅ **Kunci Utama:** Verifikasi berlapis dan jangan panik saat menerima informasi mendesak.")

# ==========================================
# MODUL 2: SIMULASI DETEKSI PENIPUAN AI
# ==========================================
elif menu == "🕵️‍♂️ Simulasi Deteksi Penipuan AI":
    st.title("🕵️‍♂️ Uji Kepekaanmu: Asli atau Buatan AI?")
    st.write("Pilih jawaban yang menurut Anda paling tepat pada 3 studi kasus di bawah ini.")
    
    skor = 0
    
    # Kasus 1
    with st.container():
        st.markdown("#### Kasus 1: Telepon Darurat Tengah Malam")
        st.info("📞 *Anda menerima telepon dari nomor tidak dikenal. Suaranya persis seperti adik/anak Anda yang sedang menangis meminta transfer uang segera karena kecelakaan, lalu telepon langsung terputus.*")
        j1 = st.radio(
            "Apa tindakan pertama yang harus dilakukan?",
            [
                "Langsung transfer ke rekening yang dikirim lewat SMS agar cepat tertolong.",
                "Tutup telepon, tarik napas, dan hubungi nomor asli kerabat tersebut atau orang di sekitarnya.",
                "Menelepon balik nomor tidak dikenal tersebut terus-menerus."
            ],
            key="q1"
        )
        if j1 == "Tutup telepon, tarik napas, dan hubungi nomor asli kerabat tersebut atau orang di sekitarnya.":
            skor += 1

    st.divider()

    # Kasus 2
    with st.container():
        st.markdown("#### Kasus 2: Video Tawaran Investasi & Giveaway")
        st.info("🎥 *Beredar video seorang tokoh terkenal menjanjikan dana bantuan tunai langsung cair jika Anda mengklik tautan di bio dan memasukkan kode OTP perbankan.*")
        j2 = st.radio(
            "Bagaimana cara mengenali bahwa video tersebut adalah Deepfake AI?",
            [
                "Gerakan bibir terkadang tidak sinkron dengan suara, kedipan mata tidak wajar, dan meminta data rahasia (OTP).",
                "Video terlihat sangat jernih sehingga pasti asli.",
                "Karena diunggah oleh akun dengan nama mirip tokoh tersebut."
            ],
            key="q2"
        )
        if j2 == "Gerakan bibir terkadang tidak sinkron dengan suara, kedipan mata tidak wajar, dan meminta data rahasia (OTP).":
            skor += 1

    st.divider()

    # Kasus 3
    with st.container():
        st.markdown("#### Kasus 3: Pesan WhatsApp Berisi File Tagihan")
        st.info("📩 *Pesan masuk: 'Yth. Bapak/Ibu, berikut rincian tagihan transaksi Anda yang mencurigakan. Silakan periksa lampiran: Rincian_Tagihan.apk'*")
        j3 = st.radio(
            "Mengapa file ini sangat berbahaya?",
            [
                "Karena ukuran filenya terlalu besar untuk HP.",
                "File berakhiran .apk adalah aplikasi installer yang bisa mencuri akses SMS/OTP di ponsel Anda.",
                "Pesan tersebut tidak menggunakan emoji."
            ],
            key="q3"
        )
        if j3 == "File berakhiran .apk adalah aplikasi installer yang bisa mencuri akses SMS/OTP di ponsel Anda.":
            skor += 1

    st.write("")
    if st.button("Periksa Hasil Evaluasi Saya", type="primary"):
        with st.spinner("Menganalisis jawaban Anda..."):
            time.sleep(0.8)
        
        st.subheader(f"Skor Anda: {skor} dari 3")
        if skor == 3:
            st.balloons()
            st.success("🎉 Luar Biasa! Anda memiliki kesadaran keamanan digital yang sangat baik terhadap rekayasa AI.")
        elif skor == 2:
            st.warning("👍 Cukup Baik! Anda sudah memahami dasar-dasarnya, namun tetap waspada pada detail teknis seperti ekstensi file (.apk) dan verifikasi suara.")
        else:
            st.error("🚨 Perlu Waspada! Kejahatan AI sangat mudah mengecoh jika kita terburu-buru. Pelajari kembali panduan di menu sebelah kiri.")

# ==========================================
# MODUL 3: CEK KEAMANAN LINK & PESAN
# ==========================================
elif menu == "🔍 Cek Keamanan Link & Pesan":
    st.title("🔍 Detektor Pola Pesan Mencurigakan")
    st.write("Tempelkan teks pesan WhatsApp/SMS atau tautan mencurigakan yang Anda terima untuk dianalisis indikator risikonya.")
    
    input_teks = st.text_area(
        "Masukkan teks pesan atau tautan di sini:",
        placeholder="Contoh: Selamat Anda menang undian Rp 50 juta! Segera klik bit.ly/klaim-sekarang dan masukkan PIN..."
    )
    
    if st.button("Analisis Risiko Pesan", type="primary"):
        if not input_teks.strip():
            st.warning("Silakan masukkan teks pesan terlebih dahulu.")
        else:
            teks_lower = input_teks.lower()
            indikator = []
            
            # Logika deteksi kata kunci berbasis aturan (Rule-Based AI Risk Scoring)
            kata_mendesak = ["segera", "darurat", "blokir", "24 jam", "hangus", "terbatas", "sekarang"]
            kata_hadiah = ["selamat", "menang", "hadiah", "undian", "gratis", "dana bantuan", "cair"]
            kata_rahasia = ["otp", "pin", "password", "kata sandi", "cvv", "nama ibu kandung"]
            ekstensi_bahaya = [".apk", "bit.ly", "tinyurl", ".exe", "http://"]
            
            if any(k in teks_lower for k in kata_mendesak):
                indikator.append("⏱️ **Manipulasi Psikologis (Urgensi):** Memaksa korban panik dan bertindak cepat tanpa berpikir.")
            if any(k in teks_lower for k in kata_hadiah):
                indikator.append("🎁 **Iming-iming Tidak Wajar:** Menawarkan keuntungan instan untuk memancing rasa penasaran.")
            if any(k in teks_lower for k in kata_rahasia):
                indikator.append("🔐 **Permintaan Data Kredensial:** Pihak resmi tidak pernah meminta PIN, Password, atau kode OTP.")
            if any(k in teks_lower for k in ekstensi_bahaya):
                indikator.append("🔗 **Tautan/File Berisiko:** Mengandung pemendek tautan tidak jelas, protokol tidak aman (http), atau file instalasi (.apk).")
            
            st.subheader("Hasil Analisis Sistem:")
            if len(indikator) >= 2:
                st.error(f"🚨 **TINGKAT RISIKO TINGGI ({len(indikator)} Indikator Terdeteksi)**")
                for item in indikator:
                    st.markdown(f"- {item}")
                st.info("**Rekomendasi:** Jangan klik tautan apa pun, jangan balas pesan, dan segera blokir pengirim.")
            elif len(indikator) == 1:
                st.warning("⚠️ **TINGKAT RISIKO SEDANG (1 Indikator Terdeteksi)**")
                st.markdown(f"- {indikator[0]}")
                st.info("**Rekomendasi:** Lakukan konfirmasi ulang melalui saluran resmi sebelum mempercayai isi pesan.")
            else:
                st.success("✅ **TIDAK DITEMUKAN POLA PENIPUAN UMUM**")
                st.caption("Catatan: Tetap gunakan akal sehat dan jangan pernah membagikan data pribadi kepada siapa pun.")

# ==========================================
# MODUL 4: PANDUAN AMAN MENGGUNAKAN AI
# ==========================================
elif menu == "🧭 Panduan Aman Menggunakan AI":
    st.title("🧭 Prinsip AI Governance untuk Masyarakat")
    st.write("Bagaimana masyarakat umum bisa memanfaatkan AI (seperti ChatGPT, Gemini, dll.) dengan aman dan bijak?")
    
    tab1, tab2, tab3 = st.tabs(["🔒 Privasi Data", "✅ Verifikasi Fakta", "⚖️ Etika Digital"])
    
    with tab1:
        st.subheader("Jangan Masukkan Data Pribadi ke AI Publik")
        st.markdown("""
        Saat menggunakan aplikasi AI gratis di internet, hindari memasukkan informasi sensitif seperti:
        * Nomor Induk Kependudukan (NIK) & Foto KTP
        * Nomor Rekening, Kartu Kredit, atau PIN
        * Dokumen rahasia pekerjaan atau data medis pribadi
        
        *Mengapa?* Data yang dimasukkan ke sistem AI publik berpotensi digunakan untuk melatih ulang model di masa depan.
        """)
        
    with tab2:
        st.subheader("Waspadai 'Halusinasi AI'")
        st.markdown("""
        AI bekerja dengan memprediksi kata yang paling masuk akal, bukan selalu berdasarkan kebenaran mutlak.
        * **Selalu Cek Ulang:** Jika AI memberikan informasi hukum, kesehatan, atau keuangan, pastikan Anda membandingkannya dengan sumber resmi pemerintah atau lembaga berwenang.
        * **Periksa Sumber:** Minta AI menyertakan referensi atau cari langsung melalui mesin pencari terpercaya.
        """)
        
    with tab3:
        st.subheader("Gunakan AI sebagai Asisten, Bukan Pengganti")
        st.markdown("""
        * Gunakan AI untuk mempercepat pekerjaan: merangkum artikel, mencari ide usaha, atau belajar bahasa baru.
        * Jangan gunakan AI untuk membuat konten hoaks, meniru identitas orang lain, atau menyebarkan ujaran kebencian.
        """)
