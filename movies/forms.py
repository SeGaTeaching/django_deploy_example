from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'director', 'release_year', 'genre', 'imdb_url']
        

class CSVUploadForm(forms.Form):
    file = forms.FileField(label='Upload CSV-File')