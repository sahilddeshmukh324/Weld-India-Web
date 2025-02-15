from django.shortcuts import render
from .forms import UploadForm
from .models import UploadedFile
# Create your views here.

def home(request):
    return render(request, 'home.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadForm()
    
    images = UploadedFile.objects.all()  # Fetch all uploaded files
    return render(request, 'upload.html', {'form': form, 'images': images})