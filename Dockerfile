FROM python:3.11-slim

WORKDIR /app

# Create a limited non-root user and group
RUN groupadd -r fastuser && useradd -r -g fastuser fastuser

COPY --chown=fastuser:fastuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=fastuser:fastuser main.py .

# Switch away from root privilege
USER fastuser

EXPOSE 8000

# NEW: Add container health checking layer
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8000/ || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]