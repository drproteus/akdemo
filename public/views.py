from django.shortcuts import render
from random import randint

# Create your views here.

def home(request):
    pic = randint(1, 6)
    return render(request, template_name="public/base.html", context={"pic": pic})
