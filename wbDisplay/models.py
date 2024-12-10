from django.db import models
from django.urls import reverse

class namaDisplay(models.Model):
    titlevip = models.CharField(max_length=128, null=True, blank=True)
    namavip = models.CharField(max_length=64, null=True, blank=True)
    perusahaan = models.CharField(max_length=128, null=True, blank=True)
    jam = models.TimeField()

    def get_absolute_url(self):
        return reverse('displayBoard', args=[str(self.id)])