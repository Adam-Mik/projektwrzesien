from django.urls import path
from .views import (
    BookingListCreate, 
    BookingDetail, 
    TableListAPIView, 
    UserListAPIView,
    booking_list_view, 
    booking_create, 
    calendar_data_feed
    )

urlpatterns = [
    path('', booking_list_view, name='booking-list'),
    # Adres dla listy rezerwacji (np. /api/bookings/)
    path('api/', BookingListCreate.as_view(), name='booking-list-create'),
    # path('<int:pk>/', booking_create, name='booking-create'),
    path('<int:restaurant_pk>/calendar-feed/', calendar_data_feed, name='calendar_data_feed'),
    path('api/<int:restaurant_pk>/tables/', TableListAPIView.as_view(), name='table-list-api'),
    path('api/users/', UserListAPIView.as_view(), name='user-list-api'),
]