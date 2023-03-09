from django.shortcuts import render
from .models import *
# Create your views here.


def home_page_view(request):
    hotels=Hotel.objects.all()
    rooms = Room.objects.filter()
    context={
        'hotels':hotels

    }
    return render(request, 'users/login.html',context)


