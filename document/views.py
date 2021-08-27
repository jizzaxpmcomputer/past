from django.shortcuts import render
from django.views.generic import TemplateView
from . models import Document
# Create your views here.
class TalimgaOidView(TemplateView):
    model = Document
    context_object_name = 'document'
    template_name = 'talimga_oid.html'



class VazirlarMahkamasiView(TemplateView):
    template_name = 'vazirlar_mahkamasi.html'


class PrezidentFarmoniView(TemplateView):
    template_name = 'prezident_farmoni.html'


class BoshqarmaBoshligiView(TemplateView):
    template_name = 'boshqarma.html'


class XalqTalimiVaziriView(TemplateView):
    template_name = 'xalq_talimi.html'