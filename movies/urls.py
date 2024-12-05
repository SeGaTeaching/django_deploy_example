from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('watchlist/', views.watchlist_view, name='watchlist'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('upload_csv/', views.upload_csv, name='upload_csv'),
    path('delete/<int:movie_id>/', views.delete_movie, name='delete_movie'),
    path('edit_movie/<int:movie_id>/', views.edit_movie, name='edit_movie'),
]
