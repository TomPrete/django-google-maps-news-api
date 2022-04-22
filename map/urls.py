from django.urls import path
from . import views

urlpatterns = [
    path('landmarks/', views.landmark_list, name='landmark_list'),
    path('landmarks/<int:landmark_id>', views.landmark_detail, name='landmark_detail'),
    path('top-headlines/', views.top_headlines, name='top_headlines'),
]
