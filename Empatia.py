import streamlit as st
from openai import OpenAI
from PIL import Image

# Sayfa ayarları
st.set_page_config(
    page_title="Empatia",
    page_icon="logo.png",
    layout="centered"
)

# Logo
logo = Image.open("logo.png")
st.image(logo, width=180)

# Başlık
st.title("Empatia")
st.subheader("Yargılamadan dinleyen dijital arkadaşın.")

# Groq bağlantısı
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
  api_key="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"
)

# Sohbet geçmişi
if "messages" not in st.session_state:
    st.session_state.messages = []

# Önceki mesajları göster
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kullanıcı mesajı
prompt = st.chat_input("Bugün nasıl hissediyorsun?")

# Önceki mesajları göster
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt:

    # Kullanıcı mesajını göster
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Sistem promptu
    mesajlar = [
        {
            "role": "system",
            "content": """
Sen Empatia'sın.

İnsanlara eşlik eden dijital bir arkadaşsın.

Kurallar:
- Türkçe konuş.
- Samimi ol.
- Kısa ve anlaşılır cevaplar ver.
- İnsanları yargılama.
- Duygusal destek sun.
- Bilgi sorularına doğru cevap ver.
- Bilmediğin bilgileri uydurma.
- Gereksiz uzun cevaplar verme.
"""
        }
    ]

    mesajlar.extend(st.session_state.messages)

    with st.chat_message("assistant"):

        with st.spinner("Empatia düşünüyor..."):

            cevap = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=mesajlar
            )

            yanit = cevap.choices[0].message.content

            st.markdown(yanit)

    st.session_state.messages.append(
        {"role": "assistant", "content": yanit}
    )

# Alt bilgi
st.markdown("---")

st.markdown(
    """
    <div style='text-align:center; color:gray;'>
    ❤️ Her zaman yanımda olan, en çok bu başarıyı hak eden<br>
    <b>Annem ve Babama, EMİŞ SULTANIMA ❤️</b>
    </div>
    """,
    unsafe_allow_html=True
)