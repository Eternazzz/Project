from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from events.views import *
from users.views import *


router = routers.DefaultRouter()

router.register(r'client', ClientViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'sale', SaleViewSet)
router.register(r'position', PositionViewSet)
router.register(r'type-of-tour', TypeofTourViewSet)
router.register(r'event', EventViewSet)
router.register(r'hotel', HotelViewSet)
router.register(r'tour', TourViewSet)
router.register(r'users', UsersViewSet)


events_urls = [
    path('api/', include(router.urls))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(events_urls)),
    path('auth/', include('djoser.urls')),
    path('sign-up/', UserSignUpView.as_view()),
    path('sign-in/', UserSignInView.as_view())
]
