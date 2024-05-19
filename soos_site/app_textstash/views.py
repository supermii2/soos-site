from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Stash
from .forms import StashForm

def home_stash(request):
    return render(request, 'textstash_home.html')

def create_stash(request):
    if request.method == 'POST':
        form = StashForm(request.POST)
        if form.is_valid():

            exists = Stash.objects.filter(title=form.cleaned_data['title']).exists()
            if exists:
                messages.error(request, 'Title already used! Please delete first.')
                return redirect(create_stash)

            stash = Stash.objects.create(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
            )
            return redirect(view_stash, string_id=stash.string_id)

    form = StashForm()
    return render(request, 'textstash_create.html', {'form': form})

def read_stash(request):
    if request.method == 'POST':
        form = StashForm(request.POST)
        if form.is_valid():
            exists = Stash.objects.filter(title=form.cleaned_data['title']).exists()
            if not exists:
                messages.error(request, 'No stash found!')
                return redirect(read_stash)

            stash = Stash.objects.get(title=form.cleaned_data['title'])
            return redirect(view_stash, string_id=stash.string_id)

    form = StashForm()
    return render(request, 'textstash_read.html', {'form': form})

def update_stash(request):
    if request.method == 'POST':
        form = StashForm(request.POST)
        if form.is_valid():
            stash = Stash.objects.get(title=form.cleaned_data['title'])
            stash.content = form.cleaned_data['content']
            return redirect(view_stash, string_id=stash.string_id)

    form = StashForm()
    return render(request, 'textstash_update.html', {'form': form})

def delete_stash(request):
    if request.method == 'POST':
        form = StashForm(request.POST)
        if form.is_valid():
            exists = Stash.objects.filter(title=form.cleaned_data['title']).exists()
            if not exists:
                messages.error(request, 'No stash found!')
                return redirect(delete_stash)

            Stash.objects.get(title=form.cleaned_data['title']).delete()
            return redirect(home_stash)

    form = StashForm()
    return render(request, 'textstash_delete.html', {'form': form})

def view_stash(request, string_id):
    stash_to_render = Stash.objects.get(string_id=string_id)
    return render(request, 'textstash_view.html', { 'title': stash_to_render.title, 'content': stash_to_render.content })

