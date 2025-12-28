FROM python:3.9-slim AS builder

WORKDIR /app/backend

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 

COPY  . /app/backend/

FROM python:3.9-slim

WORKDIR /app/backend

# Python stores most of its package installations in this path
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# Copy the source code
COPY --from=builder /app/backend /app/backend

EXPOSE 8000

CMD python /app/backend/manage.py runserver 0.0.0.0:8000