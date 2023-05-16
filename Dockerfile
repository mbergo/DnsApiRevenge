# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required Python dependencies
RUN pip install -r requirements.txt

# Copy the project files to the container
COPY . .

# Expose the port on which your API runs
EXPOSE 5000

# Set the entry point command to run the API
CMD ["python", "app.py"]
