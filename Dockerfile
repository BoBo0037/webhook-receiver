FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 9999
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "9999"]
