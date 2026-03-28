from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Services
from .forms import ServicesForms

class ServicesList(View):
    def get(self, request):
        service = Services.objects.all()
        return render(request, 'crud/service_list.html', {'service': service})

class CreateService(View):
    def get(self, request):
        form = ServicesForms()
        return render(request, 'crud/service_add.html', {'form': form})

    def post(self, request): 
        form = ServicesForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('servis_list')
        return render(request, 'crud/service_add.html', {'form': form})

class UpdateServis(View):
    def get(self, request, pk):
        servis = get_object_or_404(Services, pk=pk)
        form = ServicesForms(instance=servis)
        return render(request, 'crud/servis_update.html', {'form': form, 'servis': servis})

    def post(self, request, pk):
        servis = get_object_or_404(Services, pk=pk)
        form = ServicesForms(request.POST, request.FILES, instance=servis)
        if form.is_valid():
            form.save()
            return redirect('servis_list')
        return render(request, 'crud/servis_update.html', {'form': form, 'servis': servis})
    
    
class DeleteServis(View):
    def get(self, request, pk):
        servis = get_object_or_404(Services, pk=pk)
        return render(request, 'crud/servis_delete.html', {'servis': servis})

    def post(self, request, pk):
        servis = get_object_or_404(Services, pk=pk)
        servis.delete()
        return redirect('servis_list')