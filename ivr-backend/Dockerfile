# Build stage
FROM python:3.12-slim AS builder

WORKDIR /build

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Production stage
FROM python:3.12-slim AS production

WORKDIR /app

# Create non-root user
RUN groupadd --system --gid 1001 pythongroup && \
    useradd --system --gid 1001 --uid 1001 --shell /bin/bash --create-home pythonuser

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application code
COPY --chown=1001:1001 . /app

# Switch to non-root user
USER 1001:1001

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/api/v1/health')" || exit 1

# Run with gunicorn for production
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000", "app.main:app", "--workers", "4"]