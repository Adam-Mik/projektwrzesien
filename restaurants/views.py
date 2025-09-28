from django.shortcuts import render
from rest_framework import generics
from .models import Restaurant, Table
from .serializers import RestaurantSerializer, TableSerializer

class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class TableList(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class TableDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


def home_view(request):
    return render(request, 'home.html')

def restaurant_list_view(request):
    return render(request, 'restaurants/restaurant_list.html')

def table_list_view(request):
    return render(request, 'restaurants/table_list.html')

