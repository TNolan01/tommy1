from django.shortcuts import render

# Renders home page
def index(request):
    
    return render(request, 'home/index.html')
