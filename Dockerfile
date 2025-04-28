FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files to the container
COPY . /app

# Install required dependencies (if any)
# RUN pip install -r requirements.txt   # Uncomment if you have a requirements.txt

# Set the entry point to run the calculator script
ENTRYPOINT ["python", "calculator.py"]
