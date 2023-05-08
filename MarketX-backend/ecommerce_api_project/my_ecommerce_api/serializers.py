from .models import User, Category, Product, Order, Checkout
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        extra_kwargs = {'password': {'write_only': True}}
        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            address=validated_data['address'],
            phone=validated_data['phone'],
            city=validated_data['city'],
            state=validated_data['state'],
            zip_code=validated_data['zip_code'],
            country=validated_data['country'],
            email=validated_data['email'],
            password=make_password(validated_data['password']),
        )
        user.save()
        return user


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
