from django.db import models
from django.utils.text import slugify

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Added default
    description = models.TextField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Blog Model
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    author = models.CharField(max_length=100, default="Admin")
    published_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# Uploaded File Model
class UploadedFile(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.image.name.split('.')[0])  
        super().save(*args, **kwargs)

    def __str__(self):
        return f"File uploaded on {self.uploaded_at}"

# Inquiry Model
class Inquiry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inquiries')
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.name} for {self.product.name}"
