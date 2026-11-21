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
    .stApp {
        background-color: #F4F7FB;
    }
    
    .hero-banner {
        background: linear-gradient(135deg, #002D72 0%, #00509E 100%);
        padding: 26px 30px;
        border-radius: 16px;
        color: white;
        margin-bottom: 22px;
        box-shadow: 0 8px 20px rgba(0, 45, 114, 0.15);
        border-bottom: 5px solid #D4AF37;
    }
    .hero-banner h1 {
        color: #FFFFFF;
        margin-bottom: 8px;
        font-size: 2.0rem;
    }
    .hero-banner p {
        color: #E2E8F0;
        font-size: 1.02rem;
        margin: 0;
    }

    .cbp-card {
        background-color: #FFFFFF;
        padding: 22px;
        border-radius: 14px;
        border-top: 5px solid #002D72;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        height: 100%;
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
        font-size: 1.22rem;
        margin-bottom: 10px;
    }

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
# FUNGSI GENERATOR VISUAL UANG RUPIAH (SVG)
# ==========================================
def render_visual_rupiah(pecahan, mode_cahaya, c_lihat1, c_lihat2, c_raba1, c_raba2, c_terawang1, c_terawang2):
    # Konfigurasi warna dan tokoh sesuai pecahan TE 2022
    data_pecahan = {
        "Rp100.000 (TE 2022)": {
            "nominal": "100.000",
            "teks_nominal": "SERATUS RIBU RUPIAH",
            "tokoh": "Dr. (H.C.) Ir. Soekarno & Dr. (H.C.) Drs. Mohammad Hatta",
            "bg_start": "#C8102E",
            "bg_end": "#9B111E",
            "accent": "#FDE047"
        },
        "Rp50.000 (TE 2022)": {
            "nominal": "50.000",
            "teks_nominal": "LIMA PULUH RIBU RUPIAH",
            "tokoh": "Ir. H. Djuanda Kartawidjaja",
            "bg_start": "#00509E",
            "bg_end": "#002D72",
            "accent": "#7DD3FC"
        },
        "Rp20.000 (TE 2022)": {
            "nominal": "20.000",
            "teks_nominal": "DUA PULUH RIBU RUPIAH",
            "tokoh": "Dr. G.S.S.J. Ratulangi",
            "bg_start": "#15803D",
            "bg_end": "#14532D",
            "accent": "#86EFAC"
        },
        "Rp10.000 (TE 2022)": {
            "nominal": "10.000",
            "teks_nominal": "SEPULUH RIBU RUPIAH",
            "tokoh": "Frans Kaisiepo",
            "bg_start": "#6D28D9",
            "bg_end": "#4C1D95",
            "accent": "#D8B4FE"
        }
    }

    info = data_pecahan[pecahan]

    # Penyesuaian visual berdasarkan mode pencahayaan
    if mode_cahaya == "🔦 Mode Sinar UV":
        grad_1, grad_2 = "#0F172A", "#1E1B4B"
        border_col = "#38BDF8"
        glow_uv = "box-shadow: 0 0 25px rgba(56, 189, 248, 0.6);"
    elif mode_cahaya == "☀️ Mode Diterawang":
        grad_1, grad_2 = info["bg_start"] + "AA", info["bg_end"] + "AA"
        border_col = "#FACC15"
        glow_uv = "box-shadow: 0 0 25px rgba(250, 204, 21, 0.5);"
    else:
        grad_1, grad_2 = info["bg_start"], info["bg_end"]
        border_col = "#D4AF37"
        glow_uv = "box-shadow: 0 10px 24px rgba(0, 0, 0, 0.18);"

    # Indikator dinamis tiap unsur pengaman
    benang_opacity = "1" if c_lihat2 else "0.2"
    benang_color = "#38BDF8" if mode_cahaya == "🔦 Mode Sinar UV" else "#FACC15"

    color_shift_fill = "#22C55E" if (c_lihat1 and mode_cahaya != "Normal") else ("#F59E0B" if c_lihat1 else "rgba(255,255,255,0.15)")
    color_shift_stroke = "#FFFFFF" if c_lihat1 else "rgba(255,255,255,0.3)"

    intaglio_stroke = "#FDE047" if c_raba1 else "rgba(255,255,255,0.45)"
    blind_code_color = "#FACC15" if c_raba2 else "rgba(255,255,255,0.2)"

    watermark_opacity = "0.95" if (c_terawang1 or mode_cahaya == "☀️ Mode Diterawang") else "0.18"
    rectoverso_opacity = "1" if (c_terawang2 or mode_cahaya == "☀️ Mode Diterawang") else "0.25"

    svg_html = f"""
    <div style="background: linear-gradient(135deg, {grad_1} 0%, {grad_2} 100%); 
                border-radius: 16px; padding: 18px; color: white; border: 3px solid {border_col}; {glow_uv} margin-bottom: 16px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-size: 0.78rem; letter-spacing: 1px; background: rgba(0,0,0,0.3); padding: 3px 10px; border-radius: 12px;">
                SIMULASI VISUAL: {mode_cahaya.upper()}
            </span>
            <span style="font-size: 0.8rem; font-weight: bold; color: #FDE047;">NEGARA KESATUAN REPUBLIK INDONESIA</span>
        </div>

        <svg viewBox="0 0 600 265" width="100%" xmlns="http://www.w3.org/2000/svg" style="border-radius: 10px; background: rgba(255,255,255,0.06);">
            <!-- Bingkai Ornamen -->
            <rect x="8" y="8" width="584" height="249" rx="10" fill="none" stroke="rgba(255,255,255,0.35)" stroke-width="2" stroke-dasharray="6,4"/>

            <!-- 1. BLIND CODE (Kode Tunanetra - Diraba) -->
            <g opacity="1">
                <rect x="14" y="85" width="7" height="18" rx="2" fill="{blind_code_color}"/>
                <rect x="14" y="110" width="7" height="18" rx="2" fill="{blind_code_color}"/>
                <rect x="14" y="135" width="7" height="18" rx="2" fill="{blind_code_color}"/>
                <rect x="14" y="160" width="7" height="18" rx="2" fill="{blind_code_color}"/>
                <rect x="579" y="85" width="7" height="18" rx="2" fill="{blind_code_color}"/>
                <rect x="579" y="110" width="7" height="18" rx="2" fill="{blind_code_color}"/>
                <rect x="579" y="135" width="7" height="18" rx="2" fill="{blind_code_color}"/>
                <rect x="579" y="160" width="7" height="18" rx="2" fill="{blind_code_color}"/>
