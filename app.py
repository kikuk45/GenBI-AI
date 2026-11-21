import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import time

# ==========================================
# KONFIGURASI HALAMAN & TEMA VISUAL
# ==========================================
st.set_page_config(
    page_title="CBP Rupiah & AI Guard",
    page_icon="🇮🇩",
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
.hero-banner h1 { color: #FFFFFF; margin-bottom: 6px; font-size: 1.9rem; }
.hero-banner p { color: #E2E8F0; font-size: 1rem; margin: 0; }
.cbp-card {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 14px;
    border-top: 5px solid #002D72;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    height: 100%;
}
.cbp-card-gold { border-top: 5px solid #D4AF37; }
.cbp-card-red { border-top: 5px solid #C8102E; }
.cbp-title { color: #002D72; font-weight: 700; font-size: 1.2rem; margin-bottom: 8px; }
.badge-bi {
    background-color: #D4AF37;
    color: #002D72;
    padding: 4px 12px;
    border-radius: 20px;
    font-weight: 700;
    font-size: 0.78rem;
    display: inline-block;
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# GENERATOR VISUAL UANG RUPIAH (PLOTLY SHAPE)
# ==========================================
def buat_visual_uang(pecahan, mode_cahaya, c_lihat1, c_lihat2, c_raba1, c_raba2, c_terawang1, c_terawang2):
    data_uang = {
        "Rp100.000 (TE 2022)": {
            "nominal": "Rp100.000",
            "terbilang": "SERATUS RIBU RUPIAH",
            "tokoh": "Ir. Soekarno & Drs. Mohammad Hatta",
            "warna_dasar": "#B91C1C",
            "warna_sekunder": "#991B1B"
        },
        "Rp50.000 (TE 2022)": {
            "nominal": "Rp50.000",
            "terbilang": "LIMA PULUH RIBU RUPIAH",
            "tokoh": "Ir. H. Djuanda Kartawidjaja",
            "warna_dasar": "#1D4ED8",
            "warna_sekunder": "#1E3A8A"
        },
        "Rp20.000 (TE 2022)": {
            "nominal": "Rp20.000",
            "terbilang": "DUA PULUH RIBU RUPIAH",
            "tokoh": "Dr. G.S.S.J. Ratulangi",
            "warna_dasar": "#15803D",
            "warna_sekunder": "#14532D"
        },
        "Rp10.000 (TE 2022)": {
            "nominal": "Rp10.000",
            "terbilang": "SEPULUH RIBU RUPIAH",
            "tokoh": "Frans Kaisiepo",
            "warna_dasar": "#6D28D9",
            "warna_sekunder": "#4C1D95"
        }
    }

    info = data_uang[pecahan]

    # Mode Pencahayaan
    if mode_cahaya == "🔦 Mode Sinar UV":
        bg_uang = "#0F172A"
        garis_tepi = "#38BDF8"
        opasitas_dasar = 0.95
    elif mode_cahaya == "☀️ Mode Diterawang":
        bg_uang = info["warna_dasar"]
        garis_tepi = "#FACC15"
        opasitas_dasar = 0.55
    else:
        bg_uang = info["warna_dasar"]
        garis_tepi = "#D4AF37"
        opasitas_dasar = 0.92

    fig = go.Figure()

    # 1. Badan Utama Uang Kertas
    fig.add_shape(
        type="rect", x0=0, y0=0, x1=100, y1=46,
        fillcolor=bg_uang, opacity=opasitas_dasar,
        line=dict(color=garis_tepi, width=3)
    )
    fig.add_shape(
        type="rect", x0=2, y0=2, x1=98, y1=44,
        fillcolor="rgba(0,0,0,0)",
        line=dict(color="rgba(255,255,255,0.4)", width=1, dash="dot")
    )

    # 2. Blind Code (Kode Tunanetra - Diraba)
    warna_blind = "#FACC15" if c_raba2 else "rgba(255,255,255,0.25)"
    for y_pos in [14, 19, 24, 29]:
        fig.add_shape(type="rect", x0=2.5, y0=y_pos, x1=4, y1=y_pos+3, fillcolor=warna_blind, line_width=0)
        fig.add_shape(type="rect", x0=96, y0=y_pos, x1=97.5, y1=y_pos+3, fillcolor=warna_blind, line_width=0)

    # 3. Watermark / Tanda Air (Diterawang)
    op_wm = 0.9 if (c_terawang1 or mode_cahaya == "☀️ Mode Diterawang") else 0.2
    fig.add_shape(
        type="circle", x0=10, y0=11, x1=28, y1=35,
        fillcolor="rgba(255,255,255,0.25)", opacity=op_wm,
        line=dict(color="#FDE047", width=2, dash="dash")
    )
    fig.add_annotation(
        x=19, y=23, text="WATERMARK<br>PAHLAWAN", showarrow=False,
        font=dict(color="white", size=9), opacity=op_wm
    )

    # 4. Rectoverso Logo BI (Diterawang)
    op_rv = 1.0 if (c_terawang2 or mode_cahaya == "☀️ Mode Diterawang") else 0.25
    fig.add_shape(
        type="circle", x0=31, y0=33, x1=38, y1=41,
        fillcolor="rgba(255,255,255,0.2)", opacity=op_rv,
        line=dict(color="#FACC15", width=2)
    )
    fig.add_annotation(
        x=34.5, y=37, text="<b>BI</b>", showarrow=False,
        font=dict(color="#FACC15", size=11), opacity=op_rv
    )

    # 5. Benang Pengaman (Dilihat)
    warna_benang = "#38BDF8" if mode_cahaya == "🔦 Mode Sinar UV" else "#FACC15"
    op_benang = 0.95 if c_lihat2 else 0.2
    fig.add_shape(
        type="rect", x0=43, y0=0, x1=45, y1=46,
        fillcolor=warna_benang, opacity=op_benang, line_width=0
    )

    # 6. Tinta Berubah Warna / Color Shifting (Dilihat)
    warna_cs = "#22C55E" if (c_lihat1 and mode_cahaya != "Normal") else ("#F59E0B" if c_lihat1 else "rgba(255,255,255,0.2)")
    fig.add_shape(
        type="circle", x0=51, y0=12, x1=61, y1=24,
        fillcolor=warna_cs,
        line=dict(color="white", width=2)
    )
    fig.add_annotation(
        x=56, y=18, text="COLOR<br>SHIFT", showarrow=False,
        font=dict(color="white", size=8)
    )

    # 7. Area Cetak Intaglio / Gambar Utama (Diraba)
    garis_intaglio = "#FDE047" if c_raba1 else "rgba(255,255,255,0.4)"
    fig.add_shape(
        type="rect", x0=65, y0=10, x1=93, y1=32,
        fillcolor="rgba(255,255,255,0.12)",
        line=dict(color=garis_intaglio, width=2.5)
    )
    fig.add_annotation(
        x=79, y=21, text="<b>GAMBAR UTAMA</b><br>(Cetak Intaglio Kasar)", showarrow=False,
        font=dict(color="#FDE047" if c_raba1 else "white", size=10)
    )

    # Teks Identitas Uang Rupiah
    fig.add_annotation(x=48, y=40, text="<b>BANK INDONESIA</b>", showarrow=False, xanchor="left", font=dict(color="white", size=13))
    fig.add_annotation(x=94, y=39, text=f"<b>{info['nominal']}</b>", showarrow=False, xanchor="right", font=dict(color="#FDE047", size=18))
    fig.add_annotation(x=6, y=6, text=f"<b>{info['terbilang']}</b>", showarrow=False, xanchor="left", font=dict(color="white", size=10))
    fig.add_annotation(x=94, y=6, text=info["tokoh"], showarrow=False, xanchor="right", font=dict(color="#E2E8F0", size=9))

    fig.update_xaxes(visible=False, range=[-1, 101])
    fig.update_yaxes(visible=False, range=[-1, 47])
    fig.update_layout(
        height=270,
        margin=dict(l=5, r=5, t=5, b=5),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    return fig


# ==========================================
# SIDEBAR NAVIGASI
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#002D72; margin-bottom:0;'>🇮🇩 CBP RUPIAH</h2>", unsafe_allow_html=True)
    st.caption("<p style='text-align:center;'>Smart Education & AI Risk Governance</p>", unsafe_allow_html=True)
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
    st.info("💡 **Integrasi AI Management:** Menggunakan sistem pemindaian berbasis aturan (*Rule-Based AI*) dan visualisasi interaktif untuk membantu masyarakat mengenali ciri keaslian uang dan mencegah kejahatan finansial digital.")

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

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="cbp-card cbp-card-red">
            <div class="cbp-title">❤️ CINTA RUPIAH</div>
            <p style="color:#334155; font-size:0.95rem;">Wujud kemampuan masyarakat untuk <b>Mengenali</b> karakteristik Rupiah, <b>Merawat</b> Rupiah (5 Jangan), serta <b>Menjaga</b> diri dari kejahatan uang palsu.</p>
            <small style="color:#C8102E; font-weight:600;">Kunci: 3D (Dilihat, Diraba, Diterawang) & 5 Jangan</small>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="cbp-card cbp-card-gold">
            <div class="cbp-title">🇮🇩 BANGGA RUPIAH</div>
            <p style="color:#334155; font-size:0.95rem;">Wujud kemampuan masyarakat memahami Rupiah sebagai <b>Alat Pembayaran yang Sah</b>, <b>Simbol Kedaulatan NKRI</b>, dan <b>Alat Pemersatu Bangsa</b>.</p>
            <small style="color:#B45309; font-weight:600;">Kunci: Wajib digunakan di seluruh wilayah NKRI</small>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="cbp-card">
            <div class="cbp-title">🧠 PAHAM RUPIAH</div>
            <p style="color:#334155; font-size:0.95rem;">Wujud kemampuan masyarakat memahami peran Rupiah dalam <b>Peredaran Uang</b>, <b>Stabilitas Ekonomi (Inflasi)</b>, serta perilaku <b>Berbelanja Bijak</b>.</p>
            <small style="color:#002D72; font-weight:600;">Kunci: Belanja sesuai kebutuhan & produk dalam negeri</small>
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
            df_risiko, x="Tingkat Kerentanan Masyarakat", y="Kategori Ancaman",
            orientation="h", color="Tingkat Kerentanan Masyarakat",
            color_continuous_scale=["#00509E", "#002D72", "#C8102E"],
            text="Tingkat Kerentanan Masyarakat"
        )
        fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
            height=290, margin=dict(l=10, r=10, t=10, b=10), coloraxis_showscale=False
        )
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        st.info("💡 **Peran Tata Kelola AI (AI Governance):** Perkembangan *Generative AI* memudahkan pelaku kejahatan membuat struk transfer palsu hingga hoaks uang baru. Edukasi CBP membantu masyarakat melakukan **verifikasi berlapis** sebelum bertransaksi.")
        st.warning("🚫 **Prinsip 5 Jangan Merawat Rupiah:** 1. Jangan Dilipat • 2. Jangan Dicoret • 3. Jangan Distapler • 4. Jangan Diremas • 5. Jangan Dibasahi")

# ==========================================
# MODUL 2: ASISTEN CEK KEASLIAN (3D) & AI
# ==========================================
elif menu == "🔍 Asisten Cek Keaslian (3D) & AI":
    st.markdown("""
    <div class="hero-banner">
        <span class="badge-bi">SISTEM PENDUKUNG KEPUTUSAN & VISUAL 3D</span>
        <h1>Simulator Inspeksi Keaslian Uang Rupiah (Metode 3D)</h1>
        <p>Amati ilustrasi fitur pengaman Rupiah Tahun Emisi 2022 secara interaktif dan centang indikator yang ditemukan untuk menghitung indeks keasliannya.</p>
    </div>
    """, unsafe_allow_html=True)

    col_input, col_visual = st.columns([1.15, 1.25])

    with col_input:
        st.subheader("📋 Checklist Pemeriksaan Fisik")
        pecahan = st.selectbox(
            "Pilih Pecahan Uang Kertas:",
            ["Rp100.000 (TE 2022)", "Rp50.000 (TE 2022)", "Rp20.000 (TE 2022)", "Rp10.000 (TE 2022)"]
        )

        mode_cahaya = st.radio(
            "Pilih Mode Pencahayaan Simulasi:",
            ["Normal", "☀️ Mode Diterawang", "🔦 Mode Sinar UV"],
            horizontal=True
        )

        st.markdown("**1. Dilihat (Perubahan Warna & Benang Pengaman)**")
        c_lihat1 = st.checkbox("Warna tinta ornamen berubah saat dilihat dari sudut berbeda (Color Shifting).")
        c_lihat2 = st.checkbox("Terdapat benang pengaman seperti dianyam yang berubah warna.")

        st.markdown("**2. Diraba (Tekstur Cetak Intaglio)**")
        c_raba1 = st.checkbox("Terasa kasar saat diraba pada gambar utama pahlawan dan tulisan 'Bank Indonesia'.")
        c_raba2 = st.checkbox("Terdapat kode tunanetra (Blind Code) berupa garis kasar di sisi kanan & kiri uang.")

        st.markdown("**3. Diterawang (Watermark & Rectoverso)**")
        c_terawang1 = st.checkbox("Terlihat tanda air (Watermark) gambar pahlawan saat diterawang ke cahaya.")
        c_terawang2 = st.checkbox("Logo BI (Rectoverso) terlihat utuh dan saling mengisi sempurna dari depan & belakang.")

        checks = [c_lihat1, c_lihat2, c_raba1, c_raba2, c_terawang1, c_terawang2]
        skor_persen = int((sum(checks) / len(checks)) * 100)

    with col_visual:
        st.subheader("💵 Visualisasi Unsur Pengaman Uang")
        
        fig_uang = buat_visual_uang(
            pecahan, mode_cahaya,
            c_lihat1, c_lihat2, c_raba1, c_raba2, c_terawang1, c_terawang2
        )
        st.plotly_chart(fig_uang, use_container_width=True, config={'displayModeBar': False})

        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=skor_persen,
            number={'suffix': "%", 'font': {'color': '#002D72', 'size': 36}},
            title={'text': f"Indeks Keaslian Sistem ({pecahan.split()[0]})", 'font': {'size': 15, 'color': '#334155'}},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#002D72"},
                'bar': {'color': "#002D72"},
                'bgcolor': "white",
                'steps': [
                    {'range': [0, 40], 'color': "#FECACA"},
                    {'range': [40, 85], 'color': "#FDE68A"},
                    {'range': [85, 100], 'color': "#BBF7D0"}
                ],
                'threshold': {'line': {'color': "#C8102E", 'width': 4}, 'thickness': 0.75, 'value': 100}
            }
        ))
        fig_gauge.update_layout(height=210, margin=dict(l=20, r=20, t=35, b=10), paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_gauge, use_container_width=True)

        if skor_persen == 100:
            st.success("✅ **TERVERIFIKASI ASLI:** Seluruh unsur pengaman 3D terpenuhi dengan sempurna.")
        elif skor_persen >= 50:
            st.warning("⚠️ **PERLU PEMERIKSAAN LANJUT:** Beberapa unsur pengaman belum dicentang atau kondisi uang lusuh. Gunakan sinar UV atau tanyakan ke bank terdekat.")
        else:
            st.error("🚨 **DIRAGUKAN KEASLIANNYA:** Unsur pengaman utama belum ditemukan. Centang ciri yang sesuai pada uang atau laporkan ke bank terdekat jika mencurigakan.")

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

    contoh_pilihan = st.selectbox(
        "Pilih contoh kasus untuk diuji atau ketik manual di bawah:",
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
                time.sleep(0.5)

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
                temuan.append("📢 **Indikasi Disinformasi/Hoaks Rupiah:** Pencabutan uang Rupiah selalu diumumkan secara resmi melalui situs bi.go.id dengan masa tenggang penukaran bertahun-tahun.")

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
