from django.db import models

# Create your models here.
"""
Project Description:

The project is to create an ecommerce API using Django Rest Framework (DRF) that allows users to browse and buy products online. The API should be secure and allow users to authenticate using tokens, and manage categories and products.

Key Features:

	1-User authentication using tokens
	2-Category management system
	3-Product catalog with search and filter functionality
	4-User management system
	5-Checkout functionality
	
Requirements:

	1-The project should be built using Django Rest Framework (DRF) and use PostgreSQL database.
	2 User authentication should be implemented using token-based authentication, and the tokens should expire after an hour.
	3-Users should be able to browse products by categories and search for specific products using keywords.
	4- Categories should be managed through DRF's API endpoints.
	5- Products should be able to be added, edited and deleted through DRF's API endpoints.
	6- Users should be able to create an account, update their profile, and view their order history through DRF's API endpoints.
	7 -The checkout system should collect user information, shipping details, and payment information through DRF's API endpoints.



Deliverables:

	Source code and project documentation.
	A working demo of the API hosted on a live server OR (video on local environment in case you have not a host)
	User manual and technical documentation.
	Presentation of the project to the evaluation committee. (not required based on the need)
"""


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
# make the category show as the name of the category instead of the id
# from django.db import models

