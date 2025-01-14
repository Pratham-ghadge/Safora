from django.shortcuts import render
from decouple import config

# Create your views here.
def index(request):
    context = {
        'google_maps_api_key': config('GOOGLE_MAPS_API_KEY')  # Corrected the syntax
    }
    return render(request, 'index.html', context)
