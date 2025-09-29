from django.shortcuts import render, redirect, get_object_or_404
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


#------------------------------ Additional Context -----------------------------#

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


# def delete_recipe(request, id):
#     recipe = get_object_or_404(Recipe, id=id)
#     recipe.delete()
#     return redirect('/')


# def update_recipe(request, id):
#     recipe = get_object_or_404(Recipe, id=id)
#     if request.method == 'POST':
#         data = request.POST
#         recipe_name = data.get('recipe_name')
#         recipe_description = data.get('recipe_description')
#         recipe_image = request.FILES.get('recipe_image')

#         recipe.recipe_name = recipe_name
#         recipe.recipe_description = recipe_description
#         if recipe_image:
#             recipe.recipe_image = recipe_image
#         recipe.save()
#         return redirect('/')

#     context = {'recipe': recipe}
#     return render(request, 'update_recipe.html', context)
