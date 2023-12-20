from django.shortcuts import render
from django.views.generic import ListView,DetailView , CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import PackageDetails
from django.urls import reverse_lazy
from Packages.forms import PackageForm
from .models import Package


def home(request):
    return render(request, 'home.html', {})

def package_list(request):
    package_objects = Package.objects.all()
    return render(request, 'packages.html',{'package_objects' : package_objects})

class HomeView(ListView):
    model = Package

    template_name = 'home.html'

class PackageView(ListView):
    model = Package
    template_name = 'packages.html'

def package_details(request, package_id):
    package_item = Package.objects.get(id=package_id)
    return render(request, 'package_details.html', {'package': package_item})

class PackagesDetail(CreateView):
 model = PackageDetails
 form_class = PackageForm
 template_name = 'add_package.html'

 def get_success_url(self):
    return reverse_lazy('packagenote')  
    
class NotePackageView(ListView):
 model = Package
 template_name = 'packagenote.html' 