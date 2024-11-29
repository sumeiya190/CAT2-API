from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.index, name='index'),  # Map the root of 'question1/' to the index view
]
