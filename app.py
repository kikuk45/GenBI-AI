import os
import time
import numpy as np
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image, ImageChops, ImageEnhance

# ==========================================
# KONFIGURASI HALAMAN & TEMA VISUAL
# ==========================================
st.set_page_config(
    page_title="Rupiah AI Integrity Lab - Inovasi Edukasi Publik",
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
.hero-banner h1 { color: #FFFFFF; margin-bottom: 6px; font-size: 1.85rem; }
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
.cbp-title { color: #002D72; font-weight: 700; font-size: 1.15rem; margin-bottom: 8px; }
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

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def muat_foto_rupiah(nama_file):
    jalur_utama = os.path.join(BASE_DIR, nama_file)
    if os.path.exists(jalur_utama):
        return Image.open(jalur_utama)
    if os.path.exists(nama_file):
        return Image.open(nama_file)
    return None

# ==========================================
# FUNGSI PEMETAAN VISUAL 3D RUPIAH TE 2022
# ==========================================
def buat_visual_uang_bi(pecahan, mode_cahaya, c_lihat1, c_lihat2, c_raba1, c_raba2, c_terawang1, c_terawang2):
    katalog_uang = {
        "Rp100.000 (TE 2022)": {"file": "TE-2022-100000-depan.jpg", "tokoh": "Dr. (H.C.) Ir. Soekarno & Dr. (H.C.) Drs. Mohammad Hatta", "warna": "#B91C1C"},
        "Rp50.000 (TE 2022)": {"file": "TE-2022-50000-depan.jpg", "tokoh": "Ir. H. Djuanda Kartawidjaja", "warna": "#1D4ED8"},
        "Rp20.000 (TE 2022)": {"file": "TE-2022-20000-depan.jpg", "tokoh": "Dr. G.S.S.J. Ratulangi", "warna": "#15803D"},
        "Rp10.000 (TE 2022)": {"file": "TE-2022-10000-depan.jpg", "tokoh": "Frans Kaisiepo", "warna": "#6D28D9"},
        "Rp5.000 (TE 2022)": {"file": "TE-2022-5000-depan.jpg", "tokoh": "Dr. K.H. Idham Chalid", "warna": "#B45309"},
        "Rp2.000 (TE 2022)": {"file": "TE-2022-2000-depan.jpg", "tokoh": "Mohammad Hoesni Thamrin", "warna": "#475569"},
        "Rp1.000 (TE 2022)": {"file": "TE-2022-1000-depan.jpg", "tokoh": "Tjut Meutia", "warna": "#0F766E"}
    }

    info = katalog_uang[pecahan]
    img = muat_foto_rupiah(info["file"])
    fig = go.Figure()

    if mode_cahaya == "🔦 Mode Sinar UV":
        opasitas_img, warna_lapis = 0.45, "rgba(10, 15, 45, 0.62)"
    elif mode_cahaya == "☀️ Mode Diterawang":
        opasitas_img, warna_lapis = 0.72, "rgba(255, 250, 210, 0.18)"
    else:
        opasitas_img, warna_lapis = 1.0, "rgba(0, 0, 0, 0)"

    if img is not None:
        fig.add_layout_image(dict(source=img, xref="x", yref="y", x=0, y=46, sizex=100, sizey=46, sizing="stretch", opacity=opasitas_img, layer="below"))
    else:
        fig.add_shape(type="rect", x0=0, y0=0, x1=100, y1=46, fillcolor=info["warna"], line=dict(color="#D4AF37", width=3))
        fig.add_annotation(x=50, y=23, text=f"<b>{pecahan} - {info['tokoh']}</b>", showarrow=False, font=dict(color="white", size=13))

    if mode_cahaya != "Normal":
        fig.add_shape(type="rect", x0=0, y0=0, x1=100, y1=46, fillcolor=warna_lapis, line_width=0)

    if c_lihat2:
        warna_b = "#38BDF8" if mode_cahaya == "🔦 Mode Sinar UV" else "#FACC15"
        fig.add_shape(type="rect", x0=28.8, y0=0, x1=31.5, y1=46, fillcolor=warna_b, opacity=0.65, line=dict(color="#FFFFFF", width=1.5))
        fig.add_annotation(x=30.2, y=43.5, text="<b>Benang Pengaman</b>", showarrow=False, bgcolor="#002D72", font=dict(color="#FACC15", size=8.5))

    if c_terawang1 or mode_cahaya == "☀️ Mode Diterawang":
        fig.add_shape(type="circle", x0=8, y0=19, x1=23, y1=36, fillcolor="rgba(255, 255, 255, 0.22)", line=dict(color="#FDE047", width=2.5, dash="dash"))
        fig.add_annotation(x=15.5, y=37.5, text="<b>WATERMARK</b>", showarrow=False, bgcolor="rgba(0,45,114,0.88)", font=dict(color="#FDE047", size=8.5))

    if c_lihat1:
        fig.add_shape(type="circle", x0=6.5, y0=10, x1=18.5, y1=18.5, fillcolor="rgba(34, 197, 94, 0.25)", line=dict(color="#22C55E", width=2.5))
        fig.add_annotation(x=12.5, y=8.2, text="<b>OVMI / Color Shifting</b>", showarrow=False, bgcolor="#15803D", font=dict(color="white", size=8))

    if c_terawang2 or mode_cahaya == "☀️ Mode Diterawang":
        fig.add_shape(type="circle", x0=89.5, y0=12.0, x1=95.5, y1=18.2, fillcolor="rgba(56, 189, 248, 0.22)", line=dict(color="#0284C7", width=2.5))
        fig.add_annotation(x=89.5, y=20.2, text="<b>Rectoverso BI</b>", showarrow=False, bgcolor="#002D72", font=dict(color="#38BDF8", size=8))

    if c_raba1:
        fig.add_shape(type="rect", x0=33, y0=5, x1=70, y1=36, fillcolor="rgba(250, 204, 21, 0.12)", line=dict(color="#FACC15", width=2.5))
        fig.add_annotation(x=51.5, y=38, text="<b>Cetak Intaglio (Terasa Kasar)</b>", showarrow=False, bgcolor="#B45309", font=dict(color="white", size=8.5))

    if c_raba2:
        fig.add_shape(type="rect", x0=0.2, y0=10, x1=2.2, y1=35, fillcolor="rgba(250,204,21,0.55)", line=dict(color="#FACC15", width=1.5))
        fig.add_shape(type="rect", x0=97.8, y0=10, x1=99.8, y1=35, fillcolor="rgba(250,204,21,0.55)", line=dict(color="#FACC15", width=1.5))
        fig.add_annotation(x=92, y=37, text="<b>Blind Code</b>", showarrow=False, bgcolor="#002D72", font=dict(color="white", size=8))

    fig.update_xaxes(visible=False, range=[0, 100])
    fig.update_yaxes(visible=False, range=[0, 46])
    fig.update_layout(height=305, margin=dict(l=2, r=2, t=2, b=2), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    return fig, info["tokoh"]

# ==========================================
# FUNGSI FORENSIK GAMBAR (ERROR LEVEL ANALYSIS)
# ==========================================
def analisis_ela_gambar(pil_img):
    rgb_img = pil_img.convert("RGB")
    temp_path = "temp_ela.jpg"
    rgb_img.save(temp_path, "JPEG", quality=85)
    kompres_img = Image.open(temp_path)
    diff = ImageChops.difference(rgb_img, kompres_img)
    extrema = diff.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    if max_diff == 0:
        max_diff = 1
    scale = 255.0 / max_diff
    ela_img = ImageEnhance.Brightness(diff).enhance(scale)
    arr = np.array(diff)
    skor_anomali = round(float(np.std(arr)), 2)
    if os.path.exists(temp_path):
        os.remove(temp_path)
    return ela_img, skor_anomali

# ==========================================
# SIDEBAR NAVIGASI
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#002D72; margin-bottom:0;'>🇮🇩 RUPIAH AI LAB</h2>", unsafe_allow_html=True)
    st.caption("<p style='text-align:center;'>Next-Gen Central Bank & AI Governance</p>", unsafe_allow_html=True)
    st.divider()
    
    menu = st.radio(
        "🧭 Pilih Laboratorium Interaktif:",
        [
            "🔬 Lab 1: Forensik Struk & QRIS (Computer Vision)",
            "📉 Lab 2: Simulator Dampak '5 Jangan' & Biaya Cetak",
            "🤖 Lab 3: Audit Halusinasi AI Kebanksentralan",
            "💵 Lab 4: Pemetaan Visual 3D Rupiah TE 2022"
        ]
    )
    
    st.divider()
    st.info("🚀 **Inovasi Edukasi Publik:** Menggabungkan *Explainable AI*, analisis forensik citra digital, dan simulasi kebijakan moneter interaktif.")

# ==========================================
# LAB 1: FORENSIK STRUK TRANSFER & QRIS (INOVASI BARU)
# ==========================================
if menu == "🔬 Lab 1: Forensik Struk Struk & QRIS (Computer Vision)" or menu == "🔬 Lab 1: Forensik Struk & QRIS (Computer Vision)":
    st.markdown("""
    <div class="hero-banner">
        <span class="badge-bi">INOVASI COMPUTER VISION & PERLINDUNGAN KONSUMEN</span>
        <h1>AI Forensik Bukti Transfer & Stiker QRIS Digital</h1>
        <p>Unggah tangkapan layar (screenshot) bukti transfer m-banking atau foto QRIS yang mencurigakan untuk mendeteksi jejak manipulasi editan AI/aplikasi melalui Error Level Analysis (ELA).</p>
    </div>
    """, unsafe_allow_html=True)

    col_up, col_info = st.columns([1.2, 1])
    with col_up:
        uploaded_file = st.file_uploader("📤 Unggah Gambar Bukti Transfer / QRIS (JPG/PNG):", type=["jpg", "jpeg", "png"])
    with col_info:
        st.markdown("""
        <div class="cbp-card cbp-card-gold">
            <div class="cbp-title">Bagaimana AI Mendeteksi Editan Struk?</div>
            <p style="font-size:0.9rem; color:#334155;">
            Ketika pelaku kejahatan mengubah nominal transfer atau menempelkan QRIS palsu menggunakan AI/editor foto, tingkat kompresi piksel di area yang diubah akan berbeda dari latar belakang aslinya. Teknik <b>Error Level Analysis (ELA)</b> memetakan perbedaan tersebut menjadi pendaran terang.
            </p>
        </div>
        """, unsafe_allow_html=True)

    if uploaded_file is not None:
        img_asli = Image.open(uploaded_file)
        with st.spinner("Menjalankan pemindaian forensik kompresi piksel..."):
            time.sleep(0.6)
            img_ela, skor_std = analisis_ela_gambar(img_asli)

        c1, c2 = st.columns(2)
        with c1:
            st.subheader("🖼️ Gambar Asli yang Diunggah")
            st.image(img_asli, use_container_width=True)
        with c2:
            st.subheader("🩻 Peta Forensik ELA (Jejak Piksel)")
            st.image(img_ela, use_container_width=True)

        st.divider()
        st.subheader("📊 Hasil Audit Forensik Sistem:")
        m1, m2, m3 = st.columns(3)
        m1.metric("Resolusi Citra", f"{img_asli.size[0]} x {img_asli.size[1]} px")
        m2.metric("Indeks Variansi Piksel (ELA)", f"{skor_std}")
        status_audit = "Waspada Tinggi" if skor_std > 6.5 else "Relatif Seragam"
        m3.metric("Indikasi Anomali", status_audit)

        st.warning("🔍 **Cara Membaca Peta ELA:** Perhatikan bagian **angka nominal, jam transaksi, atau kotak QRIS**. Jika bagian tersebut menyala jauh lebih terang/kasar dibandingkan teks lain di sekitarnya, kemungkinan besar gambar tersebut telah diedit. **Selalu cek mutasi saldo langsung di aplikasi m-banking Anda!**")
    else:
        st.info("👆 Silakan unggah gambar bukti transfer atau foto QRIS apa saja dari perangkat Anda untuk menguji cara kerja deteksi forensik ini.")

# ==========================================
# LAB 2: SIMULATOR DAMPAK '5 JANGAN' (INOVASI BARU)
# ==========================================
elif menu == "📉 Lab 2: Simulator Dampak '5 Jangan' & Biaya Cetak":
    st.markdown("""
    <div class="hero-banner">
        <span class="badge-bi">INOVASI PREDICTIVE POLICY MODELING</span>
        <h1>Simulator Dampak Perilaku '5 Jangan' terhadap Ekonomi Negara</h1>
        <p>Selama ini masyarakat hanya dihimbau merawat Rupiah. Ubah parameter perilaku masyarakat di bawah ini untuk melihat proyeksi kerusakan uang dan beban pencetakan ulang.</p>
    </div>
    """, unsafe_allow_html=True)

    col_ctrl, col_chart = st.columns([1, 1.4])

    with col_ctrl:
        st.subheader("🎛️ Parameter Perilaku Masyarakat")
        kebiasaan_buruk = st.slider(
            "Tingkat Kebiasaan Melipat, Menstapler & Mencoret Uang (%):",
            min_value=5, max_value=90, value=45, step=5
        )
        pecahan_simulasi = st.selectbox(
            "Pilih Segmen Pecahan Uang:",
            ["Pecahan Kecil (Rp1.000 - Rp5.000)", "Pecahan Besar (Rp20.000 - Rp100.000)"]
        )

        # Model simulasi edukatif umur edar (bulan) & rasio UTLE
        umur_ideal = 24 if "Kecil" in pecahan_simulasi else 48
        umur_aktual = max(4, round(umur_ideal * (1 - (kebiasaan_buruk / 115)), 1))
        rasio_utle = round(10 + (kebiasaan_buruk * 0.78), 1)
        indeks_efisiensi = max(10, round(100 - (kebiasaan_buruk * 0.85)))

        st.metric("Estimasi Umur Edar Uang", f"{umur_aktual} Bulan", delta=f"{round(umur_aktual - umur_ideal, 1)} Bulan dari standar ideal")
        st.metric("Proyeksi Uang Tidak Layak Edar (UTLE)", f"{rasio_utle}%", delta="Harus ditarik & dimusnahkan", delta_color="inverse")

    with col_chart:
        st.subheader("📈 Proyeksi Degradasi Kualitas Rupiah (24 Bulan)")
        bulan = list(range(0, 25, 3))
        kualitas_ideal = [max(40, 100 - (b * (100 / (umur_ideal * 1.5)))) for b in bulan]
        kualitas_aktual = [max(10, 100 - (b * (100 / (umur_aktual * 1.2)))) for b in bulan]

        df_sim = pd.DataFrame({
            "Bulan Peredaran": bulan,
            "Dirawat Baik (Prinsip 5 Jangan)": kualitas_ideal,
            "Skenario Perilaku Saat Ini": kualitas_aktual
        })

        fig_sim = px.line(
            df_sim, x="Bulan Peredaran",
            y=["Dirawat Baik (Prinsip 5 Jangan)", "Skenario Perilaku Saat Ini"],
            markers=True,
            color_discrete_map={
                "Dirawat Baik (Prinsip 5 Jangan)": "#002D72",
                "Skenario Perilaku Saat Ini": "#C8102E"
            }
        )
        fig_sim.add_hline(y=50, line_dash="dash", line_color="#D4AF37", annotation_text="Batas Layak Edar (50%)")
        fig_sim.update_layout(yaxis_title="Skor Kelayakan Fisik (%)", height=330, margin=dict(l=10, r=10, t=20, b=10))
        st.plotly_chart(fig_sim, use_container_width=True)

        st.success(f"💡 **Insight Kebanksentralan:** Dengan menurunkan kebiasaan melipat/menstapler uang, masa edar Rupiah meningkat menjadi **{umur_aktual} bulan**, sehingga anggaran negara untuk pencetakan dan pemusnahan uang lusuh dapat dihemat secara signifikan.")

# ==========================================
# LAB 3: AUDIT HALUSINASI AI KEBANKSENTRALAN (INOVASI BARU)
# ==========================================
elif menu == "🤖 Lab 3: Audit Halusinasi AI Kebanksentralan":
    st.markdown("""
    <div class="hero-banner">
        <span class="badge-bi">INOVASI AI GOVERNANCE & EXPLAINABLE AI</span>
        <h1>Sandbox Audit Halusinasi AI dalam Informasi Keuangan</h1>
        <p>Masyarakat kini sering bertanya ke AI publik soal aturan uang dan transaksi. Bandingkan bagaimana AI tanpa tata kelola bisa menyesatkan vs AI yang mematuhi prinsip AI Governance.</p>
    </div>
    """, unsafe_allow_html=True)

    kasus_ai = st.selectbox(
        "Pilih Pertanyaan Masyarakat yang Sering Ditanyakan ke Chatbot AI:",
        [
            "Kasus 1: Apakah uang Rupiah yang robek separuh masih bisa ditukar penuh di Bank Indonesia?",
            "Kasus 2: Saya salah transfer lewat QRIS ke warung sebelah, apakah Bank Indonesia bisa langsung menarik balik saldo saya?",
            "Kasus 3: Benarkah tahun depan Rp100.000 akan dipotong nolnya menjadi Rp100 dan uang lama langsung hangus?"
        ]
    )

    col_raw, col_gov = st.columns(2)

    if "Kasus 1" in kasus_ai:
        raw_ans = "Tentu saja! Semua uang robek berapapun ukurannya otomatis diganti 100% penuh oleh bank mana saja asalkan nomor serinya masih kelihatan satu angka."
        raw_risk = "🚨 **Risiko Halusinasi:** Mengabaikan syarat fisik minimal (> 2/3 ukuran asli) dan kesatuan nomor seri sesuai PBI Pengelolaan Uang Rupiah."
        gov_ans = "Penggantian uang rusak diberikan sebesar **nilai nominal penuh (100%)** HANYA JIKA fisik uang Rupiah kertas masih **lebih besar dari 2/3 (dua pertiga) ukuran aslinya** dan ciri keasliannya masih dapat dikenali (serta nomor seri lengkap jika terpotong)."
        gov_guard = "✅ **AI Guardrail Aktif:** Terverifikasi berdasarkan Peraturan Bank Indonesia (PBI) tentang Pengelolaan Uang Rupiah."

    elif "Kasus 2" in kasus_ai:
        raw_ans = "Bisa, silakan hubungi call center Bank Indonesia dan sebutkan PIN aplikasi Anda agar sistem BI segera membatalkan transaksi QRIS tersebut dalam 5 menit."
        raw_risk = "🚨 **Risiko Keamanan Fatal:** Mendorong pengguna membocorkan PIN dan salah menjelaskan kewenangan operasional transaksi ritel."
        gov_ans = "Transaksi QRIS bersifat *real-time* dan final. Bank Indonesia sebagai regulator **tidak dapat membatalkan transaksi secara sepihak dan tidak pernah meminta PIN/OTP**. Segera hubungi **Penyedia Jasa Pembayaran (Bank/Dompet Digital)** penerbit aplikasi Anda dengan melampirkan bukti transaksi untuk mediasi pengembalian dana."
        gov_guard = "✅ **AI Guardrail Aktif:** Perlindungan Konsumen (PeKA) & Kebijakan Zero-Credential Request."

    else:
        raw_ans = "Benar, pemerintah sudah memutuskan mulai 1 Januari depan uang Rp100.000 lama otomatis tidak laku dan hangus jika tidak ditukar minggu ini."
        raw_risk = "🚨 **Risiko Disinformasi Publik:** Memicu kepanikan masyarakat (*panic exchange*) dan membuka celah penipuan tautan penukaran uang."
        gov_ans = "Informasi tersebut **HOAKS**. Kebijakan redenominasi memerlukan undang-undang khusus, kesiapan ekonomi yang matang, serta masa transisi bertahun-tahun di mana uang lama dan baru tetap berlaku berdampingan. Selalu cek kebenaran informasi melalui **BICARA 131** atau situs resmi **bi.go.id**."
        gov_guard = "✅ **AI Guardrail Aktif:** Fact-Checking Moneter & Anti-Hoaks Kebanksentralan."

    with col_raw:
        st.markdown("""
        <div class="cbp-card cbp-card-red">
            <div class="cbp-title">❌ AI Tanpa Tata Kelola (Raw Unfiltered AI)</div>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        st.error(f"**Jawaban AI:**\n\n\"{raw_ans}\"")
        st.markdown(raw_risk)

    with col_gov:
        st.markdown("""
        <div class="cbp-card">
            <div class="cbp-title">✅ Governed AI (Dengan Prinsip AI Management)</div>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        st.success(f"**Jawaban Terverifikasi:**\n\n\"{gov_ans}\"")
        st.markdown(gov_guard)

# ==========================================
# LAB 4: PEMETAAN VISUAL 3D RUPIAH TE 2022
# ==========================================
elif menu == "💵 Lab 4: Pemetaan Visual 3D Rupiah TE 2022":
    st.markdown("""
    <div class="hero-banner">
        <span class="badge-bi">PEMETAAN VISUAL RUPIAH RESMI & METODE 3D</span>
        <h1>Simulator Inspeksi Keaslian Uang Rupiah (TE 2022)</h1>
        <p>Pilih salah satu dari 7 pecahan uang kertas Rupiah TE 2022 dan centang ciri keaslian yang ditemukan untuk memetakan lokasi unsur pengaman pada uang.</p>
    </div>
    """, unsafe_allow_html=True)

    col_input, col_visual = st.columns([1.1, 1.3])

    with col_input:
        st.subheader("📋 Checklist Pemeriksaan Fisik")
        pecahan = st.selectbox(
            "Pilih Pecahan Uang Kertas (7 Pecahan TE 2022):",
            ["Rp100.000 (TE 2022)", "Rp50.000 (TE 2022)", "Rp20.000 (TE 2022)", "Rp10.000 (TE 2022)", "Rp5.000 (TE 2022)", "Rp2.000 (TE 2022)", "Rp1.000 (TE 2022)"]
        )

        mode_cahaya = st.radio("Pilih Mode Pencahayaan Simulasi:", ["Normal", "☀️ Mode Diterawang", "🔦 Mode Sinar UV"], horizontal=True)

        st.markdown("**1. Dilihat (Perubahan Warna & Benang Pengaman)**")
        c_lihat1 = st.checkbox("Warna tinta bunga anggrek/perisai berubah saat dilihat dari sudut berbeda (OVMI / Color Shifting).")
        c_lihat2 = st.checkbox("Terdapat benang pengaman seperti dianyam yang berubah warna.")

        st.markdown("**2. Diraba (Tekstur Cetak Intaglio)**")
        c_raba1 = st.checkbox("Terasa kasar saat diraba pada gambar utama pahlawan dan tulisan 'Bank Indonesia'.")
        c_raba2 = st.checkbox("Terdapat kode tunanetra (Blind Code) berupa garis kasar di tepi kanan & kiri uang.")

        st.markdown("**3. Diterawang (Watermark & Rectoverso)**")
        c_terawang1 = st.checkbox("Terlihat tanda air (Watermark) gambar pahlawan saat diterawang ke cahaya.")
        c_terawang2 = st.checkbox("Logo BI (Rectoverso) di sisi kanan terlihat utuh dan saling mengisi sempurna dari depan & belakang.")

        checks = [c_lihat1, c_lihat2, c_raba1, c_raba2, c_terawang1, c_terawang2]
        skor_persen = int((sum(checks) / len(checks)) * 100)

    with col_visual:
        st.subheader("💵 Pemetaan Titik Pengaman Uang Rupiah")
        fig_uang, nama_pahlawan = buat_visual_uang_bi(pecahan, mode_cahaya, c_lihat1, c_lihat2, c_raba1, c_raba2, c_terawang1, c_terawang2)
        st.plotly_chart(fig_uang, use_container_width=True, config={'displayModeBar': False})
        st.caption(f"Gambar Utama: **{nama_pahlawan}** | Sumber: Bank Indonesia ([bi.go.id](https://www.bi.go.id/id/rupiah/gambar-uang/Default.aspx))")

        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=skor_persen,
            number={'suffix': "%", 'font': {'color': '#002D72', 'size': 34}},
            title={'text': f"Indeks Keaslian Sistem ({pecahan.split()[0]})", 'font': {'size': 15, 'color': '#334155'}},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#002D72"},
                'bar': {'color': "#002D72"},
                'bgcolor': "white",
                'steps': [{'range': [0, 40], 'color': "#FECACA"}, {'range': [40, 85], 'color': "#FDE68A"}, {'range': [85, 100], 'color': "#BBF7D0"}],
                'threshold': {'line': {'color': "#C8102E", 'width': 4}, 'thickness': 0.75, 'value': 100}
            }
        ))
        fig_gauge.update_layout(height=205, margin=dict(l=20, r=20, t=35, b=10), paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_gauge, use_container_width=True)
