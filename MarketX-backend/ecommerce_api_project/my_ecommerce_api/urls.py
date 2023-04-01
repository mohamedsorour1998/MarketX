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
from django.urls import path, include
from .views import UserListCreateView, UserRetrieveUpdateDestroyView, CategoryListCreateView, CategoryRetrieveUpdateDestroyView, ProductListCreateView, ProductRetrieveUpdateDestroyView, OrderListCreateView, OrderRetrieveUpdateDestroyView, CheckoutListView
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/',
         UserRetrieveUpdateDestroyView.as_view(),
         name='user-detail'),
    path('users/<int:pk>/orders/',
         OrderListCreateView.as_view(),
         name='order-list'),
    path('users/<int:pk>/orders/<int:pk2>/',
         OrderRetrieveUpdateDestroyView.as_view(),
         name='order-detail'),
    path('users/<int:pk>/orders/checkout/',
         CheckoutListView.as_view(),
         name='checkout-list'),
    path('categories/', CategoryListCreateView.as_view(),
         name='category-list'),
    path('categories/<int:pk>/',
         CategoryRetrieveUpdateDestroyView.as_view(),
         name='category-detail'),
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/',
         ProductRetrieveUpdateDestroyView.as_view(),
         name='product-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
