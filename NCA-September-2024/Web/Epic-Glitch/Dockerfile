# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 1331 for Flask
EXPOSE 3113

# Define environment variable for Flask
ENV FLASK_APP=app.py

# Run the Flask app
# CMD ["flask", "run", "--host=0.0.0.0", "--port=3113"]
CMD ["gunicorn", "--bind", "0.0.0.0:3113", "app:app"]