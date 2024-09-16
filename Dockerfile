FROM python:3.12.5-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /django

# Install Pillow before copying requirements.txt
RUN python -m pip install Pillow
RUN apk add --no-cache postgresql-client

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Add your superuser creation script to the Docker image
COPY create_superuser.py /django/