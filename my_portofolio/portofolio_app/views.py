from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'tentang.html')

def jadwal_view(request):
    return render(request, 'jadwal.html')

def galery_view(request):
    return render(request, 'galery.html')

def project_view(request):
    return render(request, 'project.html')

def feedback_view(request):
    return render(request, 'feedback.html')