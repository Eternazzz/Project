from django.contrib import admin
from .models import *


@admin.register(Positions)
class PositionsAdmin(admin.ModelAdmin):
    pass


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    pass

@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    pass


@admin.register(Tours)
class ToursAdmin(admin.ModelAdmin):
    pass


@admin.register(TypeofTour)
class TypeofTourAdmin(admin.ModelAdmin):
    pass


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    pass


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    pass


@admin.register(Hotels)
class HotelsAdmin(admin.ModelAdmin):
    pass
