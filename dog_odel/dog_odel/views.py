from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
from somewhere import handle_uploaded_file

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def handler404(request):
    return render(request, 'errors/404.html', {}, status=404)

def handler500(request):
    return render(request, 'errors/500.html', {}, status=500)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})