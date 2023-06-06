from django.shortcuts import render
from member.models import Member
from product.models import Product

# Create your views here.
def homepage(request):
    members = Member.objects.all()
    products = Product.objects.all()
    return render(request, 'correctioncreate/front/home.html', {"members": members, 'products': products})