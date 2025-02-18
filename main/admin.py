from django.contrib import admin
from .models import Product, BlogPost,Inquiry

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price','created_at')
    search_fields = ('name', 'category')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Inquiry)  # ✅ Register Inquiry model