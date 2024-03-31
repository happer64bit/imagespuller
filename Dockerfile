# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all files from the current directory to the container's working directory
COPY . .

# Run setup.py to build and install the package
RUN pip install -r requirements.txt && \
    python setup.py build && \
    python setup.py install && \
    python examples/test.py
