from django.urls import include, path
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('guests', viewset_guest)
router.register('movies', viewset_movie)
router.register('reservations', viewset_reservation)


urlpatterns = [
    path('viewsets/', include(router.urls))
]
