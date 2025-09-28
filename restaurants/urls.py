from django.urls import path
from .views import (
    RestaurantList,
    RestaurantDetail,
    TableList,
    TableDetail,
    restaurant_list_view,
    table_list_view
)

urlpatterns = [
    # Frontend routes
    path('', restaurant_list_view, name='home'),
    path('tables/', table_list_view, name='table-view'),

    # API routes
    path('api/restaurants/', RestaurantList.as_view(), name='restaurant-list'),
    path('api/restaurants/<int:pk>/', RestaurantDetail.as_view(), name='restaurant-detail'),
    path('api/tables/', TableList.as_view(), name='table-list'),
    path('api/tables/<int:pk>/', TableDetail.as_view(), name='table-detail'),
]