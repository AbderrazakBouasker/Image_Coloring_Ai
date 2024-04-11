# Use a base image with Python and CUDA support
FROM nvidia/cuda:11.4.0-base

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required packages
RUN apt update && apt install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt
RUN gdown 1j__QripZ4wBX0ABgsiGi6B3VfWLCsGO3
RUN gdown 1jrEiEaWNNZMwjGxJw0yr5voKaMeo0IP-

# Copy the application code
COPY . .

# Expose the Flask port
EXPOSE 5000

# Set the entrypoint command
CMD ["python3", "app.py"]
