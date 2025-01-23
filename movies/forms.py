from django import forms
from .models import Movies

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['title', 'description', 'category', 'duration', 'img', 'rating', 'year', 'video']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'rating': forms.NumberInput(attrs={'step': 0.01, 'min': 0, 'max': 10}),
            'duration': forms.TextInput(attrs={'placeholder': 'Duración en minutos'}),
            'year': forms.TextInput(attrs={'placeholder': 'Año (e.g., 2023)'}),
            'img': forms.URLInput(attrs={'placeholder': 'http://example.com/imagen.jpg'}),
            'video': forms.URLInput(attrs={'placeholder': 'http://example.com/video.mp4'}),
        }
