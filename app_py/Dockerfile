FROM python:alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app_py

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt 

COPY . .

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "wsgi"]
