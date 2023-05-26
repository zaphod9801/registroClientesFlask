# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install the application
RUN pip install -e .

# Move into app directory (where your Python files are)
WORKDIR /app/app

# Create the database tables and seed data
RUN python set_db.py

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run run.py when the container launches
CMD ["python", "run.py"]

