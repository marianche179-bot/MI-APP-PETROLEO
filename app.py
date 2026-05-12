import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuración de la página
st.set_page_config(page_title="FluidMaster Pro - Marian Lisboa", layout="wide")

# 2. Encabezado con el Logo de la UDO
col1, col2 = st.columns([1, 4])

with col1:
    # Usamos el nombre exacto del archivo que ya tienes en GitHub
    st.image("Logo_UDO.svg.png", width=120)

with col2:
    st.title("FluidMaster Pro v2.0")
    st.subheader("Ingeniería de Fluidos | UDO Anzoátegui")
    st.write("**Realizado por:** Marian Lisboa")

st.divider()

# 3. Entrada de Datos (Panel lateral)
st.sidebar.header("📊 Parámetros Operacionales")
l600 = st.sidebar.number_input("Lectura 600 RPM", value=40.0)
l300 = st.sidebar.number_input("Lectura 300 RPM", value=25.0)
caudal = st.sidebar.number_input("Caudal (GPM)", value=300.0)
dh = st.sidebar.number_input("Diámetro Hoyo (pulg)", value=8.5)
dp = st.sidebar.number_input("Diámetro Tubería (pulg)", value=5.0)

# 4. El Botón que activa todo
if st.button("GENERAR DIAGNÓSTICO TÉCNICO"):
    # Cálculos de Ingeniería
    pv = l600 - l300
    yp = l300 - pv
    va = (24.51 * caudal) / (dh**2 - dp**2)

    # 5. Visualización de Resultados Numéricos
    st.header("📈 Resultados del Análisis")
    c1, c2, c3 = st.columns(3)
    c1.metric("PV (Viscosidad Plástica)", f"{pv} cp")
    c2.metric("YP (Punto Cedente)", f"{yp} lb/100ft²")
    c3.metric("VA (Velocidad Anular)", f"{round(va, 2)} ft/min")

    st.divider()

    # 6. GRÁFICA TÉCNICA (Lo que le interesa al profesor)
    st.subheader("🚀 Monitor de Limpieza de Hoyo")
    
    # Creamos una tabla para la gráfica
    df_grafica = pd.DataFrame({
        'Parámetro': ['Tu Velocidad (VA)', 'Límite Crítico'],
        'Valor (ft/min)': [va, 120]
    })

    # Color verde si es seguro, rojo si es peligroso
    color_grafica = ["#00CC96" if va >= 120 else "#EF553B", "#636EFA"]

    fig = px.bar(df_grafica, 
                 x='Parámetro', 
                 y='Valor (ft/min)', 
                 color='Parámetro',
                 color_discrete_sequence=color_grafica,
                 text_auto='.2f')
    
    # Ajustes de la gráfica
    fig.update_layout(showlegend=False, height=400)
    
    st.plotly_chart(fig, use_container_width=True)

    # Mensaje de Criterio Técnico
    if va >= 120:
        st.success(f"✅ **ESTADO: OPERACIÓN SEGURA.** La VA ({round(va,2)}) supera el límite de acarreo.")
    else:
        st.error(f"⚠️ **ALERTA: LIMPIEZA DEFICIENTE.** Riesgo de embotamiento o atascamiento.")
else:
    st.info("Ajuste los valores en el panel izquierdo y presione el botón para ver las gráficas.")
