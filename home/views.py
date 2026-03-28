from django.shortcuts import render
from services.models import Services

def home_page(request):
    servies = Services.objects.all()
    return render(request, 'home_page/index.html', {'servies': servies})

