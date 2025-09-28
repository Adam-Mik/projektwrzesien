from rest_framework import serializers
from .models import Booking
from restaurants.models import Restaurant, Table
from django.contrib.auth.models import User

class BookingSerializer(serializers.ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())
    table = serializers.PrimaryKeyRelatedField(queryset=Table.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Booking
        fields = ['id', 'user', 'restaurant', 'table', 'start_time', 'end_time', 'number_of_guests']