from rest_framework import serializers
from .models import *


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = '__all__'


class TypeofTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeofTour
        fields = '__all__'


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class HotelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = '__all__'


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'


class ToursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tours
        fields = '__all__'


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'
