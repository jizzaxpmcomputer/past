from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

class Namuna(TemplateView):
    template_name = 'boshqarma-raxbariyati.html'