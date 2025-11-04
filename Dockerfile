# ---- Base Image ----
FROM python:3.12-slim

# ---- System deps ----
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on

WORKDIR /app

# ---- Install OS packages ----
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# ---- Python deps ----
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# ---- Copy project ----
COPY . .

# ---- Collect static (optional, for production) ----
RUN python manage.py collectstatic --noinput

# ---- Expose port ----
EXPOSE 8000

# ---- Run Gunicorn ----
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]