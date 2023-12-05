from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm

# Create your views here.
def note_list(req):
    notes = Note.objects.all()
    return render(req, 'notes/note_list.html', {'notes': notes})

def note_detail(req, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(req, 'notes/note_detail.html', {'note' : note})

def note_new(req):
    if req.method == "POST":
        form = NoteForm(req.post)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_detail', pk=note.pk)
        else:
            form = NoteForm()
        return render(req, 'notes/note_edit.html', {'form' : form})