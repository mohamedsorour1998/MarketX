from rest_framework import generics, permissions, filters, status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User, Category, Product, Order, Checkout
from .serializers import UserSerializer, CategorySerializer, ProductSerializer, OrderSerializer, CheckoutSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException, AuthenticationFailed
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny


# Create your views here.
# this is the view for the user model
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny, )


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # using jwt token to authenticate
    # authentication_classes = (JWTAuthentication, )
    # permission_classes = (IsAuthenticated, )
    permission_classes = (permissions.AllowAny, )



# this is the view for the category model
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.AllowAny, )


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # using jwt token to authenticate
    permission_classes = (permissions.AllowAny, )


# this is the view for the product model
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny, )
    # adding filter and search functionality
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['category']
    search_fields = ['name', 'description']


class ProductSearch(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny, )
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny, )


# this is the view for the order model
# when  http://127.0.0.1:8000/my_ecommerce_api/users/1/orders/ is called,
# it will return all orders for user 1  and it will available only for user 1
class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    # using jwt token to authenticate
    # authentication_classes = (JWTAuthentication, )
    # permission_classes = (IsAuthenticated, )
    permission_classes = (permissions.AllowAny, )

    queryset = Order.objects.all()

    def get_queryset(self):
        # get the user id from the url
        user_id = self.kwargs['pk']
        # get the user object
        user = User.objects.get(id=user_id)
        # get all orders for this user
        orders = Order.objects.filter(user=user)
        return orders

    # def create(self, request, *args, **kwargs):
    #     # get the user id from the url
    #     user_id = self.kwargs['pk']
    #     # get the user object
    #     user = User.objects.get(id=user_id)
    #     # get the data from the request
    #     data = request.data
    #     # add the user to the data
    #     data['user'] = user.id
    #     # create the order
    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data,
    #                     status=status.HTTP_201_CREATED,
    #                     headers=headers)


class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # using jwt token to authenticate
    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated, )

    def retrieve(self, request, *args, **kwargs):
        # get the user id from the url
        user_id = self.kwargs['pk']
        # get the user object
        user = User.objects.get(id=user_id)
        # get the order id from the url
        order_id = self.kwargs['pk2']
        # get the order object
        order = Order.objects.get(id=order_id)
        # check if the order belongs to the user
        if order.user != user:
            return Response(
                {'error': 'You are not allowed to access this order'},
                status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(order)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        # get the user id from the url
        user_id = self.kwargs['pk']
        # get the user object
        user = User.objects.get(id=user_id)
        # get the order id from the url
        order_id = self.kwargs['pk2']
        # get the order object
        order = Order.objects.get(id=order_id)
        # check if the order belongs to the user
        if order.user != user:
            return Response(
                {'error': 'You are not allowed to access this order'},
                status=status.HTTP_403_FORBIDDEN)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance,
                                         data=request.data,
                                         partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        # get the user id from the url
        user_id = self.kwargs['pk']
        # get the user object
        user = User.objects.get(id=user_id)
        # get the order id from the url
        order_id = self.kwargs['pk2']
        # get the order object
        order = Order.objects.get(id=order_id)
        # check if the order belongs to the user
        if order.user == user:
            self.perform_destroy(order)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


# this is the view for the checkout model
# when  http://127.0.0.1:8000/my_ecommerce_api/users/1/orders/checkout is called,
# it will return all checkout details for user 1  and it will available only for user 1
class CheckoutListView(generics.ListAPIView):
    serializer_class = CheckoutSerializer

    # Using jwt token to authenticate
    # authentication_classes = (JWTAuthentication, )
    # permission_classes = (IsAuthenticated, )
    permission_classes = (permissions.AllowAny, )

    def get_queryset(self):
        # Get the user id from the url
        user_id = self.kwargs['pk']
        # Get all checkouts for this user
        checkouts = Checkout.objects.filter(user__id=user_id)
        
        return checkouts

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not queryset:
            return Response(
                {'error': 'You have no checkout data!'},
                status=status.HTTP_403_FORBIDDEN)
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# this is the view for the user
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


class UserProfile(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)