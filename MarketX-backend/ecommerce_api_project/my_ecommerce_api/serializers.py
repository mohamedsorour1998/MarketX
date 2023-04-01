from .models import User, Category, Product, Order, Checkout
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # make the category field as name instead of id
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    # make order, user and product fields as name instead of id
    User = serializers.StringRelatedField()
    Product = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = '__all__'
        
class CheckoutSerializer(serializers.ModelSerializer):
    # make order, user and product fields as name instead of id
    User = serializers.StringRelatedField()
    Product = serializers.StringRelatedField()

    class Meta:
        model = Checkout
        fields = '__all__'