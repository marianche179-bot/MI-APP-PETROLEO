import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(page_title="FluidMaster Pro - Marian Lisboa", layout="wide")

# 2. ENCABEZADO INSTITUCIONAL (Logo UDO y Nombre)
col_logo, col_titulo = st.columns([1, 4])

with col_logo:
    # URL de un logo de la UDO (puedes cambiarla por una directa si tienes el link)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Logo_UDO.svg/1200px-Logo_UDO.svg.png", width=100)

with col_titulo:
    st.title("FluidMaster Pro v2.0")
    st.subheader("Ingeniería de Fluidos de Perforación | UDO Anzoátegui")
    st.write(f"**Desarrollado por:** Ing. Marian Lisboa")

st.divider()

# 3. ENTRADA DE DATOS (En el lateral para que no estorbe)
st.sidebar.header("⚙️ Parámetros de Entrada")
l600 = st.sidebar.number_input("Lectura 600 RPM", value=40.0)
l300 = st.sidebar.number_input("Lectura 300 RPM", value=25.0)
caudal = st.sidebar.number_input("Caudal (GPM)", value=300.0)
dh = st.sidebar.number_input("Diámetro Hoyo (pulg)", value=8.5)
dp = st.sidebar.number_input("Diámetro Tubería (pulg)", value=5.0)

# 4. CÁLCULOS TÉCNICOS
pv = l600 - l300
yp = l300 - pv
va = (24.5 * caudal) / (dh**2 - dp**2)

# 5. VISUALIZACIÓN DE RESULTADOS
st.header("📊 Diagnóstico Operativo")

col1, col2, col3 = st.columns(3)
col1.metric("Viscosidad Plástica (PV)", f"{pv} cp")
col2.metric("Punto Cedente (YP)", f"{yp} lb/100ft²")
col3.metric("Velocidad Anular (VA)", f"{round(va, 2)} ft/min")

# 6. GRÁFICA DE SEGURIDAD (Aquí es donde deja de ser simple)
st.subheader("🚀 Monitor de Limpieza de Hoyo")

# Crear datos para la gráfica
df_grafica = pd.DataFrame({
    'Parámetro': ['Tu Velocidad', 'Límite Crítico'],
    'Velocidad (ft/min)': [va, 120]
})

# Color dinámico: verde si es seguro, rojo si es peligroso
color_grafica = ["#00CC96" if va >= 120 else "#EF553B", "#636EFA"]

fig = px.bar(df_grafica, x='Parámetro', y='Velocidad (ft/min)', 
             color='Parámetro', 
             color_discrete_sequence=color_grafica,
             text_auto=True)

st.plotly_chart(fig, use_container_width=True)

# 7. ALERTAS FINALES
if va >= 120:
    st.success("✅ **LIMPIEZA EFICIENTE:** El lodo tiene la velocidad necesaria para acarrear los ripios.")
    st.balloons()
else:
    st.error("⚠️ **ALERTA DE SEGURIDAD:** Velocidad por debajo de 120 ft/min. Riesgo de atascamiento.")

st.sidebar.markdown("---")
st.sidebar.info("Criterio técnico: Modelo Plástico de Bingham")
