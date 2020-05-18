# Using an official Python runtime as a parent image
FROM python:3.6-slim

# Defining environment variables
ENV GOOGLE_APPLICATION_CREDENTIALS=/botty/api/keys/google.json

# Sets the work directory to desired
WORKDIR /botty/

# Copy desired files into desired container's directory
COPY . /botty/api

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r api/requirements.txt

# Run api.py when the container launches
CMD ["python", "api/api.py"]