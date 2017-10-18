# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Note
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NoteForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required



# Create your views here.

def note_list(request):
    notes = Note.objects.all ()
    return render ( request, 'notes/note_list.html', {'notes': notes} )


def note_detail(request, pk):
    note = get_object_or_404 ( Note, pk=pk )
    return render ( request, 'notes/note_detail.html', {'notes': note} )


def note_new(request):
    if request.method == "POST":
        form = NoteForm ( request.POST )
        if form.is_valid ():
            notes = Note.objects.all ()
            note = form.save ( commit=False )
            note.author = request.user
            note.published_date = timezone.now ()
            note.save ()
            return render ( request, 'notes/note_list.html', {'notes': notes} )
    else:
        form = NoteForm ()
    return render ( request, 'notes/note_edit.html', {'form': form} )


def note_edit(request, pk):
    note = get_object_or_404 ( Note, pk=pk )
    if request.method == "POST":
        form = NoteForm ( request.POST, instance=note )
        if form.is_valid ():
            note = form.save ( commit=False )
            note.author = request.user
            note.published_date = timezone.now ()
            note.save ()
            return redirect ( 'note_detail', pk=note.pk )
    else:
        form = NoteForm ( instance=note )
    return render ( request, 'notes/note_edit.html', {'form': form} )


def note_delete(request, pk):
    note = get_object_or_404 ( Note, pk=pk )
    notes = Note.objects.all ()
    note.delete()
    return render(request, 'notes/note_list.html', {'notes': notes} )


def signup(request):
    if request.method == 'POST':
        notes = Note.objects.all ()
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render ( request, 'notes/note_list.html', {'notes': notes} )
    else:
        form = UserCreationForm()
    return render(request, 'notes/signup.html', {'form': form})

