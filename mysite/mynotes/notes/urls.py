from django.urls import path, include
from . import views

urlpatterns = [
   path('',views.note_list, name='note_list')
]