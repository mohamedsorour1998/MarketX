from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(
        default=True)
    is_staff = models.BooleanField(default=False)
    username = None

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name', 'last_name', 'address', 'phone', 'city', 'state',
        'zip_code', 'country'
    ]

    def __str__(self):
        return self.first_name + " " + self.last_name

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_staff

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return self.first_name + " " + self.last_name


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image_link = models.URLField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image_link = models.URLField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_ordered = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " ordered:  " + self.product.name


class Checkout(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    product = models.CharField(max_length=50, null=True)
    quantity = models.IntegerField(null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=50, default='Cash On Delivery')

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
