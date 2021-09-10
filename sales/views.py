from django.shortcuts import render
from django.contrib.auth.decorators import login_required



def index_view(request):
    context = {}
    return render(request, 'index.html', context)

@login_required(login_url='/login/')
def homepage_view(request):
    context = {}
    return render(request, 'homepage.html', context)
