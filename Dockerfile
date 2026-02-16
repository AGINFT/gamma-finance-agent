FROM python:3.11-slim

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir flask google-generativeai

# Copy application
COPY . .

# Expose A2A port
EXPOSE 8000

# Set entrypoint
ENTRYPOINT ["python", "src/a2a_server.py"]
CMD ["--host", "0.0.0.0", "--port", "8000"]
