FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy backend dependencies first
COPY backend/requirements.txt /app/requirements.txt

# Install Python deps with longer timeout and retries and fallback mirror
RUN pip install --default-timeout=100 --retries=5 --no-cache-dir -r /app/requirements.txt || \
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r /app/requirements.txt

# Copy the backend source code
COPY backend /app/backend

# Ensure Python can find "backend" package
ENV PYTHONPATH=/app

# Run the FastAPI app
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
