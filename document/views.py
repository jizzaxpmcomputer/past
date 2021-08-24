from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class TalimgaOidView(TemplateView):
    template_name = 'talimga_oid.html'
