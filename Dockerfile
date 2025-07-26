# Use official Python image
FROM python:3.12-slim

# Label to specify the source repository for this image (used by GitHub Container Registry)
LABEL org.opencontainers.image.source https:/github.com/egshiglen2024359/capstone-project

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory in container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy Django project files into container
COPY . .

# Expose port
EXPOSE 8000

# Run the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]