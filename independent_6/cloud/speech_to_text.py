from google.cloud import speech
from google.cloud.speech import RecognitionAudio, RecognitionConfig
import subprocess
import os

def convert_to_wav_ffmpeg(input_path, output_path="temp_audio.wav"):
    # Конвертує аудіофайл в формат WAV за допомогою ffmpeg
    result = subprocess.run([
        "ffmpeg", "-y", "-i", input_path, "-ar", "16000", "-ac", "1", output_path
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        raise RuntimeError(f"Помилка ffmpeg при конвертації: {result.stderr.decode()}")

    return output_path

def transcribe_audio(audio_path):
    # Конвертуємо файл у wav
    wav_path = convert_to_wav_ffmpeg(audio_path)
    
    with open(wav_path, "rb") as audio_file:
        content = audio_file.read()
        
    if not content:
        raise ValueError("Аудіофайл порожній або нечитабельний!")
    
    # Використовуємо Google Speech API для транскрипції
    client = speech.SpeechClient()
    
    # Створюємо об'єкт аудіо для транскрипції
    audio = RecognitionAudio(content=content)
    
    # Налаштовуємо конфігурацію для транскрипції (мова, частота дискретизації)
    config = RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="uk-UA", # (українська)
        sample_rate_hertz = 16000
    )
    # Викликаємо метод API для транскрипції
    response = client.recognize(config=config, audio=audio)
    
    # Об'єднуємо отримані результати транскрипції
    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript + " "
    
     # Видаляємо тимчасовий WAV файл після транскрипції
    if os.path.exists(wav_path):
        os.remove(wav_path)
        
    return transcript.strip()
