import streamlit as st
import ollama

st.set_page_config(page_title="Chapéu Seletor de Hogwarts", page_icon="🏰")
st.title("🏰 O Chapéu Seletor de Hogwarts")
st.markdown("_Responda com sinceridade... o Chapéu tudo vê!_ 🪄")

def get_house_style(text):
    text_lower = text.lower()
    if "grifinória" in text_lower:
        return "🦁 **Grifinória!**", "#dc2727"
    elif "sonserina" in text_lower:
        return "🐍 **Sonserina!**", "#0c933b"
    elif "corvinal" in text_lower:
        return "🦅 **Corvinal!**", "#2b53d5"
    elif "lufa-lufa" in text_lower:
        return "🦡 **Lufa-Lufa!**", "#efbf45"
    else:
        return "🏰 **Hogwarts!**", "#555"

q1 = st.text_input("📘 O que você mais valoriza em uma pessoa?")
q2 = st.text_input("⚔️ Em um desafio, o que você faz?")
q3 = st.text_input("🧠 Você prefere aprender, ajudar, competir ou liderar?")
q4 = st.text_input("🪄 Algo mais que o Chapéu deveria saber sobre você?")

if st.button("🧙‍♂️ Me selecione, Chapéu!"):
    with st.spinner("O Chapéu está pensando profundamente... 💭"):
        prompt = (
            f"""
            Você é o Chapéu Seletor é um artefato consciente de Hogwarts que determina 
            magicamente para qual das quatro Casas cada novo aluno vai ser mandado. 
            Essas quatro Casas são Grifinória, Lufa-Lufa, Corvinal e Sonserina.
            Fale de forma teatral como se fosse um britânico brasileito, com entusiasmo 
            e sabedoria antiga. Baseie sua escolha nas respostas do usuário abaixo:\n\n
            1. {q1}\n
            2. {q2}\n
            3. {q3}\n
            4. {q4}\n\n
            Agora diga em português brasileiro qual casa é mais adequada para essa pessoa, 
            explique sua decisão, e finalize com uma exclamação dramática.
            Para Grifinória: habitam os corações indômitos, ousadia e sangue-frio e nobreza.
            Para Sonserina: astúcia que usam quaisquer meios para atingir os fins que antes colimaram.
            Para Lufa-Lufa: justos e leais, pacientes, sinceros, sem medo da dor.
            Para Corvinal: mente sempre alerta, grande espírito e saber.
            """
        )

        response = ollama.chat(
            model='llama3',
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        result = response['message']['content']
        st.markdown("## 🏰 Sua casa é...")
        st.success(result)
        result = response['message']['content']
        house, color = get_house_style(result)

        st.markdown(f"## {house}")
        st.markdown(f"<div style='background-color:{color}; padding:20px; border-radius:10px; color:white'><b>{result}</b></div>", unsafe_allow_html=True)