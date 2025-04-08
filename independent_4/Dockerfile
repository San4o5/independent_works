
FROM python:latest

WORKDIR /usr/src/app/

COPY requirements.txt ./

RUN pip install -r requirements.txt

# Копіюємо весь проект в контейнер
COPY . .

RUN ["python"]
