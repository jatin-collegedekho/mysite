# Use an official Python runtime as the base image
FROM python:3.10
# install vim editor
RUN apt-get update -y
RUN apt install uwsgi-plugin-python3 -y
RUN ["apt-get", "update"]

RUN ["apt-get", "install", "-y", "vim"]
# Set the working directory
RUN mkdir /code
WORKDIR /code


# Copy the requirements file
COPY requirements.txt .


# Install the dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose the port for the Django development server
EXPOSE 8000

# Set the environment variable for the mysite settings

# Run the Django development server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
