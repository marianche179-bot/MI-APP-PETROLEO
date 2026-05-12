import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="FluidMaster Pro - Marian Lisboa", layout="wide")

# ENCABEZADO
col1, col2 = st.columns([1, 4])

with col1:
    # USAMOS EL NOMBRE EXACTO QUE VEO EN TU CAPTURA
    st.image("Logo_UDO.svg.png", width=120)

with col2:
    st.title("FluidMaster Pro v2.0")
    st.subheader("Ingeniería de Fluidos | UDO Anzoátegui")
    st.write("**Realizado por:** Marian Lisboa")

st.divider()

# DATOS A LA IZQUIERDA
st.sidebar.header("Parámetros del Pozo")
l600 = st.sidebar.number_input("Lectura 600 RPM", value=40.0)
l300 = st.sidebar.number_input("Lectura 300 RPM", value=25.0)
caudal = st.sidebar.number_input("Caudal (GPM)", value=300.0)
dh = st.sidebar.number_input("Diámetro Hoyo (pulg)", value=8.5)
dp = st.sidebar.number_input("Diámetro Tubería (pulg)", value=5.0)

# EL BOTÓN
if st.button("GENERAR DIAGNÓSTICO"):
    # Cálculos
    pv = l600 - l300
    yp = l300 - pv
    va = (24.51 * caudal) / (dh**2 - dp**2)

    st.header("📊 Resultados del Análisis")
    c1, c2, c3 = st.columns(3)
    c1.metric("PV (cp)", pv)
    c2.metric("YP (lb/100ft²)", yp)
    c3.metric("Velocidad Anular (ft/min)", round(va, 2))

    if va >= 120:
        st.success("✅ LIMPIEZA EFICIENTE")
        st.balloons()
    else:
        st.error("⚠️ RIESGO DE ATASCAMIENTO")
else:
    st.info("Ajusta los datos y presiona el botón para calcular.")
