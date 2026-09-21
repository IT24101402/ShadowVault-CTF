FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ .
USER 1000
EXPOSE 5000
CMD ["python", "app.py"]
