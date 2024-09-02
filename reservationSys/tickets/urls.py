from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('guests', views.viewset_guest)
router.register('movies', views.viewset_movie)
router.register('reservations', views.viewset_reservation)


urlpatterns = [
    path('viewsets/', include(router.urls)),
    path('find-movie', views.find_movie),
    path('new-reservation', views.create_reservation)
]
