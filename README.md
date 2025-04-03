# 📖 Сайт для распознавания текста и его перевода - Документация

## 📌 Описание проекта

Это веб-приложение позволяет:
1. Загружать изображения с текстом (PNG/JPG)
2. Распознавать текст на изображении с помощью API OCR.Space
3. Автоматически переводить распознанный текст с русского на английский
4. Отображать результаты распознавания и перевода

## 🌟 Особенности

- Простой и интуитивно понятный интерфейс
- Быстрое распознавание текста
- Качественный перевод через Google Translate API
- Не требует сохранения файлов на сервере

## 📦 Используемые библиотеки

| Библиотека | Назначение | Версия |
|------------|------------|--------|
| streamlit | Создание веб-интерфейса | >=1.44.1 |
| requests | Отправка HTTP-запросов к API OCR.Space | >=2.32.3 |
| json | Обработка JSON-ответов от API | встроенная |
| deep-translator | Перевод текста через Google Translate | >=1.11.4 |

## 🚀 Быстрый старт

### Установка зависимостей

pip install streamlit requests deep-translator

### Запуск приложения

streamlit run main.py

### Использование

1. Нажмите "Browse files" и выберите изображение с текстом
2. Нажмите кнопку "Распознать изображение"
3. Дождитесь обработки (обычно занимает несколько секунд)
4. Просмотрите результаты:
   - Исходный распознанный текст
   - Переведенный текст

## ⚙️ Настройка API ключа

По умолчанию используется тестовый ключ API OCR.Space. Для production использования:

1. Получите свой API ключ на [OCR.Space](https://ocr.space/ocrapi)
2. Замените строку:
   
   text = ocr_space_file(img, False, "КЛЮЧ", "rus")
   
   на:
   
   text = ocr_space_file(img, False, "ВАШ_КЛЮЧ", "rus")
   

## 🌍 Поддерживаемые языки

### Распознавание текста
Измените параметр language в вызове ocr_space_file():
- rus - русский
- eng - английский
- [Другие языки](https://ocr.space/ocrapi)

### Перевод текста
Измените параметры в GoogleTranslator:
GoogleTranslator(source='auto', target='en')  # 'en' замените на нужный язык

## 🤝 Как внести вклад

1. Форкните репозиторий
2. Создайте ветку с новым функционалом (git checkout -b feature/AmazingFeature)
3. Зафиксируйте изменения (git commit -m 'Add some AmazingFeature')
4. Запушьте в ветку (git push origin feature/AmazingFeature)
5. Откройте Pull Request
