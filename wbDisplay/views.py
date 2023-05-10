from django.views.generic import TemplateView, UpdateView, DetailView
from .models import namaDisplay

class displayBoard(DetailView):
    template_name = 'index.html'
    model = namaDisplay

class gantiNama(UpdateView):
    model = namaDisplay
    template_name =  'update.html'
    fields = '__all__'