from django.urls import path
from .views import HomePageView,Namuna

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('pages/',Namuna.as_view(), name='namuna'),
]
