import streamlit as st #Устанавливаем библиотеку streamlit и объявляем её под именем st (библиотека для создания интерфейса)
import requests #Устанавливаем библоитеку для отправки запросов с помощью API
import json #Импортируем библиотеку для конвертирования объектов в формате JSON
from deep_translator import GoogleTranslator #Импортируем библиотеку для перевода текста

def load_image(): #Функция для загрузки изображения через интерфейс
    uploaded_file = st.file_uploader(label='Выберите изображение для распознавания', type=["png", "jpg"]) #Создаем файловый загрузчик с фильтром форматов PNG/JPG
    if uploaded_file is not None: #Проверяем наличие загруженного файла
        return uploaded_file #Возвращаем загруженный файл
    else:
        return None #Если файла нет, то возвращаем значение None

st.title('Распознай текст и переди его с русского на английский язык!') #Устанавливаем заголовок веб-приложения
img = load_image() #Загружаем изображение через нашу функцию

def ocr_space_file(uploaded_file, overlay=False, api_key='helloworld', language='rus'): #Функция для распознавания текста через API OCR.Space
    payload = {'isOverlayRequired': overlay, #Задаём параметры запроса: наложение текста,  
               'apikey': api_key, #API-ключ,
               'language': language, #Язык распознавания
               }
    response = requests.post( #Отправка POST-запроса к API с файлом и параметрами
        'https://api.ocr.space/parse/image', #End point запроса
        files={uploaded_file.name: uploaded_file.getbuffer()}, #Передаем файл как бинарные данные
        data=payload, #Добавляем параметры запроса
    )
    return json.loads(f"{response.content.decode()}")["ParsedResults"][0]["ParsedText"] #Парсинг JSON-ответа и извлечение распознанного текста


def translate_text(text): #Функция для перевода текста с русского на английский
    return GoogleTranslator(source='auto', target='en').translate(text) #Возвращем переведённый текст

result = st.button('Распознать изображение') #Создаем кнопку для запуска обработки
if result: #Если кнопка нажата (result = True)
    text = ocr_space_file(img, False, "K87431946488957", "rus") #Вызываем OCR-функцию (передаем изображение, API-ключ-заглушку и язык)
    st.write('**Результаты распознавания:**') #Выводим текст в скобках
    st.write("Текст до перевода:") #Выводим текст в скобках
    st.write(text) #Выводим распознанный текст
    text = translate_text(text) #Вызываем функцию для перевода, распознанного текста
    st.write("Текст после перевода:") #Выводим текст в скобках
    st.write(text) #Выводим текст после перевода
