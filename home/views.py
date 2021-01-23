from django.shortcuts import render

from .models import Job

def homepage(request):
    home = Job.objects
    return render(request, 'home/homepage.html', {'home':home})
    
