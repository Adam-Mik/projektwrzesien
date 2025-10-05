from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from .models import Restaurant, Table
from .serializers import RestaurantSerializer, TableSerializer

class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantDetailAPIView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    lookup_field = 'pk'

class TableList(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class TableDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

def restaurant_list_view(request):
    return render(request, 'restaurants/restaurant_list.html')

def table_list_view(request):
    return render(request, 'restaurants/table_list.html')


#------------------------------ Additional Context -----------------------------#
def restaurant_detail_view(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    context = {'restaurant': restaurant}
    return render(request, 'restaurants/detail_restaurant.html', context)

def restaurants_table(request):
    queryset = Restaurant.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(name__icontains=request.GET.get('search'))

    context = {'restaurants': queryset}
    return render(request, 'restaurants_table.html', context)

def restaurants(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        address = data.get('address')
        phone_number = data.get('phone_number')
        description = data.get('description')

        Restaurant.objects.create(
            name=name,
            address=address,
            phone_number=phone_number,
            description=description,
        )
        return redirect('/')

    queryset = Restaurant.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(name__icontains=request.GET.get('search'))

    context = {'restaurants': queryset}
    return render(request, 'restaurants.html', context)


def delete_restaurant(request, id):
    restaurants = get_object_or_404(Restaurant, id=id)
    restaurants.delete()
    return redirect('/')


def update_restaurant(request, id):
    restaurants = get_object_or_404(Restaurant, id=id)
    if request.method == 'POST':
        data = request.POST
        restaurants.name = data.get('name')
        restaurants.address = data.get('address')
        restaurants.phone_number = data.get('phone_number')
        restaurants.description = data.get('description')
        restaurants.save()
        return redirect('/')

    context = {'restaurants': restaurants}
    return render(request, 'update_restaurant.html', context)
