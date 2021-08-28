from django.urls import path
from .views import VazirlarMahkamasiView, \
    PrezidentFarmoniView, \
    BoshqarmaBoshligiView, \
    XalqTalimiVaziriView

from . import views

app_name = 'document'

urlpatterns = [
    path('Ta`limga oid xujjatlar/', views.talimgaOid, name='talim'),
    path('Vazrilar mahkamasiga oid xujjatlar/', VazirlarMahkamasiView.as_view(), name='vazirlar_mahkamasi'),
    path('Prezident farmoni va qarorlari/', PrezidentFarmoniView.as_view(), name='prezident_farmoni'),
    path('Boshqarma boshlig`i buyruqlari/', BoshqarmaBoshligiView.as_view(), name='boshqarma'),
    path('Xalq ta`limi vaziri buyruqlari/', XalqTalimiVaziriView.as_view(), name='xalq_talimi'),

]
