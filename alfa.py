import streamlit as st
import random

# Constante universal de los gases
R = 0.0821  # L·atm/mol·K

st.set_page_config(page_title="Ley de Gases Ideales", page_icon="🧪", layout="centered")

st.title("🧪 Calculadora de la Ley de Gases Ideales")
st.markdown("Resuelve **PV = nRT** con unidades estándar:\n\n"
            "- Presión: atm\n"
            "- Volumen: litros\n"
            "- Temperatura: Kelvin\n"
            "- Cantidad de sustancia: mol")

# Selección de variable a calcular
opcion = st.selectbox("¿Qué variable deseas calcular?", ["Presión (P)", "Volumen (V)", "Temperatura (T)", "Moles (n)"])

def frase_inspiradora():
    frases = [
        "✨ ¡Sigue explorando, el conocimiento es infinito!",
        "💪 ¡Cada intento te acerca más al éxito!",
        "🚀 ¡El universo premia la curiosidad!",
        "🎯 ¡Aprender ciencia es conquistar el mundo!",
        "📘 ¡Nunca dejes de aprender, estás brillando!"
    ]
    return random.choice(frases)

def resolver_ecuacion(opcion, V=None, T=None, n=None, P=None):
    if opcion == "Presión (P)":
        return (n * R * T) / V
    elif opcion == "Volumen (V)":
        return (n * R * T) / P
    elif opcion == "Temperatura (T)":
        return (P * V) / (n * R)
    elif opcion == "Moles (n)":
        return (P * V) / (R * T)

# Mostrar campos según selección
if opcion == "Presión (P)":
    V = st.number_input("Volumen (L)", min_value=0.01)
    T = st.number_input("Temperatura (K)", min_value=0.01)
    n = st.number_input("Cantidad de sustancia (mol)", min_value=0.01)
    if st.button("Calcular Presión"):
        P = resolver_ecuacion(opcion, V=V, T=T, n=n)
        st.success(f"Presión = {P:.3f} atm\n\n{frase_inspiradora()}")

elif opcion == "Volumen (V)":
    P = st.number_input("Presión (atm)", min_value=0.01)
    T = st.number_input("Temperatura (K)", min_value=0.01)
    n = st.number_input("Cantidad de sustancia (mol)", min_value=0.01)
    if st.button("Calcular Volumen"):
        V = resolver_ecuacion(opcion, P=P, T=T, n=n)
        st.success(f"Volumen = {V:.3f} L\n\n{frase_inspiradora()}")

elif opcion == "Temperatura (T)":
    P = st.number_input("Presión (atm)", min_value=0.01)
    V = st.number_input("Volumen (L)", min_value=0.01)
    n = st.number_input("Cantidad de sustancia (mol)", min_value=0.01)
    if st.button("Calcular Temperatura"):
        T = resolver_ecuacion(opcion, P=P, V=V, n=n)
        st.success(f"Temperatura = {T:.3f} K\n\n{frase_inspiradora()}")

elif opcion == "Moles (n)":
    P = st.number_input("Presión (atm)", min_value=0.01)
    V = st.number_input("Volumen (L)", min_value=0.01)
    T = st.number_input("Temperatura (K)", min_value=0.01)
    if st.button("Calcular Moles"):
        n = resolver_ecuacion(opcion, P=P, V=V, T=T)
        st.success(f"Moles = {n:.3f} mol\n\n{frase_inspiradora()}")

# Chat de dudas
st.markdown("---")
st.subheader("❓ ¿Tienes una duda?")
pregunta = st.text_input("Escribe tu pregunta sobre la ley de gases ideales")

if pregunta:
    # Aquí podrías conectar con una IA o FAQ estático
    st.info("📘 Esta fórmula es útil cuando se conoce 3 de las 4 variables: Presión, Volumen, Temperatura y Moles.\n"
            "R = 0.0821 L·atm/mol·K es la constante universal en estas unidades.")
    st.write(frase_inspiradora())

# Ejercicios
st.markdown("---")
st.subheader("🧠 Ejercicios de práctica")
nivel = st.selectbox("Selecciona nivel de dificultad", ["Fácil", "Intermedio", "Avanzado"])

def generar_ejercicio(nivel):
    if nivel == "Fácil":
        P, V, T = 1.0, 22.4, 273
        n_correcta = round((P * V) / (R * T), 2)
        opciones = [n_correcta, n_correcta + 0.5, n_correcta - 0.5]
        random.shuffle(opciones)
        pregunta = f"¿Cuántos moles hay si P=1 atm, V=22.4 L, T=273 K?"
        return pregunta, opciones, n_correcta

    elif nivel == "Intermedio":
        P, n, T = 2.0, 0.5, 300
        V_correcto = round((n * R * T) / P, 2)
        opciones = [V_correcto, V_correcto + 2, V_correcto - 2]
        random.shuffle(opciones)
        pregunta = f"¿Cuál es el volumen si P=2 atm, n=0.5 mol, T=300 K?"
        return pregunta, opciones, V_correcto

    elif nivel == "Avanzado":
        V, n, T = 10.0, 1.2, 350
        P_correcta = round((n * R * T) / V, 2)
        opciones = [P_correcta, P_correcta + 1, P_correcta - 1]
        random.shuffle(opciones)
        pregunta = f"¿Cuál es la presión si V=10 L, n=1.2 mol, T=350 K?"
        return pregunta, opciones, P_correcta

ejercicio, opciones, respuesta_correcta = generar_ejercicio(nivel)
st.write(ejercicio)
respuesta_usuario = st.radio("Selecciona una opción", opciones)

if st.button("Verificar respuesta"):
    if respuesta_usuario == respuesta_correcta:
        st.success(f"✅ ¡Correcto! {frase_inspiradora()}")
    else:
        st.error(f"❌ Incorrecto. La respuesta correcta era: {respuesta_correcta} {frase_inspiradora()}")

