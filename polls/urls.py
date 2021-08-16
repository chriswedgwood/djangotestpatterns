
from django.urls import path

from . import views

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('', views.index, name='index'),
]