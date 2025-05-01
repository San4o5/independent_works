from google.cloud import storage
import os

def upload_file_to_bucket(bucket_name, source_file_name, destination_blob_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    
    blob.upload_from_filename(source_file_name)
    print(f"Файл {source_file_name} завантажено як {destination_blob_name} у бакеті {bucket_name}.")
    
    