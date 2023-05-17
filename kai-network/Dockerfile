# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy the code files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "kai_network.py"]
