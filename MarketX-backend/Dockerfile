# creating a dockerfile for the app backend
FROM python:3.8.5-slim-buster
# set the working directory in the container
WORKDIR /app-backend
# copy the dependencies file to the working directory
COPY /ecommerce_api_project/requirements.txt .
# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# copy the content of the local src directory to the working directory
COPY /ecommerce_api_project .
# Expose port 8000 to the outside world
EXPOSE 8000
# start the app
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8080"]
