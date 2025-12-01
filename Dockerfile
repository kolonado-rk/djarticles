# Dockerfile
FROM python:3.12-slim

# Neinteraktívny režim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# systémové dependency (psycopg2, build tools)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# pracovný adresár v kontajneri
WORKDIR /app

# requirements
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# skopíruj celý projekt
COPY . /app/

# default port (pre runserver / gunicorn)
EXPOSE 8000

# default command – pre istotu, ale v docker-compose si ho prebijeme
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]