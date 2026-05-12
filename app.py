import streamlit as st

# Configuración visual de la aplicación
st.set_page_config(page_title="FluidMaster Pro", page_icon="💧", layout="wide")

# Estilos para que se vea más profesional
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #0284c7; color: white; font-weight: bold; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

st.title("💧 FluidMaster Pro: Ingeniería de Lodos")
st.write("Software especializado en Reología e Hidráulica de Perforación")
st.divider()

# Layout de columnas para la entrada de datos
col_input1, col_input2 = st.columns(2)

with col_input1:
    st.subheader("📊 Datos del Viscosímetro")
    l600 = st.number_input("Lectura a 600 RPM", value=40.0, step=0.1)
    l300 = st.number_input("Lectura a 300 RPM", value=25.0, step=0.1)
    densidad = st.number_input("Densidad del Lodo (ppg)", value=9.5, step=0.1)

with col_input2:
    st.subheader("🏗️ Geometría del Pozo")
    diam_hoyo = st.number_input("Diámetro del Hoyo (pulg)", value=8.5, step=0.1)
    diam_tubo = st.number_input("Diámetro ext. Tubería (pulg)", value=5.0, step=0.1)
    caudal = st.number_input("Caudal de Bombeo (GPM)", value=300.0, step=10.0)

st.divider()

# Botón para ejecutar el software
if st.button("GENERAR DIAGNÓSTICO OPERATIVO"):
    # --- MOTOR DE CÁLCULO ---
    # Reología (Modelo de Bingham)
    pv = l600 - l300
    yp = l300 - pv
    
    # Hidráulica (Velocidad Anular)
    # VA = (24.51 * Q) / (Dh^2 - Dp^2)
    va = (24.51 * caudal) / (diam_hoyo**2 - diam_tubo**2)
    
    # --- MOSTRAR RESULTADOS ---
    st.write("### Resultados Técnicos")
    res1, res2, res3 = st.columns(3)
    
    res1.metric("Viscosidad Plástica (PV)", f"{pv} cp")
    res2.metric("Punto Cedente (YP)", f"{yp} lb/100ft²")
    res3.metric("Velocidad Anular (VA)", f"{round(va, 2)} ft/min")
    
    st.divider()
    
    # Evaluación de Seguridad
    if va >= 120:
        st.success("✅ **ESTADO: OPERACIÓN SEGURA.** La velocidad anular es suficiente para el acarreo de ripios.")
    else:
        st.error("⚠️ **ALERTA DE SEGURIDAD.** Velocidad anular por debajo del límite crítico (120 ft/
