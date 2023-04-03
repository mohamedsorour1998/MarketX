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
