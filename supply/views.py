from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image

# Create your views here.
def index(request):
    images = Image.objects.all()
    return render (request, 'all-supply/index.html',{"images":images},)

 