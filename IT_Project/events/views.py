from events.serializers import *
from events.models import *
from rest_framework import viewsets


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Positions.objects.all()
    serializer_class = PositionSerializer


class TypeofTourViewSet(viewsets.ModelViewSet):
    queryset = TypeofTour.objects.all()
    serializer_class = TypeofTourSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotels.objects.all()
    serializer_class = HotelsSerializer


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tours.objects.all()
    serializer_class = ToursSerializer
