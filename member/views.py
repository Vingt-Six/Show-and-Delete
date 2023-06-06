from django.shortcuts import render, redirect
from .forms import MemberForm
from .models import Member

# Create your views here.
def home(request):
    members = Member.objects.all()
    return render(request, 'correctioncreate/back/member/member.html', {'members': members})

def create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MemberForm()
    return render(request, 'correctioncreate/back/member/createmember.html', {'form': form})

def read(request, id):
    show = Member.objects.get(id=id)
    return render(request, 'correctioncreate/back/member/detail.html', {"show": show})

def update(request, id):
    edit = Member.objects.get(id=id)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MemberForm(instance=edit)
    return render(request, 'correctioncreate/back/member/edit.html', {'form': form})

def destroy(request, id):
    destroy = Member(id)
    destroy.delete()
    return redirect('home')