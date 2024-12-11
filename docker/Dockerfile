# Dockerfile
FROM python:3.10

WORKDIR /app
COPY backend/requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY backend/ .

EXPOSE 5000
CMD ["python", "app.py"]
