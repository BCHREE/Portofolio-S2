from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html') # <--- Ada jarak 1 tab di depan 'return'

def biodata_view(request):
    return render(request, 'tentang.html') # <--- Harus sejajar dengan return di atas

def jadwal_view(request):
    return render(request, 'jadwal.html')

def galery_view(request):
    return render(request, 'galery.html')

def feedback_view(request):
    return render(request, 'feedback.html')

def project_view(request):
    # Ini untuk halaman apa saja yang dipelajari di pondok
    return render(request, 'project.html')