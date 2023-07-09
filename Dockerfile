# Use a Python base image
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script and movie descriptions file to the container
COPY watch_next.py .
COPY movies.txt .

# Run the watch_next.py script when the container starts
CMD ["python", "watch_next.py"]
