from django.views.generic import TemplateView, UpdateView, DetailView, RedirectView
from .models import namaDisplay
from django.conf import settings
from pathlib import os

class indexView(RedirectView):
    url = '/1'#os.path.join(settings.BASE_DIR, '1')

class displayBoard(DetailView):
    template_name = 'index.html'
    model = namaDisplay

class gantiNama(UpdateView):
    model = namaDisplay
    template_name =  'update.html'
    fields = '__all__'