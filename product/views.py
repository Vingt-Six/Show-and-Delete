from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.
def createproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'correctioncreate/back/product/create.html', {'form': form})
