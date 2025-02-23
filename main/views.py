from django.shortcuts import render,redirect
from .forms import UploadForm
from .models import UploadedFile,Product,Inquiry
from django.views.generic import DetailView
from .forms import InquiryForm
from django.core.mail import send_mail
from django.contrib import messages
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
    search_query = request.GET.get('search', '')  # Get the search query from the request
    if search_query:
        # Filter products based on the search query in product name
        products = Product.objects.filter(name__icontains=search_query)
    else:
        # If no search query, display all products
        products = Product.objects.all()
    
    return render(request, 'products.html', {'products': products, 'search_query': search_query})


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = InquiryForm()  # Pass the Inquiry form
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # Get the product object
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.product = self.object  # Associate inquiry with the product
            inquiry.save()

            # ✅ Send Email Notification
            admin_email = "sahildeshmukh335@gmail.com"  # Replace with the admin's email
            subject = f"New Inquiry for {inquiry.product.name}"
            message = (
                f"Name: {inquiry.name}\n"
                f"Company: {inquiry.company_name or 'N/A'}\n"
                f"Phone: {inquiry.phone or 'N/A'}\n"
                f"Email: {inquiry.email}\n"
                f"Message:\n{inquiry.message}"
            )
            send_mail(subject, message, 'sahildeshmukh335@gmail.com', [admin_email])

            # ✅ Show Success Message
            messages.success(request, "Your inquiry has been sent successfully!")

            return redirect('product_detail', pk=self.object.pk)  # Redirect after submission

        return self.get(request, *args, **kwargs, form=form)  # Re-render the page with errors