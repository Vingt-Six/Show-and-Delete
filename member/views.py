from django.shortcuts import render, redirect
from .forms import MemberForm
from .models import Member

# Create your views here.
def home(request):
    members = Member.objects.all()
    return render(request, 'correctioncreate/member/member.html', {'members': members})

def create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MemberForm()
    return render(request, 'correctioncreate/member/createmember.html', {'form': form})

def read(request, id):
    show = Member.objects.get(id=id)
    return render(request, 'correctioncreate/member/detail.html', {"show": show})

def destroy(request, id):
    destroy = Member(id)
    destroy.delete()
    return redirect('home')