# Ecommerce API

This project is an ecommerce API built using Django Rest Framework (DRF) that allows users to browse and buy products 
online. The API supports secure user authentication using tokens and allows users to manage categories and products.

## Demo

A working demo of the API can be hosted on a live server or presented through a video on a local environment.
this is a link to the demo video: https://www.linkedin.com/feed/update/urn:li:activity:7049455662342234112/

## Key Features

1. User authentication using tokens
2. Category management system
3. Product catalog with search and filter functionality
4. User management system
5. Checkout functionality

## Requirements

1. Django Rest Framework (DRF)
2. PostgreSQL database

## Installation

1. Clone the repository:

git clone https://github.com/mohamedsorour1998/MarketX.git


2. Change to the project directory:

cd MarketX-backend/ecommerce_api_project/


3. Create a virtual environment and activate it:

python3 -m venv venv
source venv/bin/activate


4. Install the required packages:

pip install -r requirements.txt


5. Set up the PostgreSQL database (refer to the [official documentation](https://www.postgresql.org/docs/current/tutorial-install.html) for installation instructions).

6. Update the `DATABASES` setting in `settings.py` with your PostgreSQL database credentials:
python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


7. Run the initial migrations:

python manage.py migrate


8. Start the development server:

python manage.py runserver


## API Endpoints

### Users

* List and create users: `GET, POST /users/`
* Retrieve, update, and delete a specific user: `GET, PUT, DELETE /users/<int:pk>/`
* List and create orders for a specific user: `GET, POST /users/<int:pk>/orders/`
* Retrieve, update, and delete a specific order: `GET, PUT, DELETE /users/<int:pk>/orders/<int:pk2>/`
* List and create checkouts for a specific user: `GET, POST /users/<int:pk>/orders/checkout/`

### Categories

* List and create categories: `GET, POST /categories/`
* Retrieve, update, and delete a specific category: `GET, PUT, DELETE /categories/<int:pk>/`

### Products

* List and create products, also filter them by category: `GET, POST /products/`
* Search for products by keyword: `GET /products/search/`
* Retrieve, update, and delete a specific product: `GET, PUT, DELETE /products/<int:pk>/`

### Authentication

* Obtain a token pair: `POST /token/`
* Refresh a token: `POST /token/refresh/`

## Models

### User

* `first_name`
* `last_name`
* `email`
* `password`
* `phone`
* `address`
* `city`
* `state`
* `zip_code`
* `country`
* `date_joined`
* `last_login`
* `is_staff`

### Category

* `name`
* `description`

### Product

* `name`
* `description`
* `price`
* `category` (foreign key to Category)

### Order

* `user` (foreign key to User)
* `product` (foreign key to Product)
* `quantity`
* `date_ordered`
* `is_complete`

### Checkout

* `user` (foreign key to User)
* `order` (one-to-one field with Order)
* `address`
* `city`
* `state`
* `zip_code`
* `country`
* `product`
* `quantity`
* `date_ordered`
* `is_complete`
* `payment_method`


## Documentation

This README serves as a user manual and technical documentation for the project.
