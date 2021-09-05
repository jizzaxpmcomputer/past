from django.urls import path
from .views import \
    PrezidentFarmoniView, \
    BoshqarmaBoshligiView, \
    XalqTalimiVaziriView, DocumentDetailView,TalimgaOidView,DocumentNewView

from . import views



urlpatterns = [
    path('new/',DocumentNewView.as_view(), name='document_new'),
    path('Ta`limga oid xujjatlar/',TalimgaOidView.as_view(), name='talim'),
    path('Vazrilar mahkamasiga oid xujjatlar/', views.vazirlarMahkamasi, name='vazirlar_mahkamasi'),
    path('Prezident farmoni va qarorlari/', PrezidentFarmoniView.as_view(), name='prezident_farmoni'),
    path('Boshqarma boshlig`i buyruqlari/', BoshqarmaBoshligiView.as_view(), name='boshqarma'),
    path('Xalq ta`limi vaziri buyruqlari/', XalqTalimiVaziriView.as_view(), name='xalq_talimi'),
    path('<int:pk>/', DocumentDetailView.as_view(), name='detail_view'),

]
