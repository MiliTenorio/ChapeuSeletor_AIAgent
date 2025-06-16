
# 🏰 Chapéu Seletor de Hogwarts 
### ✨ Um Agente de IA no Mundo Bruxo

Um mini app feito com **Streamlit** e **Ollama (Llama 3)** que simula o famoso **Chapéu Seletor** do universo de Harry Potter! Caso não tenha achado interessante, existem outros projetos no Git para os trouxas que possam estar lendo esse texto.
Nesse app você responde algumas perguntas... e o Chapéu, com toda sua sabedoria ancestral, te indica qual casa de Hogwarts combina mais com você! 🦁🐍🦅🦡

---

## ✨ Como funciona?

O usuário responde 4 perguntas sobre personalidade, atitudes e preferências.  
As respostas são enviadas como prompt para um modelo de linguagem (Llama 3 via Ollama).  
O modelo retorna a decisão do Chapéu, com explicações teatrais e dramáticas como nos filmes!  
O app exibe a casa sugerida com um destaque visual nas cores da casa (Grifinória, Sonserina, Corvinal ou Lufa-Lufa).

---

## 🚀 Tecnologias usadas

- [Streamlit](https://streamlit.io/) – para a interface web rápida e interativa
- [Ollama](https://ollama.com/) – para rodar o modelo Llama 3 localmente
- Python 🐍

---

## 💻 Como rodar localmente

### Pré-requisitos:
- Python 3.9+
- Ollama instalado e rodando (`ollama serve`)
- Modelo Llama 3 já baixado (`ollama pull llama3`)

### Passos:

```bash
# Clone o repositório
git clone https://github.com/SeuUsuario/chapel-seletor-hogwarts.git

# Instale as dependências
pip install -r requirements.txt

# Rode a aplicação
streamlit run app.py
```

---

## O App


---

## 📌 Próximos passos (ideias para evoluir):

- 🎨 Melhorias de visual com CSS customizado
- Adicionar novos agentes para criação de storytelling e gerador de um nome bruxo