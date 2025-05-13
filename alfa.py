import streamlit as st
import random
import openai

# Inicializar
st.set_page_config(page_title="Ecuación de los Gases Ideales", layout="centered")
st.title("🌡️ Calculadora de Gases Ideales")

R = 0.0821  # Constante de los gases en L·atm/mol·K

def frase_inspiradora():
    frases = [
        "💡 ¡Cada paso que das te acerca a tu meta!",
        "🚀 ¡El conocimiento es poder, y tú lo estás conquistando!",
        "🌟 ¡Sigue así, estás haciendo un gran trabajo!",
        "📚 ¡Aprender es el primer paso hacia el éxito!",
        "🔥 ¡No hay límites cuando tienes determinación!"
    ]
    return random.choice(frases)

opcion = st.selectbox("¿Qué deseas calcular?", ["Selecciona...", "Presión (P)", "Volumen (V)", "Temperatura (T)", "Número de moles (n)"])

if opcion != "Selecciona...":
    st.subheader(f"Cálculo de {opcion}")

    if opcion == "Presión (P)":
        V = st.number_input("Volumen (L)", min_value=0.01)
        T = st.number_input("Temperatura (K)", min_value=0.01)
        n = st.number_input("Número de moles (mol)", min_value=0.01)
        if st.button("Calcular Presión"):
            P = (n * R * T) / V
            st.success(f"La presión es: {P:.2f} atm")
            st.info(frase_inspiradora())

    elif opcion == "Volumen (V)":
        P = st.number_input("Presión (atm)", min_value=0.01)
        T = st.number_input("Temperatura (K)", min_value=0.01)
        n = st.number_input("Número de moles (mol)", min_value=0.01)
        if st.button("Calcular Volumen"):
            V = (n * R * T) / P
            st.success(f"El volumen es: {V:.2f} L")
            st.info(frase_inspiradora())

    elif opcion == "Temperatura (T)":
        P = st.number_input("Presión (atm)", min_value=0.01)
        V = st.number_input("Volumen (L)", min_value=0.01)
        n = st.number_input("Número de moles (mol)", min_value=0.01)
        if st.button("Calcular Temperatura"):
            T = (P * V) / (n * R)
            st.success(f"La temperatura es: {T:.2f} K")
            st.info(frase_inspiradora())

    elif opcion == "Número de moles (n)":
        P = st.number_input("Presión (atm)", min_value=0.01)
        V = st.number_input("Volumen (L)", min_value=0.01)
        T = st.number_input("Temperatura (K)", min_value=0.01)
        if st.button("Calcular número de moles"):
            n = (P * V) / (R * T)
            st.success(f"El número de moles es: {n:.2f} mol")
            st.info(frase_inspiradora())

# Sección de ChatGPT
st.header("🤖 Pregúntale a ChatGPT")

pregunta = st.text_input("Escribe tu pregunta sobre cualquier tema:")
if st.button("Consultar"):
    openai.api_key = "TU_API_KEY"  # Reemplaza con tu API KEY real

    if pregunta:
        with st.spinner("Pensando..."):
            respuesta = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": pregunta}]
            )
            st.write(respuesta.choices[0].message['content'])
            st.info(frase_inspiradora())

# Sección de ejercicios
st.header("🧠 Practica con ejercicios")

nivel = st.selectbox("Selecciona dificultad", ["Fácil", "Intermedio", "Avanzado"])

def generar_ejercicio(nivel):
    if nivel == "Fácil":
        n, T, V = 1, 300, 10
    elif nivel == "Intermedio":
        n, T, V = 2, 350, 5
    else:
        n, T, V = 3, 400, 2

    P = (n * R * T) / V
    opciones = [round(P, 2), round(P*1.1, 2), round(P*0.9, 2)]
    random.shuffle(opciones)

    return {
        "enunciado": f"Calcula la presión (P) si n={n} mol, T={T} K y V={V} L",
        "opciones": opciones,
        "respuesta": round(P, 2)
    }

if st.button("Generar ejercicio"):
    ejercicio = generar_ejercicio(nivel)
    st.write(ejercicio["enunciado"])
    seleccion = st.radio("Elige una opción:", ejercicio["opciones"])
    if st.button("Verificar"):
        if seleccion == ejercicio["respuesta"]:
            st.success("✅ ¡Correcto!")
        else:
            st.error(f"❌ Incorrecto. La respuesta correcta es: {ejercicio['respuesta']} atm")
        st.info(frase_inspiradora())
