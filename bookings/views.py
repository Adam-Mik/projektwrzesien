from rest_framework import generics
from .models import Booking
from .serializers import BookingSerializer
from django.shortcuts import render


# Widok dla listy i tworzenia rezerwacji
class BookingListCreate(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# Widok dla szczegółów rezerwacji (pobieranie, edycja, usuwanie)
class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

def booking_list_view(request):
    return render(request, 'bookings/booking_list.html')