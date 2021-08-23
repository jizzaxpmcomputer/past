from django.urls import path
from .views import HomePageView,Raxbariyat

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('pages/',Raxbariyat.as_view(), name='raxbariyat'),
]
