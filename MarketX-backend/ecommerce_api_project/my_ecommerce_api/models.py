from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

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


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    date_ordered = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " ordered:  " + self.product.name


class Checkout(models.Model):

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    order = models.OneToOneField(Order, on_delete=models.DO_NOTHING, null=True)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    product = models.CharField(max_length=50, null=True)
    quantity = models.IntegerField(null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=50, default='Credit Card')

    def save(self, *args, **kwargs):
        # get user address details from the user model
        self.address = self.user.address
        self.city = self.user.city
        self.state = self.user.state
        self.zip_code = self.user.zip_code
        self.country = self.user.country
        # get user orders details from the order model
        self.product = self.order.product.name
        self.quantity = self.order.quantity
        self.date_ordered = self.order.date_ordered
        self.is_complete = self.order.is_complete
        # this is to save the checkout model
        super(Checkout, self).save(*args, **kwargs)


#  this is to create a checkout model when an order is created
@receiver(post_save, sender=Order)
def create_checkout(sender, instance, created, **kwargs):
    if created:
        Checkout.objects.create(order=instance, user=instance.user)


# this is to delete the checkout model when an order is delete
@receiver(post_delete, sender=Order)
def delete_checkout(sender, instance, **kwargs):
    instance.checkout.delete()


# this is to update the checkout model when an order is updated
@receiver(post_save, sender=Order)
def update_checkout(sender, instance, **kwargs):
    instance.checkout.save()