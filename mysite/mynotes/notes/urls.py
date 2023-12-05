from django.urls import path, include
from . import views

urlpatterns = [
   path('',views.note_list, name='note_list'), 
   path('note/<int:pk>/', views.note_detail, name='note_detail'), 
   path('note/new/', views.note_new, name="note_new")
]