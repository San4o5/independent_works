from google.cloud import storage
import os

def upload_file_to_bucket(bucket_name, source_file_name, destination_blob_name):
    # Створюємо клієнт для Google Cloud Storage
    client = storage.Client()
    
    # Отримуємо бакет, до якого будемо завантажувати файл
    bucket = client.bucket(bucket_name)
    
    # Створюємо об'єкт для завантаження файлу (blob) в цьому бакеті
    blob = bucket.blob(destination_blob_name)
    # Завантажуємо файл у бакет
    blob.upload_from_filename(source_file_name)
    
    print(f"Файл {source_file_name} завантажено як {destination_blob_name} у бакеті {bucket_name}.")
    
    