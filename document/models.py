from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Document(models.Model):
    name = models.TextField()
    talimga_oid = 'talimga_oid'
    vazirlar_mahkamasi = 'vazirlar_mahkamasi'
    prezident_farmoni = 'prezident_farmoni'
    boshqarma_boshligi = 'boshqarma_boshligi'
    xalq_talim_vaziri = 'xalq_talim_vaziri'
    document_types = [
        (talimga_oid, 'Ta`limga oid buyruqlar'),
        (vazirlar_mahkamasi, 'Vazirlar mahkamasi qarorlari'),
        (prezident_farmoni, 'Prezident farmoni va qarorlari'),
        (boshqarma_boshligi, 'Boshqarma boshligi buyruqlari'),
        (xalq_talim_vaziri, 'Xalq ta`lim vaziri buyruqlari'),

    ]
    user_type = models.CharField(max_length=20, choices=document_types, default=talimga_oid)
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='images/', blank=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    url = models.URLField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']