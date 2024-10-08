from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly
from rest_framework import generics

# Create your views here.
# Using viewsets


class viewset_guest(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    authentication_calsses = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class viewset_movie(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_calsses = [TokenAuthentication]


class viewset_reservation(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    authentication_calsses = [TokenAuthentication]


@api_view(['GET'])
def find_movie(request):
    movies = Movie.objects.filter(
        # hall = request.data['hall'],
        movie = request.data['movie']
    )
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_reservation(request):
    movie = Movie.objects.get(
        # hall = request.data['hall'],
        movie = request.data['movie']
    )

    guest = Guest()
    guest.name = request.data['name']
    guest.phone = request.data['phone']
    guest.save()

    reservation = Reservation()
    reservation.guest = guest
    reservation.movie = movie
    reservation.save()

    return Response("Reservation Created Successfully ", status=status.HTTP_201_CREATED)



class Post_pk(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer