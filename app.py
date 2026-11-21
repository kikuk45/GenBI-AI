import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import time

# ==========================================
# KONFIGURASI HALAMAN & TEMA VISUAL
# ==========================================
st.set_page_config(
    page_title="CBP Rupiah & AI Guard - Edukasi Kebanksentralan",
    page_icon="🇮🇩",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS bertema Biru Navy & Emas (Identitas Kebanksentralan)
st.markdown("""
    <style>
    /* Latar Belakang Utama */
    .stApp {
        background-color: #F4F7FB;
    }
    
    /* Header Banner */
    .hero-banner {
        background: linear-gradient(135deg, #002D72 0%, #00509E 100%);
        padding: 28px 32px;
        border-radius: 16px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 8px 20px rgba(0, 45, 114, 0.15);
        border-bottom: 5px solid #D4AF37;
    }
    .hero-banner h1 {
        color: #FFFFFF;
        margin-bottom: 8px;
        font-size: 2.1rem;
    }
    .hero-banner p {
        color: #E2E8F0;
        font-size: 1.05rem;
        margin: 0;
    }

    /* Kartu Pilar CBP */
    .cbp-card {
        background-color: #FFFFFF;
        padding: 22px;
        border-radius: 14px;
        border-top: 5px solid #002D72;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        height: 100%;
        transition: transform 0.2s;
    }
    .cbp-card-gold {
        border-top: 5px solid #D4AF37;
    }
    .cbp-card-red {
        border-top: 5px solid #C8102E;
    }
    .cbp-title {
        color: #002D72;
        font-weight: 700;
        font-size: 1.25rem;
        margin-bottom: 10px;
    }

    /* Badge & Pill */
    .badge-bi {
        background-color: #D4AF37;
        color: #002D72;
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.8rem;
        display: inline-block;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR NAVIGASI
# ==========================================
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 10px 0;">
            <h2 style="color: #002D72; margin-bottom: 0;">🇮🇩 CBP RUPIAH</h2>
            <p style="color: #64748B; font-size: 0.85rem;">Smart Education & AI Risk Governance</p>
        </div>
    """, unsafe_allow_html=True)
    st.divider()
    
    menu = st.radio(
        "🧭 Navigasi Edukasi:",
        [
            "🏛️ Beranda & Pilar CBP Rupiah",
            "🔍 Asisten Cek Keaslian (3D) & AI",
            "🛡️ Simulasi Penipuan Digital & QRIS",
            "🏆 Kuis Duta CBP & Kebanksentralan"
        ]
    )
    
    st.divider()
    st.markdown("""
        <div style="background-color: #EBF3FA; padding: 14px; border-radius: 10px; border-left: 4px solid #002D72;">
            <small style="color: #002D72;">
            <b>Integrasi AI Management:</b><br>
            Menggunakan sistem pemindaian berbasis aturan (<i>Rule-Based AI</i>) untuk membantu masyarakat mengenali ciri keaslian uang dan mencegah kejahatan finansial digital.
            </small>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# MODUL 1: BERANDA & PILAR CBP RUPIAH
# ==========================================
if menu == "🏛️ Beranda & Pilar CBP Rupiah":
    st.markdown("""
        <div class="hero-banner">
            <span class="badge-bi">EDUKASI PUBLIK KEBANKSENTRALAN</span>
            <h1>Cinta, Bangga, Paham Rupiah di Era Kecerdasan Buatan</h1>
            <p>Mengenal Rupiah sebagai simbol kedaulatan negara sekaligus membentengi masyarakat dari risiko pemalsuan & penipuan keuangan berbasis AI.</p>
        </div>
    """, unsafe_allow_html=True)

    # 3 Pilar CBP dalam Kartu Visual
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="cbp-card cbp-card-red">
                <div class="cbp-title">❤️ CINTA RUPIAH</div>
                <p style="color: #334155; font-size: 0.95rem;">
                Wujud kemampuan masyarakat untuk <b>Mengenali</b> karakteristik dan desain Rupiah, <b>Merawat</b> Rupiah dengan baik (5 Jangan), serta <b>Menjaga</b> diri dari kejahatan uang palsu.
                </p>
                <hr style="border-color: #F1F5F9;">
                <small style="color: #C8102E; font-weight: 600;">Kunci: 3D (Dilihat, Diraba, Diterawang) & 5 Jangan</small>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="cbp-card cbp-card-gold">
                <div class="cbp-title">🇮🇩 BANGGA RUPIAH</div>
                <p style="color: #334155; font-size: 0.95rem;">
                Wujud kemampuan masyarakat memahami Rupiah sebagai <b>Alat Pembayaran yang Sah</b>, <b>Simbol Kedaulatan NKRI</b>, dan <b>Alat Pemersatu Bangsa</b> dari Sabang sampai Merauke.
                </p>
                <hr style="border-color: #F1F5F9;">
                <small style="color: #B45309; font-weight: 600;">Kunci: Wajib digunakan di seluruh wilayah NKRI</small>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="cbp-card">
                <div class="cbp-title">🧠 PAHAM RUPIAH</div>
                <p style="color: #334155; font-size: 0.95rem;">
                Wujud kemampuan masyarakat memahami peran Rupiah dalam <b>Peredaran Uang</b>, <b>Stabilitas Ekonomi (Inflasi)</b>, serta perilaku <b>Berbelanja Bijak & Berinvestasi</b>.
                </p>
                <hr style="border-color: #F1F5F9;">
                <small style="color: #002D72; font-weight: 600;">Kunci: Belanja sesuai kebutuhan & produk dalam negeri</small>
            </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.subheader("📈 Mengapa AI Management Penting dalam Menjaga Rupiah?")
    
    c1, c2 = st.columns([1.4, 1])
    with c1:
        df_risiko = pd.DataFrame({
            "Kategori Ancaman": [
                "Rekayasa Bukti Transfer Palsu (Edit AI)",
                "Manipulasi QRIS Palsu di Tempat Umum",
                "Hoaks Kebijakan Moneter / Redenominasi",
                "Peredaran Uang Palsu Konvensional"
            ],
            "Tingkat Kerentanan Masyarakat": [88, 82, 79, 65]
        })
        fig = px.bar(
            df_risiko,
            x="Tingkat Kerentanan Masyarakat",
            y="Kategori Ancaman",
            orientation="h",
            color="Tingkat Kerentanan Masyarakat",
            color_continuous_scale=["#00509E", "#002D72", "#C8102E"],
            text="Tingkat Kerentanan Masyarakat"
        )
        fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            height=300,
            margin=dict(l=10, r=10, t=10, b=10),
            coloraxis_showscale=False
        )
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        st.info("💡 **Peran Tata Kelola AI (AI Governance):**\n\nPerkembangan *Generative AI* memudahkan pelaku kejahatan membuat struk transfer palsu, suara tiruan pejabat bank, hingga hoaks uang baru. Edukasi CBP membantu masyarakat melakukan **verifikasi berlapis** sebelum bertransaksi.")
        st.warning("🚫 **Ingat Prinsip 5 Jangan Merawat Rupiah:**\n1. Jangan Dilipat\n2. Jangan Dicoret\n3. Jangan Distapler\n4. Jangan Diremas\n5. Jangan Dibasahi")

# ==========================================
# MODUL 2: ASISTEN CEK KEASLIAN (3D) & AI
# ==========================================
elif menu == "🔍 Asisten Cek Keaslian (3D) & AI":
    st.markdown("""
        <div class="hero-banner">
            <span class="badge-bi">SISTEM PENDUKUNG KEPUTUSAN</span>
            <h1>Simulator Inspeksi Keaslian Uang Rupiah (Metode 3D)</h1>
            <p>Pilih ciri-ciri fisik yang Anda temukan pada uang kertas Rupiah Tahun Emisi 2022 untuk menghitung indeks keasliannya.</p>
        </div>
    """, unsafe_allow_html=True)

    col_input, col_gauge = st.columns([1.3, 1])

    with col_input:
        st.subheader("📋 Checklist Pemeriksaan Fisik")
        
        pecahan = st.selectbox(
            "Pilih Pecahan Uang Kertas yang Diperiksa:",
            ["Rp100.000 (TE 2022)", "Rp50.000 (TE 2022)", "Rp20.000 (TE 2022)", "Rp10.000 (TE 2022)"]
        )

        st.markdown("**1. Dilihat (Perubahan Warna & Benang Pengaman)**")
        c_lihat1 = st.checkbox("Warna tinta perisai/bunga berubah warna saat dilihat dari sudut berbeda (Color Shifting).")
        c_lihat2 = st.checkbox("Terdapat benang pengaman seperti dianyam yang berubah warna.")

        st.markdown("**2. Diraba (Tekstur Cetak Intaglio)**")
        c_raba1 = st.checkbox("Terasa kasar saat diraba pada gambar utama pahlawan dan tulisan 'Bank Indonesia'.")
        c_raba2 = st.checkbox("Terdapat kode tunanetra (Blind Code) berupa garis-garis kasar di sisi kanan/kiri uang.")

        st.markdown("**3. Diterawang (Watermark & Rectoverso)**")
        c_terawang1 = st.checkbox("Terlihat tanda air (Watermark) gambar pahlawan dan ornamen electrotype saat diterawang ke cahaya.")
        c_terawang2 = st.checkbox("Logo BI (Rectoverso) terlihat utuh dan saling mengisi sempurna dari sisi depan & belakang.")

        checks = [c_lihat1, c_lihat2, c_raba1, c_raba2, c_terawang1, c_terawang2]
        skor_persen = int((sum(checks) / len(checks)) * 100)

    with col_gauge:
        st.subheader("📊 Indeks Keaslian Sistem")
        
        # Gauge Chart dengan Plotly
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=skor_persen,
            number={'suffix': "%", 'font': {'color': '#002D72', 'size': 44}},
            title={'text': f"Status Verifikasi ({pecahan.split()[0]})", 'font': {'size': 16, 'color': '#334155'}},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#002D72"},
                'bar': {'color': "#002D72"},
                'bgcolor': "white",
                'steps': [
                    {'range': [0, 40], 'color': "#FECACA"},
                    {'range': [40, 85], 'color': "#FDE68A"},
                    {'range': [85, 100], 'color': "#BBF7D0"}
                ],
                'threshold': {
                    'line': {'color': "#C8102E", 'width': 4},
                    'thickness': 0.75,
                    'value': 100
                }
            }
        ))
        fig_gauge.update_layout(height=300, margin=dict(l=20, r=20, t=40, b=10), paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_gauge, use_container_width=True)

        if skor_persen == 100:
            st.success("✅ **TERVERIFIKASI ASLI:** Seluruh unsur pengaman 3D terpenuhi dengan sempurna.")
        elif skor_persen >= 50:
            st.warning("⚠️ **PERLU PEMERIKSAAN LANJUT:** Beberapa unsur pengaman belum dicentang atau kondisi uang sudah sangat lusuh. Gunakan sinar UV atau tanyakan ke bank terdekat.")
        else:
            st.error("🚨 **DIRAGUKAN KEASLIANNYA:** Unsur pengaman utama tidak ditemukan. Jangan gunakan untuk bertransaksi dan laporkan ke kantor Bank Indonesia / perbankan terdekat.")

# ==========================================
# MODUL 3: SIMULASI PENIPUAN DIGITAL & QRIS
# ==========================================
elif menu == "🛡️ Simulasi Penipuan Digital & QRIS":
    st.markdown("""
        <div class="hero-banner">
            <span class="badge-bi">PROTEKSI KONSUMEN & AI RISK</span>
            <h1>Detektor Pola Penipuan Pembayaran Digital & Hoaks Rupiah</h1>
            <p>Uji pesan mencurigakan seputar transaksi QRIS, tautan bantuan Bank Indonesia, atau bukti transfer digital menggunakan mesin analisis pola.</p>
        </div>
    """, unsafe_allow_html=True)

    st.write("Masukkan teks pesan WhatsApp/SMS, deskripsi transaksi, atau berita berantai terkait keuangan:")
    
    contoh_pilihan = st.selectbox(
        "Atau pilih contoh kasus untuk diuji:",
        [
            "-- Ketik Manual --",
            "Selamat! Anda terpilih menerima dana hibah Bank Indonesia Rp 25.000.000. Segera klik bit.ly/klaim-bi-2026 dan masukkan kode OTP m-banking Anda.",
            "Kak, ini bukti transfer pembelian barangnya sudah saya kirim ya (gambar terlihat buram di bagian tanggal & jam, dan saldo mutasi rekening belum bertambah).",
            "Info valid: Mulai besok uang pecahan Rp 100.000 lama ditarik dan tidak berlaku lagi, segera tukarkan lewat link berikut."
        ]
    )

    teks_default = "" if contoh_pilihan == "-- Ketik Manual --" else contoh_pilihan
    input_pesan = st.text_area("Teks Pesan / Informasi:", value=teks_default, height=110)

    if st.button("🔍 Analisis Risiko Sekarang", type="primary"):
        if not input_pesan.strip():
            st.warning("Silakan masukkan teks pesan atau pilih contoh kasus terlebih dahulu.")
        else:
            with st.spinner("Memindai indikator rekayasa sosial & risiko AI..."):
                time.sleep(0.6)

            teks_low = input_pesan.lower()
            temuan = []

            if any(k in teks_low for k in ["hibah", "undian", "hadiah", "bantuan", "gratis", "cair"]):
                temuan.append("🏛️ **Pencatutan Nama Institusi:** Bank Indonesia tidak pernah menyalurkan dana hibah/hadiah langsung kepada individu melalui pesan pribadi atau tautan.")
            if any(k in teks_low for k in ["otp", "pin", "password", "kata sandi", "cvv"]):
                temuan.append("🔐 **Pencurian Kredensial:** Meminta kode rahasia perbankan (OTP/PIN) adalah ciri mutlak kejahatan siber.")
            if any(k in teks_low for k in ["bit.ly", "tinyurl", "klik", "link", ".apk", "http://"]):
                temuan.append("🔗 **Tautan Berbahaya (Phishing/Malware):** Berpotensi mengarahkan ke situs palsu atau mengunduh aplikasi pencuri data.")
            if any(k in teks_low for k in ["buram", "mutasi", "bukti transfer", "edit"]):
                temuan.append("🖼️ **Manipulasi Bukti Transaksi (AI Image Editing):** Selalu cek mutasi rekening secara mandiri di aplikasi mobile banking, jangan hanya percaya gambar struk.")
            if any(k in teks_low for k in ["tidak berlaku", "ditarik", "redenominasi", "uang baru"]):
                temuan.append("📢 **Indikasi Disinformasi/Hoaks Rupiah:** Pencabutan uang Rupiah selalu diumumkan secara resmi melalui situs bi.go.id dan media massa nasional dengan masa tenggang penukaran bertahun-tahun.")

            st.subheader("Hasil Evaluasi Risiko:")
            if temuan:
                st.error(f"🚨 **TERDETEKSI {len(temuan)} INDIKATOR PENIPUAN / HOAKS**")
                for t in temuan:
                    st.markdown(f"- {t}")
                st.info("📞 **Layanan Pengaduan Resmi:** Hubungi Contact Center Bank Indonesia (**BICARA 131**) untuk memverifikasi kebenaran informasi seputar kebanksentralan.")
            else:
                st.success("✅ **TIDAK DITEMUKAN POLA ANCAMAN UMUM**")
                st.caption("Tetap terapkan prinsip PeKA (Peduli, Kenali, Adukan) dalam setiap transaksi digital maupun tunai.")

# ==========================================
# MODUL 4: KUIS DUTA CBP & KEBANKSENTRALAN
# ==========================================
elif menu == "🏆 Kuis Duta CBP & Kebanksentralan":
    st.markdown("""
        <div class="hero-banner">
            <span class="badge-bi">EVALUASI INTERAKTIF</span>
            <h1>Tantangan Duta Cinta, Bangga, Paham Rupiah</h1>
            <p>Jawab 4 pertanyaan berikut untuk menguji pemahaman Anda tentang peran Bank Indonesia, QRIS, dan pengelolaan Rupiah.</p>
        </div>
    """, unsafe_allow_html=True)

    skor = 0

    with st.container():
        st.markdown("#### 1. Apa fungsi utama Bank Indonesia sebagaimana diamanatkan undang-undang?")
        q1 = st.radio(
            "Pilih jawaban:",
            [
                "Menghimpun dana tabungan masyarakat dan menyalurkan kredit usaha.",
                "Mencapai dan memelihara kestabilan nilai Rupiah (inflasi dan nilai tukar).",
                "Mengawasi seluruh kegiatan pasar modal dan asuransi di Indonesia."
            ],
            key="kuis1"
        )
        if q1 == "Mencapai dan memelihara kestabilan nilai Rupiah (inflasi dan nilai tukar).":
            skor += 25

    st.divider()

    with st.container():
        st.markdown("#### 2. Saat membayar menggunakan QRIS di warung/toko, langkah keamanan paling tepat sebelum memasukkan PIN adalah...")
        q2 = st.radio(
            "Pilih jawaban:",
            [
                "Langsung scan dan bayar secepat mungkin tanpa melihat layar.",
                "Memastikan nama merchant (toko) yang muncul di layar HP sesuai dengan nama toko tempat bertransaksi.",
                "Meminta kasir mengetikkan PIN aplikasi pembayaran kita."
            ],
            key="kuis2"
        )
        if q2 == "Memastikan nama merchant (toko) yang muncul di layar HP sesuai dengan nama toko tempat bertransaksi.":
            skor += 25

    st.divider()

    with st.container():
        st.markdown("#### 3. Mengapa tindakan menstapler, mencoret, atau melipat uang Rupiah bertentangan dengan semangat Cinta Rupiah?")
        q3 = st.radio(
            "Pilih jawaban:",
            [
                "Karena dapat merusak unsur pengaman uang, memperpendek masa edar uang, dan menyulitkan deteksi keaslian.",
                "Karena membuat uang menjadi lebih berat saat disimpan di dompet.",
                "Karena tinta coretan membuat nilai nominal uang bertambah."
            ],
            key="kuis3"
        )
        if q3 == "Karena dapat merusak unsur pengaman uang, memperpendek masa edar uang, dan menyulitkan deteksi keaslian.":
            skor += 25

    st.divider()

    with st.container():
        st.markdown("#### 4. Dalam pilar 'Paham Rupiah', bagaimana cara masyarakat turut menjaga kestabilan inflasi sehari-hari?")
        q4 = st.radio(
            "Pilih jawaban:",
            [
                "Menimbun bahan pokok dalam jumlah besar saat mendengar isu kenaikan harga.",
                "Berbelanja secara bijak sesuai kebutuhan (tidak berlebihan) dan mengutamakan produk dalam negeri.",
                "Menyimpan seluruh uang tunai di bawah bantal."
            ],
            key="kuis4"
        )
        if q4 == "Berbelanja secara bijak sesuai kebutuhan (tidak berlebihan) dan mengutamakan produk dalam negeri.":
            skor += 25

    st.write("")
    if st.button("🎯 Lihat Predikat Duta CBP Saya", type="primary"):
        st.subheader(f"Skor Akhir Anda: {skor} / 100")
        if skor == 100:
            st.balloons()
            st.success("🏅 **PREDIKAT: DUTA UTAMA CBP RUPIAH!** Pemahaman Anda tentang kebanksentralan, QRIS, dan perlindungan konsumen sangat luar biasa.")
        elif skor >= 75:
            st.info("🥈 **PREDIKAT: SAHABAT CBP RUPIAH!** Anda sudah memahami sebagian besar prinsip menjaga Rupiah dan keamanan transaksi.")
        else:
            st.warning("📘 **PREDIKAT: PENJELAJAH RUPIAH!** Yuk baca kembali materi di tab Beranda untuk memperkuat literasi kebanksentralan Anda.")
