# Create your views here.
from rest_framework import generics
from .serializers import ProfileListSerializer, ProfileDetailSerializer
from .models import Profile


# Create your views here.

class ProfileListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileListSerializer


class ProfileRetrieveAPIView(generics.ListAPIView):
    lookup_field = 'id'
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer


class ProfileCreateAPIView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer
