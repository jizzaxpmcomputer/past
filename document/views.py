from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Document


# Create your views here.
# class TalimgaOidView(ListView):
#     model = Document
#     template_name = 'talimga_oid.html'
class TalimgaOidView(ListView):
    model = Document
    queryset = Document.objects.filter(user_type='talimga_oid')
    template_name = 'talimga_oid.html'


def vazirlarMahkamasi(request):
    context = {}
    context["doc"] = Document.objects.filter(user_type='vazirlar_mahkamasi')
    return render(request, "vazirlar_mahkamasi.html", context)


class DocumentDetailView(DetailView):
    model = Document
    template_name = 'detail.html'


class PrezidentFarmoniView(ListView):
    model = Document
    queryset = Document.objects.filter(user_type='prezident_farmoni')
    template_name = 'prezident_farmoni.html'


class BoshqarmaBoshligiView(TemplateView):
    template_name = 'boshqarma.html'


class XalqTalimiVaziriView(TemplateView):
    template_name = 'xalq_talimi.html'


class DocumentNewView(CreateView):
    model = Document
    template_name = 'document_new.html'
    fields = ['name', 'user_type', 'photo', 'author', 'url']
