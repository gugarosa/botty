# Using an official Python runtime as a parent image
FROM python:3.6-slim

# Sets the work directory to desired
WORKDIR /botty/

# Copy desired files into desired container's directory
COPY . /botty/bot

# Creating a directory to hold saved voice files and saved transcripts
RUN mkdir storage && mkdir storage/voices && mkdir storage/transcripts

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r bot/requirements.txt

# Run bot.py when the container launches
CMD ["python", "bot/bot.py"]