# Base image
FROM python:3.11-slim

## Essential environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Working directory
WORKDIR /app

## Installing system dependancies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

## Copying ur all contents from local to app
COPY . .

## Run setup.py
RUN pip install --no-cache-dir -e .

# Expose port
EXPOSE 8080

# Run the app
CMD ["uvicorn", "app.main:app", "--server.port=8080", "--server.address=0.0.0.0","--server.headless=true"]
