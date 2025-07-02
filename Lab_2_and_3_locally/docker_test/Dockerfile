# Dockerfile

# 1. Use an official Python runtime as a parent image.
# The 'slim' version is a smaller, more minimal base image.
FROM python:3.9-slim

# 2. Set the working directory inside the container to /app.
# This is where our application code will live.
WORKDIR /app

# 3. Copy the dependency file into the container.
# We copy this first to leverage Docker's layer caching.
# If requirements.txt doesn't change, this layer won't be rebuilt.
COPY requirements.txt .

# 4. Install any needed packages specified in requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application source code into the container.
COPY . .

# 6. Expose port 5000.
# This informs Docker that the container listens on this port.
# This is for documentation; it doesn't actually publish the port.
EXPOSE 5000

# 7. Define the command to run your app.
# This will be executed when the container starts.
CMD ["python", "app.py"]