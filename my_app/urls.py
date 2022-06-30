from django.urls import path
from .views import ProfileListView, ProfileDetailView, ProfileUpdateView, ProfileDeleteView, signin, signup, space, spaces, extend_profile, relatives, GenealogicalTreeCreateView
#GenealogicalTreeListView

urlpatterns = [
    path('', signin, name='signin'),
    path('profile_page/', relatives, name='profile_page'),
    path('create_relatives/', GenealogicalTreeCreateView.as_view(), name='create_relatives'),
    path('admin_page/', ProfileListView.as_view(), name='admin_page'),
    path('admin_page/<int:pk>/', ProfileDetailView.as_view(), name='details'),
    path('admin_page/<int:pk>/update/', ProfileUpdateView.as_view(), name='update'),
    path('admin_page/<int:pk>/delete/', ProfileDeleteView.as_view(), name='delete'),
    path('admin_page/create/', signup, name='create'),
    path('admin_page/extend/', extend_profile, name='extend'),
    path('spaces/', spaces, name='spaces'),
    path('spaces/<slug:slug>/', space, name='space'),

]