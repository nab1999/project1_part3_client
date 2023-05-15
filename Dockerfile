FROM python:3.9-alpine

# Set working directory
WORKDIR /app

# Install necessary packages
RUN apk update && apk add --no-cache \
    openssl \
    && rm -rf /var/cache/apk/*

# Copy client application code
COPY client.py .

# Set volume
VOLUME ["/clientdata"]

# Start client
CMD ["python", "client.py"]

