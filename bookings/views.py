from rest_framework import generics
from .models import Booking, Table
from restaurants.models import Restaurant 
from django.contrib.auth import get_user_model
from .serializers import BookingSerializer, TableSerializer, UserSerializer
from django.shortcuts import render, redirect, get_object_or_404

from django.http import JsonResponse

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


def calendar_data_feed(request, restaurant_pk):
    # Używamy restaurant_pk zamiast pk dla spójności z URL
    bookings = Booking.objects.filter(restaurant_id=restaurant_pk)
    
    events = []
    for booking in bookings:
        events.append({
            'title': f"Stolik {booking.table.pk} (Zajęty)", 
            'color': "#007bff", 
            # Użyjemy isoformat() do poprawnego formatowania daty/czasu dla JS
            'start': booking.start_time.isoformat(), 
            'end': booking.end_time.isoformat(),
            'url': f'/bookings/{booking.pk}/detail/' 
        })
    return JsonResponse(events, safe=False)


class TableListAPIView(generics.ListAPIView):
    serializer_class = TableSerializer

    def get_queryset(self):
        # Pobierz ID restauracji z URL
        restaurant_pk = self.kwargs['restaurant_pk']
        # Zwróć tylko stoliki należące do tej restauracji
        return Table.objects.filter(restaurant_id=restaurant_pk)
    

class UserListAPIView(generics.ListAPIView):
    # Możesz dodać ograniczenia, jeśli nie chcesz zwracać wszystkich użytkowników
    queryset = User.objects.all()
    serializer_class = UserSerializer