from django.shortcuts import render
from .models import Note

# Create your views here.
def note_list(req):
    notes = Note.objects.all()
    return render(req, 'notes/note_list.html', {'notes': notes})