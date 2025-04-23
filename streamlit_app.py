import streamlit as st
import requests
import json
from deep_translator import GoogleTranslator

def load_image():
    uploaded_file = st.file_uploader(label='Выберите изображение для распознавания', type=["png", "jpg"])
    if uploaded_file is not None:
        return uploaded_file
    else:
        return None

st.title('Распознай текст и переведи его с русского на английский язык!')
img = load_image()

def ocr_space_file(uploaded_file, overlay=False, api_key='helloworld', language='rus'):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    response = requests.post(
        'https://api.ocr.space/parse/image',
        files={uploaded_file.name: uploaded_file.getbuffer()},
        data=payload,
    )
    return json.loads(f"{response.content.decode()}")["ParsedResults"][0]["ParsedText"]


def translate_text(text):
    return GoogleTranslator(source='auto', target='en').translate(text)

result = st.button('Распознать изображение')
if result:
    text = ocr_space_file(img, False, "K87431946488957", "rus")
    st.write('**Результаты распознавания:**')
    st.write("Текст до перевода:")
    st.write(text)
    text = translate_text(text)
    st.write("Текст после перевода:")
    st.write(text)
