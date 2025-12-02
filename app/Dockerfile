# Use a small base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app.py .

# Environment variables
ENV APP_ENV=dev
ENV APP_MESSAGE="Hello from Kubernetes! 🚀"
ENV PORT=5000

# Expose the port Flask runs on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]