from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app_general/index.html')

def Movies (request):
    return render(request, 'app_general/Movie.html')

def Movie (request):
    return HttpResponse('Movie_id')              