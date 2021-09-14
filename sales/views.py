from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.views.generic import View


@login_required(login_url='/login/')
def homepage_view(request):
    context = {}
    return render(request, 'homepage.html', context)


class ApiView(View):
    '''connects to api to retrive food items'''
    
    def get(self, request):
        pass


    def post(self, request):
        pass
