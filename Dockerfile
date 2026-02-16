FROM python:3.11-slim

WORKDIR /app

# Copy application files
COPY requirements.txt .
COPY .gamma .gamma/
COPY src src/
COPY MASTER_INDEX.json .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Set environment
ENV PYTHONUNBUFFERED=1

# Run server
CMD ["python", "src/a2a_server.py", "--host", "0.0.0.0", "--port", "8000"]
