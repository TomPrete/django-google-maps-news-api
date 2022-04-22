from django.shortcuts import render
from .models import Landmark
import requests as req

# Create your views here.

NEWS_API_KEY='your api here'
GOOGLE_MAPS_API='your api here'

def landmark_list(request):
    all_landmarks = Landmark.objects.all()
    data = {
        'all_landmarks': all_landmarks
    }
    return render(request, 'map/landmark_list.html', data)

def landmark_detail(request, landmark_id):
    landmark = Landmark.objects.get(id=landmark_id)
    google_address = _generate_google_address(landmark.address)
    data = {
        'landmark': landmark,
        'google_address': google_address
    }
    return render(request, 'map/landmark_detail.html', data)

def _generate_google_address(address):
    modified_address = address.replace(' ', '%20')
    return f"https://www.google.com/maps/embed/v1/place?key={ GOOGLE_MAPS_API }&zoom=15&maptype=satellite&q={ modified_address }"

def top_headlines(request):
    resp = req.get(f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={ NEWS_API_KEY }")
    if resp.status_code == 200:
        data = resp.json()
        article_data = {
            'total_articles': data['totalResults'],
            'all_articles': data['articles']
        }
        return render(request, 'news/article_list.html', article_data)
    else:
        return render(request, 'news/404.html', {})
