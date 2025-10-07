from django.shortcuts import render

from .models import Productos

# Create your views here.
def index(request):

    productos=Productos.objects.all()

    return render(request, 'index.html',{'productos':productos})