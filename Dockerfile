# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.7-slim

COPY requirements.txt ./

# Install production dependencies.
RUN pip install -r requirements.txt

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip install Flask gunicorn

# Run the web service on container startup.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
