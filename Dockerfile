# 1. Use an official, lightweight Python base image
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy just the requirements file first (good for caching layers)
COPY requirements.txt .

# 4. Install the Python dependencies inside the container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your application code into the container
COPY main.py .

# 6. Tell Docker to expose port 8000
EXPOSE 8000

# 7. Command to run the app using uvicorn when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]