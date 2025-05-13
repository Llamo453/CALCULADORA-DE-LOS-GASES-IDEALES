import streamlit as st
import random

# Constante de los gases ideales en atm·L/mol·K
R = 0.0821

st.set_page_config(page_title="Calculadora de Gases Ideales", layout="centered")
st.title("💨 Calculadora de la Ecuación de los Gases Ideales")
st.markdown("**PV = nRT**")

# Frases motivadoras
frases = [
    "🚀 ¡Cada cálculo te acerca más a la excelencia!",
    "🌟 ¡Nunca dejes de aprender, lo estás haciendo increíble!",
    "💡 La ciencia es el puente hacia un futuro mejor.",
    "🔥 ¡Estás a un paso de dominar la química!",
    "💪 ¡El conocimiento es tu mejor herramienta!",
]

# Selección de variable a calcular
opcion = st.selectbox("¿Qué variable deseas calcular?", ["Presión (P)", "Volumen (V)", "Temperatura (T)", "Número de moles (n)"])

def mostrar_resultado(variable, resultado, unidades):
    st.success(f"✅ {variable} calculado: {resultado:.3f} {unidades}")
    st.markdown(f"**{random.choice(frases)}**")

if opcion == "Presión (P)":
    V = st.number_input("Volumen (L)", min_value=0.01)
    n = st.number_input("Número de moles (mol)", min_value=0.01)
    T = st.number_input("Temperatura (K)", min_value=0.01)
    if st.button("Calcular Presión"):
        P = (n * R * T) / V
        mostrar_resultado("Presión", P, "atm")

elif opcion == "Volumen (V)":
    P = st.number_input("Presión (atm)", min_value=0.01)
    n = st.number_input("Número de moles (mol)", min_value=0.01)
    T = st.number_input("Temperatura (K)", min_value=0.01)
    if st.button("Calcular Volumen"):
        V = (n * R * T) / P
        mostrar_resultado("Volumen", V, "L")

elif opcion == "Temperatura (T)":
    P = st.number_input("Presión (atm)", min_value=0.01)
    V = st.number_input("Volumen (L)", min_value=0.01)
    n = st.number_input("Número de moles (mol)", min_value=0.01)
    if st.button("Calcular Temperatura"):
        T = (P * V) / (n * R)
        mostrar_resultado("Temperatura", T, "K")

elif opcion == "Número de moles (n)":
    P = st.number_input("Presión (atm)", min_value=0.01)
    V = st.number_input("Volumen (L)", min_value=0.01)
    T = st.number_input("Temperatura (K)", min_value=0.01)
    if st.button("Calcular Número de moles"):
        n = (P * V) / (R * T)
        mostrar_resultado("Número de moles", n, "mol")

st.divider()

# ChatGPT integrador (simulado)
st.subheader("🤖 Pregúntale a ChatGPT")
pregunta = st.text_input("Escribe tu duda aquí:")
if st.button("Preguntar a ChatGPT"):
    st.info(f"🧠 Respuesta simulada: '{pregunta}' es una gran pregunta. Investiga conceptos como presión, volumen y temperatura. ¡Sigue aprendiendo!")
    st.markdown(f"**{random.choice(frases)}**")

st.divider()

# Generador de ejercicios
st.subheader("📚 Generador de ejercicios para practicar")
nivel = st.selectbox("Selecciona nivel de dificultad", ["Fácil", "Intermedio", "Avanzado"])

def generar_ejercicio(nivel):
    if nivel == "Fácil":
        n, T, V = 1, 300, 24.6
        P = round((n * R * T) / V, 2)
        return f"¿Cuál es la presión (atm) si n={n} mol, T={T} K y V={V} L?", P
    elif nivel == "Intermedio":
        n, T, P = 2, 350, 1.5
        V = round((n * R * T) / P, 2)
        return f"¿Cuál es el volumen (L) si n={n} mol, T={T} K y P={P} atm?", V
    else:
        V, T, P = 10, 500, 2
        n = round((P * V) / (R * T), 3)
        return f"¿Cuántos moles hay si V={V} L, T={T} K y P={P} atm?", n

if st.button("Generar ejercicio"):
    pregunta, respuesta = generar_ejercicio(nivel)
    st.write(pregunta)
    opciones = [respuesta, round(respuesta * 0.9, 2), round(respuesta * 1.1, 2)]
    random.shuffle(opciones)
    seleccion = st.radio("Elige tu respuesta:", opciones)
    if seleccion == respuesta:
        st.success("✅ ¡Correcto!")
    else:
        st.error(f"❌ Incorrecto. La respuesta correcta era {respuesta}")
    st.markdown(f"**{random.choice(frases)}**")
