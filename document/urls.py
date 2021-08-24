from django.urls import path
from .views import TalimgaOidView

urlpatterns = [
    path('talimga_oid/', TalimgaOidView.as_view(), name='talim'),
]
