from .models import User, Category, Product
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