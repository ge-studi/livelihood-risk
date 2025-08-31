# Use a lightweight Python image
FROM python:3.11.9-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all code
COPY . .

# Expose port Render expects
EXPOSE 8000

# Start FastAPI app inside api folder
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
