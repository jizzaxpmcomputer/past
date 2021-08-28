from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from . models import Document
# Create your views here.
# class TalimgaOidView(ListView):
#     model = Document
#     template_name = 'talimga_oid.html'

def talimgaOid(request):
    context = {}
    context["doc"] = Document.objects.all()

    # if Document.document_types == 'talimga_oid':

    return render(request, "talimga_oid.html", context)




class VazirlarMahkamasiView(TemplateView):
    template_name = 'vazirlar_mahkamasi.html'


class PrezidentFarmoniView(TemplateView):
    template_name = 'prezident_farmoni.html'


class BoshqarmaBoshligiView(TemplateView):
    template_name = 'boshqarma.html'


class XalqTalimiVaziriView(TemplateView):
    template_name = 'xalq_talimi.html'