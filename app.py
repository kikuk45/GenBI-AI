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

/* Kartu Modern Khusus Pilar CBP Rupiah */
.cbp-modern-card {
    border-radius: 18px;
    padding: 22px 20px;
    color: #FFFFFF;
    box-shadow: 0 10px 24px rgba(0, 45, 114, 0.12);
    height: 100%;
}
.cbp-cinta {
    background: linear-gradient(145deg, #991B1B 0%, #DC2626 100%);
    border-bottom: 5px solid #FCA5A5;
}
.cbp-bangga {
    background: linear-gradient(145deg, #92400E 0%, #D97706 100%);
    border-bottom: 5px solid #FDE68A;
}
.cbp-paham {
    background: linear-gradient(145deg, #002D72 0%, #0284C7 100%);
    border-bottom: 5px solid #7DD3FC;
}
.cbp-pill {
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(6px);
    padding: 4px 12px;
    border-radius: 999px;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.5px;
    display: inline-block;
    margin-bottom: 10px;
}
.cbp-modern-title {
    font-size: 1.35rem;
    font-weight: 800;
    margin-bottom: 8px;
    color: #FFFFFF;
}
.cbp-sublist {
    background: rgba(0, 0, 0, 0.16);
    border-radius: 12px;
    padding: 12px 14px;
    margin-top: 12px;
    font-size: 0.88rem;
}

/* Kartu Visual Edukasi 5 Jangan - Rupiah Keren */
.rk-banner {
    background: linear-gradient(135deg, #002D72 0%, #004E92 60%, #0284C7 100%);
    border-radius: 20px;
    padding: 26px 30px;
    color: #FFFFFF;
    border: 2px solid #D4AF37;
    box-shadow: 0 12px 28px rgba(0, 45, 114, 0.14);
    margin-bottom: 22px;
}
.jangan-visual-card {
    background: #FFFFFF;
    border-radius: 18px;
    padding: 20px 16px;
    text-align: center;
    border-top: 6px solid #C8102E;
    box-shadow: 0 8px 20px rgba(15, 23, 42, 0.07);
    height: 100%;
}
.jangan-badge-num {
    background: #FEE2E2;
    color: #C8102E;
    font-weight: 800;
    font-size: 0.82rem;
    padding: 4px 12px;
    border-radius: 999px;
    display: inline-block;
    margin-bottom: 10px;
}
.jangan-card-title {
    color: #002D72;
    font-weight: 800;
    font-size: 1.08rem;
    margin: 10px 0 6px 0;
}
.jangan-card-desc {
    color: #475569;
    font-size: 0.86rem;
    line-height: 1.45;
    margin: 0;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# ILUSTRASI VEKTOR EDUKASI 5 JANGAN (SVG)
# ==========================================
def svg_5_jangan(jenis):
    bingkai_awal = '<svg width="115" height="115" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg"><circle cx="60" cy="60" r="54" fill="#FFF5F5" stroke="#FECACA" stroke-width="2"/>'
    bingkai_larangan = '<circle cx="60" cy="60" r="46" fill="none" stroke="#DC2626" stroke-width="6.5"/><line x1="28" y1="28" x2="92" y2="92" stroke="#DC2626" stroke-width="6.5" stroke-linecap="round"/></svg>'

    if jenis == "lipat":
        isi = '<polygon points="30,44 60,36 60,78 30,84" fill="#DBEAFE" stroke="#1E40AF" stroke-width="2.5"/><polygon points="60,36 90,46 90,86 60,78" fill="#93C5FD" stroke="#1E40AF" stroke-width="2.5"/><line x1="60" y1="36" x2="60" y2="78" stroke="#1E3A8A" stroke-width="2.5" stroke-dasharray="4,3"/><circle cx="45" cy="60" r="5" fill="#2563EB"/><circle cx="75" cy="62" r="5" fill="#2563EB"/>'
    elif jenis == "coret":
        isi = '<rect x="28" y="42" width="64" height="36" rx="4" fill="#E0F2FE" stroke="#0369A1" stroke-width="2.5"/><path d="M35 65 Q48 48, 58 63 T82 56" fill="none" stroke="#1E293B" stroke-width="2.5" stroke-linecap="round"/><polygon points="72,30 82,36 63,65 55,67 57,58" fill="#F59E0B" stroke="#92400E" stroke-width="2"/>'
    elif jenis == "stapler":
        isi = '<rect x="28" y="42" width="64" height="36" rx="4" fill="#DCFCE7" stroke="#15803D" stroke-width="2.5"/><rect x="44" y="54" width="32" height="12" rx="2" fill="#94A3B8" stroke="#334155" stroke-width="2.5"/><line x1="48" y1="54" x2="48" y2="66" stroke="#1E293B" stroke-width="2.5"/><line x1="72" y1="54" x2="72" y2="66" stroke="#1E293B" stroke-width="2.5"/>'
    elif jenis == "remas":
        isi = '<polygon points="36,44 50,34 68,38 84,48 80,72 64,84 42,80 32,62" fill="#FEF3C7" stroke="#B45309" stroke-width="2.5"/><polyline points="42,46 56,58 48,74" fill="none" stroke="#92400E" stroke-width="2"/><polyline points="72,46 60,60 74,72" fill="none" stroke="#92400E" stroke-width="2"/>'
    else:
        isi = '<rect x="28" y="44" width="64" height="34" rx="4" fill="#E0F2FE" stroke="#0284C7" stroke-width="2.5"/><path d="M46 32 C46 32, 38 44, 38 49 A8 8 0 0 0 54 49 C54 44, 46 32, 46 32 Z" fill="#38BDF8" stroke="#0369A1" stroke-width="2"/><path d="M72 48 C72 48, 65 58, 65 63 A7 7 0 0 0 79 63 C79 58, 72 48, 72 48 Z" fill="#0EA5E9" stroke="#0369A1" stroke-width="2"/>'

    return bingkai_awal + isi + bingkai_larangan

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
            "❤️ 4. Cinta, Bangga, Paham Rupiah",
            "✨ 5. Cara Merawat Rupiah (5 Jangan)",
            "🏆 6. Kuis Literasi Kebanksentralan"
        ]
    )
    
    st.divider()
    st.info("📌 **Sumber Materi:** Seluruh data indikator, pilar kebijakan, dan kampanye CBP merujuk pada portal resmi Bank Indonesia (`bi.go.id`).")
    st.link_button("🌐 Portal Merawat Rupiah BI", "https://www.bi.go.id/id/rupiah/komunikasi-merawat-rupiah/default.aspx", use_container_width=True)

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
# MODUL 4: CINTA, BANGGA, PAHAM RUPIAH
# ==========================================
elif menu == "❤️ 4. Cinta, Bangga, Paham Rupiah":
    st.markdown("""
    <div class="hero-banner">
        <span class="badge-bi">KAMPANYE NASIONAL BANK INDONESIA</span>
        <h1>Cinta, Bangga, Paham Rupiah: Rupiah Itu Kita!</h1>
        <p>Bank Indonesia mengajak seluruh masyarakat mewujudkan kecintaan, kebanggaan, dan pemahaman terhadap Rupiah demi menjaga stabilitas nilai Rupiah dan kedaulatan NKRI.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="cbp-modern-card cbp-cinta">
            <span class="cbp-pill">PILAR 01 • KEASLIAN & MERAWAT</span>
            <div class="cbp-modern-title">❤️ CINTA RUPIAH</div>
            <p style="font-size:0.92rem; line-height:1.5; margin-bottom:0;">
            Perwujudan kemampuan masyarakat untuk mengenal karakteristik dan desain Rupiah, memperlakukan Rupiah secara tepat, serta menjaga diri dari kejahatan uang palsu.
            </p>
            <div class="cbp-sublist">
                <b>3 Cinta Diwujudkan Dengan:</b><br>
                1. <b>Mengenali</b> (Unsur pengaman 3D)<br>
                2. <b>Merawat</b> (Prinsip 5 Jangan)<br>
                3. <b>Menjaga</b> (Waspada uang palsu)
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="cbp-modern-card cbp-bangga">
            <span class="cbp-pill">PILAR 02 • IDENTITAS & SIMBOL BANGSA</span>
            <div class="cbp-modern-title">🇮🇩 BANGGA RUPIAH</div>
            <p style="font-size:0.92rem; line-height:1.5; margin-bottom:0;">
            Perwujudan kemampuan masyarakat memahami Rupiah sebagai alat pembayaran yang sah, simbol kedaulatan NKRI, dan alat pemersatu bangsa dari Sabang sampai Merauke.
            </p>
            <div class="cbp-sublist">
                <b>3 Bangga Rupiah Sebagai:</b><br>
                1. <b>Simbol Kedaulatan</b> NKRI<br>
                2. <b>Alat Pembayaran yang SAH</b><br>
                3. <b>Pemersatu Bangsa</b> Indonesia
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="cbp-modern-card cbp-paham">
            <span class="cbp-pill">PILAR 03 • FUNGSI DALAM PEREKONOMIAN</span>
            <div class="cbp-modern-title">🧠 PAHAM RUPIAH</div>
            <p style="font-size:0.92rem; line-height:1.5; margin-bottom:0;">
            Perwujudan kemampuan masyarakat memahami peran Rupiah dalam peredaran uang, stabilitas ekonomi, dan fungsinya sebagai alat penyimpan nilai kemampuan.
            </p>
            <div class="cbp-sublist">
                <b>3 Paham Rupiah Dalam:</b><br>
                1. <b>Bertransaksi</b> (Tunai & Non-Tunai)<br>
                2. <b>Berbelanja</b> (Bijak & produk lokal)<br>
                3. <b>Berhemat</b> (Menabung & investasi)
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.subheader("🧭 Eksplorasi Praktik Nyata 3x3 Pilar CBP Rupiah")
    t_cinta, t_bangga, t_paham = st.tabs(["❤️ Detail 3 Cinta", "🇮🇩 Detail 3 Bangga", "🧠 Detail 3 Paham"])

    with t_cinta:
        st.markdown("""
        * **Mengenali:** Memahami karakteristik desain dan unsur pengaman Rupiah melalui metode **3D** (**Dilihat** perubahan warna benang/tinta, **Diraba** tekstur cetak intaglio yang kasar, **Diterawang** tanda air *watermark* dan *rectoverso* logo BI).
        * **Merawat:** Menjaga kualitas fisik uang layak edar dengan menerapkan **5 Jangan**: *Jangan Dilipat, Jangan Dicoret, Jangan Distapler, Jangan Diremas, dan Jangan Dibasahi*.
        * **Menjaga:** Melindungi diri dan lingkungan sekitar dari peredaran uang palsu serta segera melaporkan temuan mencurigakan kepada bank atau pihak berwenang.
        """)

    with t_bangga:
        st.markdown("""
        * **Simbol Kedaulatan:** Setiap lembar dan keping Rupiah memuat gambar pahlawan nasional, kekayaan alam, serta ragam budaya Nusantara sebagai representasi identitas bangsa merdeka.
        * **Pembayaran yang SAH:** Berdasarkan Undang-Undang Mata Uang, Rupiah wajib digunakan dalam setiap transaksi pembayaran di seluruh wilayah Negara Kesatuan Republik Indonesia (NKRI).
        * **Pemersatu Bangsa:** Menjadi satu-satunya alat tukar yang menyatukan aktivitas ekonomi masyarakat di seluruh pulau, dari perkotaan hingga wilayah 3T (Terdepan, Terluar, Tertinggal).
        """)

    with t_paham:
        st.markdown("""
        * **Bertransaksi:** Menggunakan instrumen pembayaran tunai maupun digital (seperti QRIS dan BI-FAST) secara bijak, aman, dan sesuai peruntukan.
        * **Berbelanja:** Berbelanja secara rasional sesuai kebutuhan (tidak *panic buying* agar inflasi tetap terjaga) serta mengutamakan produk dalam negeri/UMKM.
        * **Berhemat:** Mengelola keuangan pribadi dengan menyisihkan pendapatan untuk menabung dan berinvestasi pada instrumen keuangan yang legal dan diawasi otoritas.
        """)

    st.info("🎬 **Seri Kampanye Edukasi CBP Bank Indonesia:** *Rupiah Itu Kita* • *Cinta-Bangga-Paham Rupiah: Dimulai dari Kita* • *Kenali Rupiah, Jelajahi Indonesia dalam Genggamanmu*")

# ==========================================
# MODUL 5: CARA MERAWAT RUPIAH - 5 JANGAN (VISUAL EDUKASI)
# ==========================================
elif menu == "✨ 5. Cara Merawat Rupiah (5 Jangan)":
    st.markdown("""
    <div class="rk-banner">
        <span class="badge-bi">KOMUNIKASI MERAWAT RUPIAH • BANK INDONESIA</span>
        <h1 style="color:#FFFFFF; margin:4px 0 8px 0; font-size:1.95rem;">
            Jaga dan Rawat Uang Rupiah Kertas dalam Kondisi yang Baik
        </h1>
        <p style="color:#E0F2FE; font-size:1.02rem; margin:0;">
            Wujudkan gerakan <b style="color:#FDE047;">RUPIAH KEREN</b> dengan menerapkan <b>5 Jangan</b> agar uang Rupiah tetap bersih, mudah dikenali keasliannya, dan layak edar.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🖼️ Infografis Edukasi 5 Jangan Merawat Uang Rupiah")

    data_5j = [
        {
            "no": "LARANGAN #1",
            "kode": "lipat",
            "judul": "1. Jangan Dilipat",
            "desc": "Simpan uang kertas dalam posisi rapi memanjang di dompet agar serat kertas tidak patah dan benang pengaman tetap utuh."
        },
        {
            "no": "LARANGAN #2",
            "kode": "coret",
            "judul": "2. Jangan Dicoret",
            "desc": "Hindari menulis catatan atau mencoret uang kertas dengan tinta/spidol agar desain dan unsur pengaman tidak tertutup."
        },
        {
            "no": "LARANGAN #3",
            "kode": "stapler",
            "judul": "3. Jangan Distapler",
            "desc": "Gunakan pita pengikat uang (ban uang) atau karet, bukan kawat stapler yang melubangi dan merobek lembaran Rupiah."
        },
        {
            "no": "LARANGAN #4",
            "kode": "remas",
            "judul": "4. Jangan Diremas",
            "desc": "Meremas uang membuat permukaan cetak intaglio kusut sehingga tekstur kasarnya sulit diraba saat pengecekan 3D."
        },
        {
            "no": "LARANGAN #5",
            "kode": "basah",
            "judul": "5. Jangan Dibasahi",
            "desc": "Jauhkan uang dari air, cairan kimia, maupun tempat lembap agar kertas tidak lapuk, luntur, atau ditumbuhi jamur."
        }
    ]

    cols_5j = st.columns(5)
    for col, item in zip(cols_5j, data_5j):
        with col:
            st.markdown(
                f'<div class="jangan-visual-card">'
                f'<span class="jangan-badge-num">{item["no"]}</span>'
                f'<div>{svg_5_jangan(item["kode"])}</div>'
                f'<div class="jangan-card-title">{item["judul"]}</div>'
                f'<p class="jangan-card-desc">{item["desc"]}</p>'
                f'</div>',
                unsafe_allow_html=True
            )

    st.write("")
    st.divider()

    c_chk1, c_chk2 = st.columns([1.3, 1])
    with c_chk1:
        st.subheader("✅ Tantangan Kebiasaan #RupiahKeren (Self-Check)")
        chk1 = st.checkbox("1. Saya menyimpan uang kertas memanjang rapi di dompet tanpa melipatnya.")
        chk2 = st.checkbox("2. Saya tidak pernah mencoret atau menulis di atas uang kertas.")
        chk3 = st.checkbox("3. Saya tidak menstapler bundel uang kertas.")
        chk4 = st.checkbox("4. Saya tidak meremas uang kertas saat menyimpannya di saku.")
        chk5 = st.checkbox("5. Saya menjaga uang tetap kering dan jauh dari air.")

    with c_chk2:
        total_5j = sum([chk1, chk2, chk3, chk4, chk5])
        persen_5j = int((total_5j / 5) * 100)
        st.subheader("📊 Skor Kepedulian Fisik Rupiah")
        st.progress(persen_5j / 100)
        st.metric("Skor Komitmen 5 Jangan", f"{persen_5j}%", f"{total_5j} dari 5 kebiasaan diterapkan")
        if total_5j == 5:
            st.success("🌟 **DUTAKU RUPIAH KEREN!** Seluruh prinsip **5 Jangan** telah Anda terapkan dengan sempurna.")
        else:
            st.info("💡 Centang kelima kebiasaan di samping untuk mengukur komitmen Anda merawat Rupiah.")

# ==========================================
# MODUL 6: KUIS LITERASI KEBANKSENTRALAN
# ==========================================
elif menu == "🏆 6. Kuis Literasi Kebanksentralan":
    st.markdown("""
    <div class="hero-banner">
        <span class="badge-bi">EVALUASI PEMAHAMAN PUBLIK</span>
        <h1>Kuis Literasi Bank Sentral, CBP Rupiah & Sistem Pembayaran</h1>
        <p>Uji pemahaman Anda mengenai fungsi utama Bank Indonesia, pilar Cinta Bangga Paham Rupiah, prinsip 5 Jangan, serta inovasi QRIS TAP.</p>
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
        skor += 20

    st.divider()
    st.markdown("#### 2. Dalam kampanye CBP Rupiah Bank Indonesia, pilar '3 Cinta' diwujudkan melalui tindakan...")
    q2 = st.radio(
        "Pilih jawaban:",
        [
            "Mengenali, Merawat, dan Menjaga Rupiah.",
            "Bertransaksi, Berbelanja, dan Berhemat.",
            "Simbol Kedaulatan, Pembayaran yang Sah, dan Pemersatu Bangsa."
        ],
        key="q_bi_2"
    )
    if q2 == "Mengenali, Merawat, dan Menjaga Rupiah.":
        skor += 20

    st.divider()
    st.markdown("#### 3. Manakah urutan prinsip '5 Jangan' dalam kampanye Merawat Uang Rupiah Kertas (Rupiah Keren)?")
    q3 = st.radio(
        "Pilih jawaban:",
        [
            "Jangan Dilipat, Jangan Dicoret, Jangan Distapler, Jangan Diremas, Jangan Dibasahi.",
            "Jangan Disimpan, Jangan Dibelanjakan, Jangan Ditukar, Jangan Dilihat, Jangan Diraba.",
            "Jangan Diterawang, Jangan Ditransfer, Jangan Ditabung, Jangan Dihitung, Jangan Dibawa."
        ],
        key="q_bi_3"
    )
    if q3 == "Jangan Dilipat, Jangan Dicoret, Jangan Distapler, Jangan Diremas, Jangan Dibasahi.":
        skor += 20

    st.divider()
    st.markdown("#### 4. Teknologi apa yang digunakan pada fitur QRIS TAP untuk melakukan pembayaran?")
    q4 = st.radio(
        "Pilih jawaban:",
        [
            "Pembayaran nirkontak (contactless) cukup dengan menempelkan ponsel berbasis NFC ke mesin pemindai.",
            "Pengiriman kode rahasia melalui pesan singkat SMS.",
            "Penukaran uang logam di mesin kasir."
        ],
        key="q_bi_4"
    )
    if q4 == "Pembayaran nirkontak (contactless) cukup dengan menempelkan ponsel berbasis NFC ke mesin pemindai.":
        skor += 20

    st.divider()
    st.markdown("#### 5. Berapa nomor layanan resmi Contact Center Bank Indonesia (BICARA) untuk informasi dan pengaduan konsumen?")
    q5 = st.radio(
        "Pilih jawaban:",
        [
            "131",
            "112",
            "147"
        ],
        key="q_bi_5"
    )
    if q5 == "131":
        skor += 20

    st.write("")
    if st.button("🎯 Periksa Skor Literasi Saya", type="primary"):
        st.subheader(f"Skor Akhir Anda: {skor} / 100")
        if skor == 100:
            st.balloons()
            st.success("🏅 **SEMPURNA (100/100)!** Anda memahami fungsi utama Bank Indonesia, pilar Cinta Bangga Paham Rupiah, prinsip 5 Jangan, serta inovasi sistem pembayaran.")
        elif skor >= 80:
            st.info("🥈 **SANGAT BAIK!** Sebagian besar konsep kebanksentralan dan CBP Rupiah telah Anda kuasai dengan tepat.")
        else:
            st.warning("📘 **TERUS BELAJAR!** Silakan tinjau kembali ringkasan materi pada modul sebelumnya sebelum mengulang kuis.")
