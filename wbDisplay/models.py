from django.db import models
from django.urls import reverse

class namaDisplay(models.Model):
    titlevip = models.CharField(max_length=128)
    namavip = models.CharField(max_length=64)
    perusahaan = models.CharField(max_length=128)

    def get_absolute_url(self):
        return reverse('displayBoard', args=[str(self.id)])