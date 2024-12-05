import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Movie
from .forms import MovieForm, CSVUploadForm

# Create your views here.
@login_required(login_url='accounts:login')
def watchlist_view(request):
    movies = Movie.objects.filter(user=request.user)
    return render(request, 'movies/movies.html', {'movies': movies})

@login_required(login_url='accounts:login')
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:watchlist')
    else:
        form = MovieForm()
    return render(request, 'movies/add_movie.html', {'form': form})

# Edit Movie
def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            edit_movie = form.save(commit=False)
            edit_movie.user = request.user
            edit_movie.save()
            return redirect('movies:watchlist')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/edit_movies.html', {'form': form, 'movie': movie})

# Delete Movie
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:watchlist')
    return render(request, 'movies/delete_movie.html', {'movie': movie})

@login_required(login_url='accounts:login')
def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES.get('file')
            # Check if file is a csv file
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'Please upload only CSV files.')
                return render(request, 'movies/upload_csv.html', {'form': form})
            
            # Dekodieren und Zeilen einlesen
            try:
                decoded_file = csv_file.read().decode('utf-8').splitlines()
                reader = csv.DictReader(decoded_file)
                print(f'this is what I see: {reader}')

                for row in reader:
                    Movie.objects.create(
                        user=request.user,
                        title=row['title'],
                        director=row['director'],
                        release_year=row['release_year'],
                        genre=row['genre'],
                        imdb_url=row.get('imdb_url', '')
                    )
                return redirect('movies:watchlist')
            
            except Exception as e:
                messages.error(request, f'Error while handling file: {str(e)}')
    else:
        form = CSVUploadForm()
    return render(request, 'movies/upload_csv.html', {'form': form})