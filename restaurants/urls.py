from django.urls import include, path
from .views import (
    RestaurantDetailAPIView,
    RestaurantList,
    TableList,
    TableDetail,
    restaurant_list_view,
    table_list_view,
)
from . import views
from rest_framework.routers import DefaultRouter

# 1. Utworzenie Routera
router = DefaultRouter()

# 2. Rejestracja ViewSetów
# Router automatycznie wygeneruje wszystkie standardowe ścieżki RESTful (GET, POST, PUT/PATCH, DELETE)
# pod prefiksem 'api/'.

# Endpoint: /api/restaurants/
router.register(r'restaurants', views.RestaurantViewSet, basename='restaurant')

# # Endpoint: /api/tables/
# router.register(r'tables', views.TableViewSet, basename='table')

# # Endpoint: /api/bookings/
# router.register(r'bookings', views.BookingViewSet, basename='booking')

urlpatterns = [
    # Frontend routes
    path('', restaurant_list_view, name='home'),
    path('tables/', table_list_view, name='table-view'),

    # API routes
    path('api/restaurants/', RestaurantList.as_view(), name='restaurant-list'),
    path('api/restaurants/<int:pk>/', RestaurantDetailAPIView.as_view(), name='restaurant-detail-api'),
    path('api/tables/', TableList.as_view(), name='table-list'),
    path('api/tables/<int:pk>/', TableDetail.as_view(), name='table-detail'),
    path('api/', include(router.urls)),
    
    # New post method
    path('', views.restaurants_table, name='restaurant_table'),
    path('restaurants/add', views.restaurants, name='restaurant_list_create'),
    path('restaurants/update/<id>', views.update_restaurant, name='update_restaurant'),
    path('restaurants/delete/<id>', views.delete_restaurant, name='delete_restaurant'),
    path('<int:pk>/', views.restaurant_detail_view, name='restaurant_detail'),
]