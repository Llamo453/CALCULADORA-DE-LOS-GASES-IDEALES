import streamlit as st
from PIL import Image

# Constante universal de los gases
R = 0.0821  # L·atm/mol·K

st.set_page_config(page_title="Ecuación de Gases Ideales", layout="centered")

st.title("🌡️ Calculadora de la Ecuación de los Gases Ideales")
st.markdown("**PV = nRT**")

# Imagen ilustrativa
st.image("https://upload.wikimedia.org/wikipedia/commons/9/9b/Ideal_gas_law_diagram.svg", caption="Ley del Gas Ideal", use_column_width=True)

opcion = st.selectbox("¿Qué variable deseas calcular?", ["Selecciona una opción", "Presión (P)", "Volumen (V)", "Temperatura (T)", "Número de moles (n)"])

if opcion == "Presión (P)":
    V = st.number_input("Volumen (L)", min_value=0.001)
    n = st.number_input("Número de moles (mol)", min_value=0.001)
    T = st.number_input("Temperatura (K)", min_value=0.001)
    if st.button("Calcular Presión"):
        P = (n * R * T) / V
        st.success(f"La presión es: {P:.3f} atm")
        st.info("💡 Cada molécula cuenta, ¡igual que cada uno de tus esfuerzos!")

elif opcion == "Volumen (V)":
    P = st.number_input("Presión (atm)", min_value=0.001)
    n = st.number_input("Número de moles (mol)", min_value=0.001)
    T = st.number_input("Temperatura (K)", min_value=0.001)
    if st.button("Calcular Volumen"):
        V = (n * R * T) / P
        st.success(f"El volumen es: {V:.3f} L")
        st.info("📈 Tu conocimiento se expande igual que un gas ideal.")

elif opcion == "Temperatura (T)":
    P = st.number_input("Presión (atm)", min_value=0.001)
    V = st.number_input("Volumen (L)", min_value=0.001)
    n = st.number_input("Número de moles (mol)", min_value=0.001)
    if st.button("Calcular Temperatura"):
        T = (P * V) / (n * R)
        st.success(f"La temperatura es: {T:.3f} K")
        st.info("🔥 ¡Tu mente brilla más que el calor de una reacción!")

elif opcion == "Número de moles (n)":
    P = st.number_input("Presión (atm)", min_value=0.001)
    V = st.number_input("Volumen (L)", min_value=0.001)
    T = st.number_input("Temperatura (K)", min_value=0.001)
    if st.button("Calcular Número de moles"):
        n = (P * V) / (R * T)
        st.success(f"El número de moles es: {n:.3f} mol")
        st.info("🧪 Cada paso que das te acerca a la solución.")

# Footer
st.markdown("---")
st.caption("Creado con ❤️ usando Streamlit - ¡Sigue explorando la ciencia!")

