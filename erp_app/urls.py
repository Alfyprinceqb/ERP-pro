from django.urls import path
from .views import*

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

    path('api/users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('api/employees/add/', AddUserView.as_view(), name='add-employee'),

    path('vendors/', VendorView.as_view(), name='vendor-list-create'),
    path('vendors/<int:pk>/', VendorView.as_view(), name='vendor-detail'),
    
    path('api/product-category/', ProductCategoryView.as_view(), name='product_category_list'),
    path('api/product-category/<int:pk>/', ProductCategoryView.as_view(), name='product_category_detail'),

    path('products/', ProductView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductView.as_view(), name='product_detail'),
]
