# Use official Python image
FROM python:3.12-slim

# Label to specify the source repository for this image (used by GitHub Container Registry)
LABEL org.opencontainers.image.source=https://github.com/egshiglen2024359/capstone-project

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set work directory in container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .

# Install system dependencies
RUN apt-get update && \
    apt-get install -y gcc libpq-dev netcat-traditional && \
    # Install Python dependencies
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*
    
# Copy Django project files into container
COPY . .

# Make entrypoint executable
RUN chmod +x /app/entrypoint.sh

# Expose port
EXPOSE 8000

# Run the development server
ENTRYPOINT [ "/app/entrypoint.sh" ]