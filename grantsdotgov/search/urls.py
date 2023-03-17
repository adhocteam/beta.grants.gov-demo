from django.urls import path
from . import views

urlpatterns = [
        path('search/', views.search, name='search'),
        path('details/<int:gid>/', views.details, name='details'),
]
