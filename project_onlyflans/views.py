from django.shortcuts import render
from django.http import HttpResponse

# definir funciones render

def index(request):
    return render(request, 'index.html')

# logout

