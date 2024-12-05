from . import views
from django.urls import path

app_name = 'newyear'
urlpatterns = [
    path('', views.newyear, name='newyear'),
]
