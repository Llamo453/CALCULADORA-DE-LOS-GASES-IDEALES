import streamlit as st
import random
st.image("QUÍMICA.png")
# Constante universal de los gases
R = 0.0821  # atm·L/mol·K

st.set_page_config(page_title="Calculadora de Gases Ideales", layout="centered")

st.title("💨 Calculadora de la Ecuación de los Gases Ideales")
st.markdown("Resuelve **PV = nRT** seleccionando qué variable deseas calcular.")

opcion = st.selectbox("¿Qué variable deseas calcular?", ["Presión (P)", "Volumen (V)", "Temperatura (T)", "Número de moles (n)"])

# Entrada de datos según la variable elegida
if opcion == "Presión (P)":
    V = st.number_input("Volumen (L)", min_value=0.01)
    T = st.number_input("Temperatura (K)", min_value=0.01)
    n = st.number_input("Número de moles (mol)", min_value=0.01)
    if st.button("Calcular Presión"):
        P = (n * R * T) / V
        st.success(f"La presión es {P:.2f} atm")
elif opcion == "Volumen (V)":
    P = st.number_input("Presión (atm)", min_value=0.01)
    T = st.number_input("Temperatura (K)", min_value=0.01)
    n = st.number_input("Número de moles (mol)", min_value=0.01)
    if st.button("Calcular Volumen"):
        V = (n * R * T) / P
        st.success(f"El volumen es {V:.2f} L")
elif opcion == "Temperatura (T)":
    P = st.number_input("Presión (atm)", min_value=0.01)
    V = st.number_input("Volumen (L)", min_value=0.01)
    n = st.number_input("Número de moles (mol)", min_value=0.01)
    if st.button("Calcular Temperatura"):
        T = (P * V) / (n * R)
        st.success(f"La temperatura es {T:.2f} K")
elif opcion == "Número de moles (n)":
    P = st.number_input("Presión (atm)", min_value=0.01)
    V = st.number_input("Volumen (L)", min_value=0.01)
    T = st.number_input("Temperatura (K)", min_value=0.01)
    if st.button("Calcular Número de moles"):
        n = (P * V) / (R * T)
        st.success(f"El número de moles es {n:.2f} mol")

# Función para mostrar frases inspiradoras
def frase_inspiradora():
    frases = [
        "🌟 ¡Sigue adelante, estás aprendiendo algo poderoso!",
        "🚀 El conocimiento es la llave para conquistar el universo.",
        "💡 Cada problema resuelto es un paso más hacia tu meta.",
        "🔥 ¡Eres más capaz de lo que imaginas!",
        "🌱 Hoy ciencia, mañana logros extraordinarios."
    ]
    st.markdown(random.choice(frases))

frase_inspiradora()

# Funcionalidad de preguntas (modo IA)
with st.expander("❓ Haz una pregunta libre"):
    pregunta = st.text_input("Escribe tu duda aquí:")
    if st.button("Responder"):
        # Esto se puede conectar a una IA más adelante
        st.info("📌 Por ahora, esta función es un espacio para escribir tus dudas.")
        st.markdown("👉 ¡Muy pronto incorporaremos respuestas inteligentes!")
        frase_inspiradora()

# Ejercicios interactivos
st.subheader("🎯 Practica con ejercicios")
nivel = st.selectbox("Selecciona dificultad:", ["Fácil", "Intermedio", "Avanzado"])

if st.button("Generar ejercicio"):
    def generar_ejercicio(nivel):
        if nivel == "Fácil":
            T = 300
            n = 1
            V = 10
        elif nivel == "Intermedio":
            T = 400
            n = 2
            V = 15
        else:  # Avanzado
            T = 500
            n = 3
            V = 20
        P = round((n * R * T) / V, 2)
        opciones = [P, round(P + 0.5, 2), round(P - 0.5, 2)]
        random.shuffle(opciones)
        return T, n, V, P, opciones

    T, n, V, P_real, opciones = generar_ejercicio(nivel)
    st.markdown(f"Calcula la presión (P) sabiendo que:")
    st.markdown(f"- Temperatura = {T} K")
    st.markdown(f"- Número de moles = {n} mol")
    st.markdown(f"- Volumen = {V} L")

    respuesta = st.radio("¿Cuál es la presión?", opciones)

    if st.button("Verificar respuesta"):
        if respuesta == P_real:
            st.success("✅ ¡Correcto!")
        else:
            st.error(f"❌ Incorrecto. La respuesta correcta es {P_real} atm.")
        frase_inspiradora()
