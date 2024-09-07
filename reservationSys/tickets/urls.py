from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register('guests', views.viewset_guest)
router.register('movies', views.viewset_movie)
router.register('reservations', views.viewset_reservation)


urlpatterns = [
    path('viewsets/', include(router.urls)),
    path('find-movie', views.find_movie),
    path('new-reservation', views.create_reservation),
    # Token URL
    path('token-auth', obtain_auth_token),
    # Post URL
    path('post/<int:pk>', views.Post_pk.as_view()),
    # path('post/', views.Post_pk),
]
