from django.shortcuts import render
from .forms import UploadForm
from .models import UploadedFile,Product
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

def product_list(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'products.html', {'products': products})  # Send products to template

