# Using an official Python runtime as a parent image
FROM python:3.6-slim

# Sets the work directory to desired
WORKDIR /smart/

# Copy desired files into desired container's directory
COPY . /smart/bot

# Creating a directory to hold saved voice files
RUN mkdir storage && mkdir storage/voices

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r bot/requirements.txt

# Run bot.py when the container launches
CMD ["python", "bot/bot.py"]