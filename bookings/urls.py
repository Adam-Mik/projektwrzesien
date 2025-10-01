from django.urls import path
from .views import BookingListCreate, BookingDetail, booking_list_view, booking_create

urlpatterns = [
    path('', booking_list_view, name='booking-list'),
    # Adres dla listy rezerwacji (np. /api/bookings/)
    path('api/', BookingListCreate.as_view(), name='booking-list-create'),
    # Adres dla szczegółów rezerwacji (np. /api/bookings/1/)
    # path('<int:pk>/', BookingDetail.as_view(), name='booking-detail'),
    path('<int:pk>/', booking_create, name='booking-create'),
]