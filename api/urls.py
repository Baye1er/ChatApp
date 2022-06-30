from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.ProfileListAPIView.as_view(), name='profiles'),
    path('profiles/<int:id>/', views.ProfileRetrieveAPIView.as_view(), name='profiles'),
    path('create_profile/', views.ProfileCreateAPIView.as_view(), name='create_profile'),
]