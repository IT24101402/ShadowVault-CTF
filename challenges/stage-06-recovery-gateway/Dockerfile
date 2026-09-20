FROM python:3.12-slim

RUN useradd -m vaultuser

WORKDIR /app

RUN pip install --no-cache-dir flask

COPY app.py .

RUN chown -R vaultuser:vaultuser /app

USER vaultuser

EXPOSE 5000

CMD ["python", "app.py"]
