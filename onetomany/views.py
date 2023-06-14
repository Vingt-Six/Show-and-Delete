from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def homegens(request):
    genres = Genre.objects.all()
    gens = Gens.objects.all()
    return render(request, 'correctioncreate/back/onetomany/gens.html', {'genres': genres, 'gens': gens})

def creategens(request):
    if request.method == 'POST':
        form = GensForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homegens')
    else:
        form = GensForm()
    return render(request, 'correctioncreate/back/onetomany/creategens.html', {'form': form})

def creategenre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homegens')
    else:
        form = GenreForm()
    return render(request, 'correctioncreate/back/onetomany/creategenre.html', {'form': form})