from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView.as_view(), name='displayBoard'),
    path('<int:pk>', views.displayBoard.as_view(), name='displayBoard'),
    path('update/<int:pk>', views.gantiNama.as_view(), name='update'),
]