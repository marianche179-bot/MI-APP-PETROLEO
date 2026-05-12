import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(page_title="FluidMaster Pro - Marian Lisboa", layout="wide")

# 2. ENCABEZADO CON LOGO Y TU NOMBRE
col_logo, col_titulo = st.columns([1, 4])

with col_logo:
    # Enlace directo al escudo de la UDO
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Logo_UDO.svg/512px-Logo_UDO.svg.png", width=120)

with col_titulo:
    st.title("FluidMaster Pro v2.0")
    st.subheader("Ingeniería de Fluidos de Perforación | UDO Anzoátegui")
    st.write("**Desarrollado por:** Ing. Marian Lisboa")

st.divider()

# 3. ENTRADA DE DATOS (En el lateral)
st.sidebar.header("⚙️ Parámetros de Entrada")
l600 = st.sidebar.number_input("Lectura 600 RPM", value=40.0)
l300 = st.sidebar.number_input("Lectura 300 RPM", value=25.0)
caudal = st.sidebar.number_input("Caudal (GPM)", value=300.0)
diam_hoyo = st.sidebar.number_input("Diámetro Hoyo (pulg)", value=8.5)
diam_tubo = st.sidebar.number_input("Diámetro Tubería (pulg)", value=5.0)

# 4. EL BOTÓN QUE SOLICITASTE
# Ahora los cálculos solo se verán si presionas este botón
if st.button("GENERAR DIAGNÓSTICO OPERATIVO"):
    
    # MOTOR DE CÁLCULO
    pv = l600 - l300
    yp = l300 - pv
    va = (24.51 * caudal) / (diam_hoyo**2 - diam_tubo**2)

    # 5. RESULTADOS EN PANTALLA
    st.header("📊 Resultados del Análisis")
    res1, res2, res3 = st.columns(3)

    res1.metric("Viscosidad Plástica (PV)", f"{pv} cp")
    res2.metric("Punto Cedente (YP)", f"{yp} lb/100ft²")
    res3.metric("Velocidad Anular (VA)", f"{round(va, 2)} ft/min")

    st.divider()

    # 6. GRÁFICA DE SEGURIDAD
    st.subheader("🚀 Monitor de Limpieza de Hoyo")

    df_grafica = pd.DataFrame({
        'Parámetro': ['Tu Velocidad', 'Límite Crítico'],
        'Velocidad (ft/min)': [va, 120]
    })

    # Color dinámico
    color_grafica = ["#00CC96" if va >= 120 else "#EF553B", "#636EFA"]

    fig = px.bar(df_grafica, x='Parámetro', y='Velocidad (ft/min)', 
                 color='Parámetro', 
                 color_discrete_sequence=color_grafica,
                 text_auto=True)

    st.plotly_chart(fig, use_container_width=True)

    # 7. MENSAJES DE SEGURIDAD
    if va >= 120:
        st.success("✅ **OPERACIÓN SEGURA:** La velocidad es adecuada.")
        st.balloons()
    else:
        st.error("⚠️ **ALERTA:** Riesgo de atascamiento. Velocidad insuficiente.")

else:
    # Mensaje inicial cuando el botón no se ha presionado
    st.info("Ajusta los valores en la barra lateral y presiona el botón para ver el análisis.")

st.sidebar.markdown("---")
st.sidebar.info("Criterio técnico: Modelo Plástico de Bingham")
