import time
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# ==========================================
# KONFIGURASI HALAMAN & TEMA VISUAL RESMI BI
# ==========================================
st.set_page_config(
    page_title="Portal Edukasi Kebanksentralan & AI Governance",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.stApp { background-color: #F4F7FB; }
.hero-banner {
    background: linear-gradient(135deg, #002D72 0%, #00509E 100%);
    padding: 24px 28px;
    border-radius: 16px;
    color: white;
    margin-bottom: 20px;
    border-bottom: 5px solid #D4AF37;
}
.hero-banner h1 { color: #FFFFFF; margin-bottom: 6px; font-size: 1.85rem; }
.hero-banner p { color: #E2E8F0; font-size: 1rem; margin: 0; }
.bi-card {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 14px;
    border-top: 5px solid #002D72;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    height: 100%;
}
.bi-card-gold { border-top: 5px solid #D4AF37; }
.bi-card-teal { border-top: 5px solid #0D9488; }
.bi-title { color: #002D72; font-weight: 700; font-size: 1.15rem; margin-bottom: 8px; }
.badge-bi {
    background-color: #D4AF37;
    color: #002D72;
    padding: 4px 12px;
    border-radius: 20px;
    font-weight: 700;
    font-size: 0.76rem;
    display: inline-block;
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR NAVIGASI
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#002D72; margin-bottom:0;'>🏛️ BANK SENTRAL RI</h2>", unsafe_allow_html=True)
    st.caption("<p style='text-align:center;'>Edukasi Kebanksentralan & AI Risk Governance</p>", unsafe_allow_html=True)
    st.divider()
    
    menu = st.radio(
        "🧭 Modul Edukasi Publik:",
        [
            "📊 1. Tiga Fungsi Utama & Indikator BI",
            "💳 2. Inovasi Sistem Pembayaran & Digital Rupiah",
            "🛡️ 3. Pelindungan Konsumen & Audit Hoaks AI",
            "🏆 4. Kuis Literasi Kebanksentralan"
        ]
    )
    
    st.divider()
    st.info("📌 **Sumber Materi:** Seluruh data indikator, pilar kebijakan, dan kanal layanan merujuk pada portal resmi Bank Indonesia (`bi.go.id`).")
    st.link_button("🌐 Kunjungi Website Resmi BI", "https://www.bi.go.id/id/default.aspx", use_container_width=True)

# ==========================================
# MODUL 1: TIGA FUNGSI UTAMA & INDIKATOR BI
# ==========================================
if menu == "📊 1. Tiga Fungsi Utama & Indikator BI":
    st.markdown("""
    <div class="hero-banner">
        <span class="badge-bi">MANDAT & KEWENANGAN BANK SENTRAL</span>
        <h1>Mencapai dan Memelihara Stabilitas Nilai Rupiah</h1>
        <p>Mengenal tiga pilar fungsi utama Bank Indonesia dalam menjaga stabilitas moneter, sistem keuangan, serta kelancaran sistem pembayaran nasional.</p>
    </div>
    """, unsafe_allow_html=True)

    # Baris Indikator Terkini dari Portal BI
    st.subheader("📈 Indikator Ekonomi & Moneter Terkini (Portal BI)")
    m1, m2, m3, m4, m5 = st.columns(5)
    m1.metric("BI-Rate (18 Nov 2026)", "6,00%", "+25 bps")
    m2.metric("Inflasi IHK (yoy)", "3,28%", "Target 2026: 2,5±1%")
    m3.metric("JISDOR (USD/IDR)", "Rp18.278", "20 Nov 2026")
    m4.metric("Cadangan Devisa", "US$ 146.765 Jt", "30 Okt 2026")
    m5.metric("NPI Triwulan III 2026", "Surplus US$ 0,1 M", "Ketahanan Eksternal Terjaga")

    st.write("")
    st.subheader("🏛️ Tiga Fungsi Utama Bank Indonesia")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="bi-card">
            <div class="bi-title">1. Kebijakan Moneter</div>
            <p style="color:#334155; font-size:0.93rem;">
            Menjaga kestabilan nilai Rupiah terhadap barang dan jasa (<b>inflasi</b>) serta terhadap mata uang negara lain (<b>nilai tukar</b>).
            </p>
            <ul style="color:#475569; font-size:0.88rem; padding-left:18px;">
                <li><b>Instrumen Utama:</b> BI-Rate (Suku Bunga Acuan), Operasi Moneter, Deposit Facility (5,25%), dan Lending Facility (6,75%).</li>
                <li><b>Indikator Acuan:</b> INDONIA, JISDOR, dan Kurs Transaksi BI.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="bi-card bi-card-gold">
            <div class="bi-title">2. Stabilitas Sistem Keuangan</div>
            <p style="color:#334155; font-size:0.93rem;">
            Menjaga ketahanan sistem keuangan nasional agar mampu bertahan terhadap gejolak ekonomi melalui <b>Kebijakan Makroprudensial</b>.
            </p>
            <ul style="color:#475569; font-size:0.88rem; padding-left:18px;">
                <li><b>Fokus Kebijakan:</b> Intermediasi perbankan yang seimbang, mitigasi risiko sistemik, dan protokol manajemen krisis.</li>
                <li><b>Program Pendukung:</b> Pengembangan UMKM, Keuangan Inklusif, Ekonomi & Keuangan Syariah, serta Keuangan Berkelanjutan.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="bi-card bi-card-teal">
            <div class="bi-title">3. Sistem Pembayaran & Pengelolaan Rupiah</div>
            <p style="color:#334155; font-size:0.93rem;">
            Memastikan sistem pembayaran berjalan aman, efisien, lancar, dan andal, serta menjamin ketersediaan Rupiah berkualitas di seluruh NKRI.
            </p>
            <ul style="color:#475569; font-size:0.88rem; padding-left:18px;">
                <li><b>Infrastruktur:</b> Sistem Pembayaran Nilai Besar (BI-RTGS) dan Ritel (BI-FAST, QRIS, Kartu Kredit Indonesia).</li>
                <li><b>Edukasi & Pengelolaan:</b> Gerakan Cinta, Bangga, Paham (CBP) Rupiah dan Proyek Garuda (Digital Rupiah).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.subheader("🧮 Simulasi Edukatif: Dampak Perubahan BI-Rate terhadap Ekonomi")
    c_sim1, c_sim2 = st.columns([1.1, 1.3])
    with c_sim1:
        skenario_rate = st.select_slider(
            "Pilih Skenario Arah Kebijakan BI-Rate:",
            options=["Penurunan BI-Rate (-25 bps)", "Tetap (6,00%)", "Kenaikan BI-Rate (+25 bps / Aktual Nov 2026)"],
            value="Kenaikan BI-Rate (+25 bps / Aktual Nov 2026)"
        )
        if "Kenaikan" in skenario_rate:
            st.info("**Tujuan Kebijakan (Pre-emptive & Forward Looking):** Memperkuat stabilitas nilai tukar Rupiah dari ketidakpastian global dan memastikan inflasi tetap terkendali dalam sasaran **2,5±1%**.")
        elif "Tetap" in skenario_rate:
            st.info("**Tujuan Kebijakan (Konsisten):** Menjaga keseimbangan antara stabilitas makroekonomi dan momentum pertumbuhan kredit perbankan.")
        else:
            st.info("**Tujuan Kebijakan (Akomodatif):** Mendorong penurunan suku bunga kredit perbankan untuk menstimulasi pembiayaan dunia usaha dan konsumsi domestik.")

    with c_sim2:
        df_suku_bunga = pd.DataFrame({
            "Instrumen Moneter BI": ["Deposit Facility", "BI-Rate (Acuan)", "Lending Facility"],
            "Suku Bunga (%)": [5.25, 6.00, 6.75]
        })
        fig_rate = px.bar(
            df_suku_bunga, x="Instrumen Moneter BI", y="Suku Bunga (%)",
            text="Suku Bunga (%)", color="Instrumen Moneter BI",
            color_discrete_sequence=["#0D9488", "#002D72", "#D4AF37"]
        )
        fig_rate.update_traces(texttemplate="%{text:.2f}%", textposition="outside")
        fig_rate.update_layout(
            yaxis_range=[0, 8], height=260, showlegend=False,
            margin=dict(l=10, r=10, t=15, b=10),
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig_rate, use_container_width=True)

# ==========================================
# MODUL 2: INOVASI SISTEM PEMBAYARAN & DIGITAL RUPIAH
# ==========================================
elif menu == "💳 2. Inovasi Sistem Pembayaran & Digital Rupiah":
    st.markdown("""
    <div class="hero-banner">
        <span class="badge-bi">BLUEPRINT SISTEM PEMBAYARAN INDONESIA (BSPI)</span>
        <h1>Transformasi Digital: QRIS TAP, Kartu Kredit Indonesia & Proyek Garuda</h1>
        <p>Mengenal inovasi sistem pembayaran domestik yang cepat, mudah, murah, aman, dan andal (CEMUMUAH) di era ekonomi digital.</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs([
        "📱 QRIS & QRIS TAP",
        "💳 Kartu Kredit Indonesia (KKI)",
        "🦅 Proyek Garuda: Digital Rupiah"
    ])

    with tab1:
        c1, c2 = st.columns([1.3, 1])
        with c1:
            st.subheader("Cara Kerja & Keamanan QRIS TAP")
            st.markdown("""
            **QRIS TAP** adalah inovasi pembayaran nirkontak (*contactless*) berbasis teknologi *Near Field Communication* (NFC) yang memungkinkan pengguna bertransaksi **cukup dengan menempelkan ponsel** ke mesin pemindai di gerbang transportasi umum atau kasir toko tanpa perlu memindai kamera secara manual.
            
            **Prosedur Verifikasi Aman Saat Bertransaksi QRIS:**
            1. **Periksa Identitas Merchant:** Pastikan nama toko/merchant yang tampil di layar ponsel sesuai dengan tempat bertransaksi.
            2. **Cek Nominal Transaksi:** Pastikan angka tagihan sudah tepat sebelum otorisasi PIN/biometrik.
            3. **Konfirmasi Status Berhasil:** Bagi pedagang (*merchant*), selalu pastikan notifikasi pembayaran masuk ke aplikasi resmi sebelum menyerahkan barang.
            """)
        with c2:
            st.warning("🛡️ **Waspada Rekayasa QRIS & Struk Digital:** Jangan pernah hanya mengandalkan tangkapan layar (*screenshot*) bukti bayar dari pembeli. Gunakan notifikasi suara/aplikasi *merchant* resmi.")
            st.info("🌐 **Standar Nasional Open API Pembayaran (SNAP):** Mendukung interkoneksi antar aplikasi pembayaran dan perbankan secara aman.")

    with tab2:
        st.subheader("Kartu Kredit Indonesia (KKI)")
        st.markdown("""
        Sebagaimana dipublikasikan pada portal utama Bank Indonesia, **Kartu Kredit Indonesia (KKI)** merupakan instrumen pembayaran dengan skema penundaan pembayaran yang diproses sepenuhnya melalui **infrastruktur sistem pembayaran domestik** (Gerbang Pembayaran Nasional / GPN).
        """)
        k1, k2, k3 = st.columns(3)
        k1.info("🏛️ **Kedaulatan Infrastruktur:** Seluruh pemrosesan transaksi dilakukan di dalam negeri melalui jaringan domestik.")
        k2.info("🏢 **Dukungan Belanja Pemerintah & UMKM:** Mempermudah belanja barang/jasa pemerintah pusat maupun daerah secara transparan dan akuntabel.")
        k3.info("💸 **Efisiensi Biaya Transaksi:** Biaya pemrosesan (*Merchant Discount Rate*) lebih kompetitif untuk mendukung ekosistem keuangan digital nasional.")

    with tab3:
        st.subheader("Proyek Garuda: Eksplorasi Digital Rupiah (CBDC)")
        st.markdown("""
        **Proyek Garuda** adalah inisiatif Bank Indonesia dalam mengeksplorasi desain **Digital Rupiah** (*Central Bank Digital Currency* / CBDC) sebagai satu-satunya alat pembayaran digital yang sah dan diterbitkan langsung oleh Bank Sentral di masa depan.
        
        **Tiga Pilar Desain Digital Rupiah:**
        * **Wholesale Digital Rupiah (w-Digital Rupiah):** Digunakan untuk transaksi nilai besar antar lembaga keuangan dan operasi moneter.
        * **Retail Digital Rupiah (r-Digital Rupiah):** Digunakan oleh masyarakat luas untuk transaksi sehari-hari layaknya uang kertas dan logam dalam bentuk digital.
        * **Keamanan & Interoperabilitas:** Dirancang agar terintegrasi dengan infrastruktur sistem pembayaran nasional serta mematuhi prinsip Anti Pencucian Uang dan Pencegahan Pendanaan Terorisme (APU-PPT).
        """)

# ==========================================
# MODUL 3: PELINDUNGAN KONSUMEN & AUDIT HOAKS AI
# ==========================================
elif menu == "🛡️ 3. Pelindungan Konsumen & Audit Hoaks AI":
    st.markdown("""
    <div class="hero-banner">
        <span class="badge-bi">PELINDUNGAN KONSUMEN & AI RISK GOVERNANCE</span>
        <h1>Detektor Pola Hoaks Kebanksentralan & Audit Respons AI</h1>
        <p>Pelindungan konsumen menjadi kunci ekonomi keuangan digital terpercaya. Uji pesan mencurigakan atau bandingkan perilaku AI tanpa tata kelola vs AI terverifikasi.</p>
    </div>
    """, unsafe_allow_html=True)

    sub_tab1, sub_tab2 = st.tabs([
        "🔍 Pemindai Indikator Hoaks & Penipuan",
        "🤖 Sandbox Audit Halusinasi AI (AI Governance)"
    ])

    with sub_tab1:
        contoh_pesan = st.selectbox(
            "Pilih contoh isu hoaks / penipuan untuk dianalisis:",
            [
                "-- Ketik Manual --",
                "Selamat! Anda mendapat dana bantuan/hibah dari Bank Indonesia sebesar Rp25 juta. Klik link berikut dan masukkan kode OTP untuk pencairan.",
                "Info darurat: Mulai besok BI-Rate naik menjadi 25% dan seluruh tabungan masyarakat di bank akan dibekukan sementara.",
                "Saya salah transfer QRIS ke warung sebelah, katanya petugas BI bisa membatalkan transaksi kalau saya kasih PIN m-banking saya."
            ]
        )

        teks_uji = st.text_area("Masukkan teks informasi yang ingin diverifikasi:", value="" if contoh_pesan == "-- Ketik Manual --" else contoh_pesan, height=100)

        if st.button("🔎 Verifikasi Indikator Risiko", type="primary"):
            if not teks_uji.strip():
                st.warning("Silakan masukkan teks informasi terlebih dahulu.")
            else:
                with st.spinner("Menganalisis pola risiko perlindungan konsumen..."):
                    time.sleep(0.4)
                low = teks_uji.lower()
                temuan = []
                if any(w in low for w in ["hibah", "hadiah", "undian", "bantuan", "cair"]):
                    temuan.append("🏛️ **Pencatutan Nama BI:** Bank Indonesia tidak menyalurkan bantuan dana/hibah langsung kepada individu maupun meminta biaya administrasi.")
                if any(w in low for w in ["otp", "pin", "password", "kata sandi"]):
                    temuan.append("🔐 **Pelanggaran Keamanan Kredensial:** Petugas Bank Indonesia maupun bank umum tidak pernah meminta PIN, OTP, atau kata sandi nasabah.")
                if any(w in low for w in ["dibekukan", "25%", "hangus", "ditarik besok"]):
                    temuan.append("📢 **Disinformasi Kebijakan Moneter:** Keputusan RDG (seperti BI-Rate 6,00%) selalu diumumkan resmi melalui Siaran Pers di `bi.go.id`.")
                if any(w in low for w in ["salah transfer", "membatalkan transaksi"]):
                    temuan.append("💳 **Prosedur Sengketa Pembayaran:** Pengaduan transaksi ritel/QRIS ditangani oleh Penyedia Jasa Pembayaran (PJP) penerbit aplikasi dengan bukti transaksi resmi.")

                if temuan:
                    st.error(f"🚨 **TERDETEKSI {len(temuan)} INDIKATOR RISIKO / HOAKS**")
                    for item in temuan:
                        st.markdown(f"- {item}")
                else:
                    st.success("✅ **TIDAK DITEMUKAN POLA PENIPUAN UMUM**")

                st.info("""
                **Kanal Resmi Layanan & Pengaduan Bank Indonesia:**
                * **Contact Center BICARA:** `131` (atau `1500131` dari luar negeri)
                * **Layanan Informasi Digital (LISA):** WhatsApp `081 131 131 131`
                * **Email Resmi:** `bicara@bi.go.id` | **Kanal Aspirasi:** `LAPOR!` & `Whistleblowing System BI`
                """)

    with sub_tab2:
        st.subheader("Perbandingan Tata Kelola AI (AI Governance) dalam Informasi Publik")
        topik_audit = st.selectbox(
            "Pilih skenario pertanyaan publik kepada sistem AI:",
            [
                "Skenario 1: Pertanyaan seputar Suku Bunga Acuan (BI-Rate) & Inflasi",
                "Skenario 2: Pertanyaan seputar Penukaran Uang Rusak / Tidak Layak Edar",
                "Skenario 3: Pertanyaan seputar Keamanan Transaksi Digital & Pelindungan Konsumen"
            ]
        )

        col_a, col_b = st.columns(2)
        if "Skenario 1" in topik_audit:
            raw_txt = "BI-Rate ditetapkan oleh Kementerian Keuangan setiap hari Senin dan saat ini berada di angka 12% untuk menaikkan harga pangan."
            gov_txt = "Berdasarkan Rapat Dewan Gubernur (RDG) Bank Indonesia tanggal 17–18 November 2026, **BI-Rate ditetapkan sebesar 6,00%** (Deposit Facility 5,25% dan Lending Facility 6,75%) untuk menjaga stabilitas nilai Rupiah dan mengarahkan inflasi tetap dalam sasaran **2,5±1%**."
        elif "Skenario 2" in topik_audit:
            raw_txt = "Uang kertas yang terbakar separuh atau robek kecil sudah tidak laku sama sekali dan harus dibuang."
            gov_txt = "Masyarakat dapat menukarkan uang Rupiah rusak/cacat di kantor Bank Indonesia atau bank yang ditunjuk. Penggantian diberikan sebesar **nilai nominal penuh** apabila fisik uang kertas masih **lebih besar dari 2/3 ukuran aslinya** dan ciri keasliannya masih dapat dikenali."
        else:
            raw_txt = "Jika mengalami penipuan online, segera kirimkan foto KTP, nomor kartu ATM, dan kode OTP ke akun media sosial yang mengaku admin BI."
            gov_txt = "Terapkan prinsip **PeKA (Peduli, Kenali, Adukan)**. Jangan pernah membagikan data pribadi maupun kredensial (PIN/OTP) kepada pihak mana pun. Laporkan kendala transaksi ke Penyedia Jasa Pembayaran terkait atau hubungi saluran resmi **BICARA 131** / **LISA (081 131 131 131)**."

        with col_a:
            st.markdown("<div class='bi-card'><b>❌ AI Tanpa Guardrails (Berisiko Halusinasi)</b></div>", unsafe_allow_html=True)
            st.write("")
            st.error(raw_txt)
        with col_b:
            st.markdown("<div class='bi-card bi-card-teal'><b>✅ Governed AI (Terverifikasi Data Resmi BI)</b></div>", unsafe_allow_html=True)
            st.write("")
            st.success(gov_txt)

# ==========================================
# MODUL 4: KUIS LITERASI KEBANKSENTRALAN
# ==========================================
elif menu == "🏆 4. Kuis Literasi Kebanksentralan":
    st.markdown("""
    <div class="hero-banner">
        <span class="badge-bi">EVALUASI PEMAHAMAN PUBLIK</span>
        <h1>Kuis Literasi Bank Sentral & Sistem Pembayaran</h1>
        <p>Uji pemahaman Anda mengenai fungsi utama Bank Indonesia, indikator moneter, inovasi QRIS TAP, dan kanal resmi pelindungan konsumen.</p>
    </div>
    """, unsafe_allow_html=True)

    skor = 0

    st.markdown("#### 1. Apa tujuan tunggal Bank Indonesia sebagaimana tercantum dalam mandatnya?")
    q1 = st.radio(
        "Pilih jawaban:",
        [
            "Menghimpun simpanan masyarakat dan menyalurkan kredit komersial.",
            "Mencapai dan memelihara kestabilan nilai Rupiah (terhadap barang/jasa dan mata uang asing).",
            "Mengatur seluruh kegiatan perdagangan saham di bursa efek."
        ],
        key="q_bi_1"
    )
    if q1 == "Mencapai dan memelihara kestabilan nilai Rupiah (terhadap barang/jasa dan mata uang asing).":
        skor += 25

    st.divider()
    st.markdown("#### 2. Teknologi apa yang digunakan pada fitur QRIS TAP untuk melakukan pembayaran?")
    q2 = st.radio(
        "Pilih jawaban:",
        [
            "Pembayaran nirkontak (contactless) cukup dengan menempelkan ponsel berbasis NFC ke mesin pemindai.",
            "Pengiriman kode rahasia melalui pesan singkat SMS.",
            "Penukaran uang logam di mesin kasir."
        ],
        key="q_bi_2"
    )
    if q2 == "Pembayaran nirkontak (contactless) cukup dengan menempelkan ponsel berbasis NFC ke mesin pemindai.":
        skor += 25

    st.divider()
    st.markdown("#### 3. Apa nama inisiatif Bank Indonesia dalam mengeksplorasi pengembangan Digital Rupiah (CBDC)?")
    q3 = st.radio(
        "Pilih jawaban:",
        [
            "Proyek Nusantara",
            "Proyek Garuda",
            "Proyek Khatulistiwa"
        ],
        key="q_bi_3"
    )
    if q3 == "Proyek Garuda":
        skor += 25

    st.divider
