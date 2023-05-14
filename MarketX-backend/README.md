# Ecommerce API

This project is an ecommerce API built using Django Rest Framework (DRF) that allows users to browse and buy products online. The API supports secure user authentication using custom tokens and an `AbstractBaseUser` implementation. It also supports management of categories and products, and allows for Cross-Origin Resource Sharing (CORS).

## Demo

A working demo of the API can be hosted on a live server or presented through a video on a local environment. This is a link to the demo video: https://www.linkedin.com/feed/update/urn:li:activity:7049455662342234112/

## Key Features

1. User authentication using custom tokens and `AbstractBaseUser`
2. CORS support for cross-domain requests
3. Category management system
4. Product catalog with search and filter functionality
5. User management system
6. Checkout functionality

## Requirements

1. Django Rest Framework (DRF)
2. PostgreSQL database
3. django-cors-headers

## Installation

1. Clone the repository:

```
git clone https://github.com/your_username/your_repository.git
```

2. Change to the project directory:

```
cd your_project_directory
```

3. Create a virtual environment and activate it:

```
python3 -m venv venv
source venv/bin/activate
```

4. Install the required packages:

```
pip install -r requirements.txt
```

5. Set up the PostgreSQL database (refer to the [official documentation](https://www.postgresql.org/docs/current/tutorial-install.html) for installation instructions).

6. Update the `DATABASES` setting in `settings.py` with your PostgreSQL database credentials:

```python
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
```

7. Enable CORS by adding `'corsheaders.middleware.CorsMiddleware'` to your `MIDDLEWARE` in `settings.py` and configuring the `CORS_ALLOWED_ORIGINS` setting:

```python
INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]

MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://www.example.com",
]
```

8. Run the initial migrations:

```
python manage.py migrate
```

9. Start the development server:

```
python manage.py runserver
```

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

* Obtain a custom token pair: `POST /token/`
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

This README servesas a user manual and technical documentation for the project. Please refer to the [Django documentation](https://docs.djangoproject.com/en/stable/) and the [Django Rest Framework documentation](https://www.django-rest-framework.org/) for further information on working with Django and DRF, respectively.

For implementing `AbstractBaseUser`, consult the [official Django documentation on custom user models](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#substituting-a-custom-user-model). Additionally, you may want to check out the [Django Rest Framework SimpleJWT documentation](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html) for information on working with token-based authentication.

For the `django-cors-headers` library, consult the [official documentation](https://github.com/adamchainz/django-cors-headers) for more information on CORS and how to configure it properly in your project.