# VULN-76: Using latest tag - unpinned base image
FROM python:latest

# VULN-77: Running as root (no USER directive)
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# VULN-78: Exposing unnecessary ports
EXPOSE 5000 8080 22 3306

# VULN-79: No health check defined
# VULN-80: Debug server used in production
CMD ["python", "app.py"]
