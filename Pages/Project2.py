import streamlit as st
import cv2
import tempfile
import numpy as np
from pathlib import Path
from yt_dlp import YoutubeDL

class Project2:
    def __init__(self):
        self.cap = None  # Переменная для хранения VideoCapture

    def app(self):
        st.title('Видео или камера')

        # Выбор источника видео
        source_option = st.selectbox(
            "Выберите источник видео",
            ("Камера телефона", "YouTube ссылка", "Локальный файл", "Веб-камера", "RTSP поток")
        )

        # Переменная для URL или устройства
        video_url = None
        img_file = None  # Для камеры телефона

        # Проверка выбранного источника
        if source_option == "Камера телефона":
            img_file = st.camera_input("Сделайте снимок с камеры")

        elif source_option == "YouTube ссылка":
            youtube_url = st.text_input("Введите YouTube ссылку")
            if youtube_url:
                # Используем yt_dlp для загрузки видео
                with st.spinner("Загружается видео с YouTube..."):
                    try:
                        ydl_opts = {"format": "best", "noplaylist": True}
                        with YoutubeDL(ydl_opts) as ydl:
                            info_dict = ydl.extract_info(youtube_url, download=False)
                            video_url = info_dict.get("url", None)
                    except Exception as e:
                        st.error(f"Не удалось загрузить видео: {e}")

        elif source_option == "Локальный файл":
            video_file = st.file_uploader("Загрузите видеофайл", type=["mp4", "avi", "mov"])
            if video_file:
                # Сохраняем файл временно для использования в OpenCV
                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=Path(video_file.name).suffix)
                temp_file.write(video_file.read())
                video_url = temp_file.name

        elif source_option == "Веб-камера":
            video_url = 0  # Подключение к веб-камере на порте 0

        elif source_option == "RTSP поток":
            rtsp_url = st.text_input("Введите RTSP ссылку")
            if rtsp_url:
                video_url = rtsp_url

        # Кнопка для запуска видео
        run_button = st.button("Запустить")
        frame_place = st.empty()  # Место для показа видео

        # Если выбрана камера телефона и есть изображение
        if source_option == "Камера телефона" and img_file is not None:
            file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
            frame = cv2.imdecode(file_bytes, 1)
            st.image(frame, channels="BGR")  # Показываем изображение

        # Запуск потока с других источников
        elif run_button and video_url is not None:
            self.cap = cv2.VideoCapture(video_url)

            # Проверка подключения
            if not self.cap.isOpened():
                st.error("Не удалось подключиться к источнику видео.")
            else:
                # Кнопка для остановки видео
                stop_button = st.button("Остановить")

                # Чтение и показ кадров
                while self.cap.isOpened() and not stop_button:
                    ret, frame = self.cap.read()
                    if not ret:
                        st.write("Видео недоступно")
                        break

                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame_place.image(frame, channels="RGB")

                    #cv2.waitKey(1) & 0xFF == ord("q") or stop_button:
                    if stop_button:
                        break

                # Освобождение ресурсов после остановки
                self.cap.release()
                cv2.destroyAllWindows()

# Создаем и запускаем приложение
app = Project2()
app.app()
