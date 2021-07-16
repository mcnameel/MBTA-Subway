# The alpine images are the best when it comes to start up time and size on disk, this one comes preloaded with python
FROM python:3.8-alpine

# Copy and install the external python libraries
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the source code
COPY ./src /src

# Set source as working dir
WORKDIR /src

# Set the app to run on port 5000 and start the app
EXPOSE 5000
CMD python main/server.py '/run/secrets/db-password'