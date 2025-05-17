from django.shortcuts import render, get_object_or_404
from .models import MenuItem

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dynamic_menu_view(request, url):
    menu_item = get_object_or_404(MenuItem, url=url)

    template_name = 'dynamic_template.html'
    
    return render(request, template_name, {'menu_item': menu_item})