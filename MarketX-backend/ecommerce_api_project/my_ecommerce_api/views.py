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
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User, Category, Product, Order, Checkout
from .serializers import UserSerializer, CategorySerializer, ProductSerializer, OrderSerializer, CheckoutSerializer
from rest_framework import generics, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.response import Response


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
    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated, )


# this is the view for the category model
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.AllowAny, )


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # using jwt token to authenticate
    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated, )


# this is the view for the product model
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny, )
    # adding filter and search functionality
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category']
    SearchFilter = ['name', 'description']


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # using jwt token to authenticate
    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated, )


# this is the view for the order model
# when  http://127.0.0.1:8000/my_ecommerce_api/users/1/orders/ is called,
# it will return all orders for user 1  and it will available only for user 1
class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    # using jwt token to authenticate
    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated, )
    queryset = Order.objects.all()

    def get_queryset(self):
        # get the user id from the url
        user_id = self.kwargs['pk']
        # get the user object
        user = User.objects.get(id=user_id)
        # get all orders for this user
        orders = Order.objects.filter(user=user)
        return orders

    def create(self, request, *args, **kwargs):
        # get the user id from the url
        user_id = self.kwargs['pk']
        # get the user object
        user = User.objects.get(id=user_id)
        # get the data from the request
        data = request.data
        # add the user to the data
        data['user'] = user.id
        # create the order
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)


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

    # using jwt token to authenticate
    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        # get the user id from the url
        user_id = self.kwargs['pk']
        # get the user object
        user = User.objects.get(id=user_id)
        # get all orders for this user
        orders = Order.objects.filter(user=user)
        # get all checkouts for this user
        checkouts = Checkout.objects.filter(order__in=orders)
        # check if the order belongs to the user if so return the checkout
        if checkouts:
            return checkouts
        else:
            return Response(
                {'error': 'You are not allowed to access this checkout'},
                status=status.HTTP_403_FORBIDDEN)
