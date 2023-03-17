from django.urls import path
from . import views

urlpatterns = [
        path('search/', views.search, name='search'),
        path('details/<int:id>/', views.details, name='details'),
]
