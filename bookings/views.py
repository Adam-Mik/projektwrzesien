from rest_framework import generics
from .models import Booking, Table
from restaurants.models import Restaurant 
from django.contrib.auth import get_user_model
from .serializers import BookingSerializer
from django.shortcuts import render, redirect, get_object_or_404


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

User = get_user_model() 

def booking_create(request, pk):
    restaurant_obj = get_object_or_404(Restaurant, pk=pk)
    all_users = User.objects.all()
    available_tables = Table.objects.filter(restaurant=restaurant_obj)

    if request.method == 'POST':
        data = request.POST
        
        # LOGIKA POBIERANIA UŻYTKOWNIKA (MUSI TU BYĆ)
        user_id = data.get('user') 
        try:
            # DEFINIOWANIE ZMIENNEJ selected_user
            selected_user = User.objects.get(pk=user_id) 
        except User.DoesNotExist:
            # Możesz dodać obsługę błędu, jeśli ID użytkownika jest błędne
            return redirect('home')
        
        table_id = data.get('table')
        # Pamiętaj o obsłudze braku stolika, jeśli nie używasz get_object_or_404()
        selected_table = get_object_or_404(Table, pk=table_id) 

        # Dane czasowe i goście
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        number_of_guests = data.get('number_of_guests')

        Booking.objects.create(
            user=selected_user,         # <--- Zmienna jest teraz zdefiniowana!
            restaurant=restaurant_obj,
            table=selected_table, 
            start_time=start_time,
            end_time=end_time,
            number_of_guests=number_of_guests,
        )
        return redirect('home')

    context = {
        'restaurant': restaurant_obj,
        'all_users': all_users,
        'available_tables': available_tables
    }
    return render(request, 'bookings/booking_form.html', context)