from django.db import models
from django.utils.text import slugify

# Product Model
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('MIG', 'MIG Welding Wire'),
        ('TIG', 'TIG Welding Rod'),
        ('ARC', 'Arc Welding Electrode'),
    ]
    
    name = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
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

from django.db import models
from django.utils.text import slugify

class UploadedFile(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True)  # ✅ Add this

    def save(self, *args, **kwargs):
        if not self.slug:  # ✅ Generate slug if not set
            self.slug = slugify(self.image.name.split('.')[0])  
        super().save(*args, **kwargs)

    def __str__(self):
        return f"File uploaded on {self.uploaded_at}"



    
    
    def __str__(self):
        return self.title
