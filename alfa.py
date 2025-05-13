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
            "R = 0.0821 L·atm/mol·K es la constante unive
