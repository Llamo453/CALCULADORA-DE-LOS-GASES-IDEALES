import streamlit as st
import random

R = 0.0821  # L·atm/mol·K

st.set_page_config(page_title="Calculadora de Gases Ideales", layout="centered")

st.title("🌡️ Calculadora de la Ecuación de los Gases Ideales")
st.markdown("La ecuación universal es: **PV = nRT**")

opcion = st.selectbox("¿Qué variable deseas calcular?", ["Selecciona...", "Presión (P)", "Volumen (V)", "Temperatura (T)", "Número de moles (n)"])

def frase_inspiradora():
    frases = [
        "✨ ¡Sigue adelante, cada paso te acerca a tu meta!",
        "🚀 ¡Nunca subestimes el poder de tu esfuerzo!",
        "🌟 ¡Estás haciendo un gran trabajo!",
        "🔥 ¡El conocimiento es poder, sigue aprendiendo!",
        "💡 ¡Cada error es una nueva oportunidad para aprender!"
    ]
    return random.choice(frases)

def calcular():
    if opcion == "Presión (P)":
        V = st.number_input("Volumen (L)", min_value=0.01)
        n = st.number_input("Número de moles (mol)", min_value=0.01)
        T = st.number_input("Temperatura (K)", min_value=0.01)
        if st.button("Calcular Presión"):
            P = (n * R * T) / V
            st.success(f"La presión es {P:.2f} atm")
            st.info(frase_inspiradora())

    elif opcion == "Volumen (V)":
        P = st.number_input("Presión (atm)", min_value=0.01)
        n = st.number_input("Número de moles (mol)", min_value=0.01)
        T = st.number_input("Temperatura (K)", min_value=0.01)
        if st.button("Calcular Volumen"):
            V = (n * R * T) / P
            st.success(f"El volumen es {V:.2f} L")
            st.info(frase_inspiradora())

    elif opcion == "Temperatura (T)":
        P = st.number_input("Presión (atm)", min_value=0.01)
        n = st.number_input("Número de moles (mol)", min_value=0.01)
        V = st.number_input("Volumen (L)", min_value=0.01)
        if st.button("Calcular Temperatura"):
            T = (P * V) / (n * R)
            st.success(f"La temperatura es {T:.2f} K")
            st.info(frase_inspiradora())

    elif opcion == "Número de moles (n)":
        P = st.number_input("Presión (atm)", min_value=0.01)
        V = st.number_input("Volumen (L)", min_value=0.01)
        T = st.number_input("Temperatura (K)", min_value=0.01)
        if st.button("Calcular Número de moles"):
            n = (P * V) / (R * T)
            st.success(f"El número de moles es {n:.2f} mol")
            st.info(frase_inspiradora())

calcular()

st.markdown("---")
st.subheader("🤖 ¿Tienes una duda?")
pregunta = st.text_input("Escribe tu pregunta:")

if st.button("Buscar en Google"):
    if pregunta:
        query = pregunta.replace(" ", "+")
        st.markdown(f"[Buscar '{pregunta}' en Google](https://www.google.com/search?q={query})")
    else:
        st.warning("Por favor escribe una pregunta.")
    st.info(frase_inspiradora())

st.markdown("---")
st.subheader("🧠 Generador de Ejercicios")

nivel = st.selectbox("Selecciona el nivel de dificultad:", ["Fácil", "Intermedio", "Avanzado"])

def generar_ejercicio():
    n = round(random.uniform(0.5, 3.0), 2)
    T = round(random.uniform(250, 350), 2)
    V = round(random.uniform(5.0, 20.0), 2)
    P_real = round((n * R * T) / V, 2)
    opciones = sorted([P_real, P_real + random.uniform(0.1, 1.0), P_real - random.uniform(0.1, 1.0)])
    random.shuffle(opciones)

    st.write(f"Calcula la presión (P) dada la siguiente información:")
    st.write(f"- Volumen: {V} L")
    st.write(f"- Temperatura: {T} K")
    st.write(f"- Número de moles: {n} mol")

    respuesta = st.radio("Selecciona la respuesta correcta (atm):", opciones)

    if st.button("Verificar respuesta"):
        if abs(respuesta - P_real) < 0.1:
            st.success("✅ ¡Correcto!")
        else:
            st.error(f"❌ Incorrecto. La respuesta correcta es {P_real:.2f} atm")
        st.info(frase_inspiradora())

if nivel != "":
    generar_ejercicio()
