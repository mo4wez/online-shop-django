from django.contrib import admin

from .models import Product, Comment

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'price',
        'active',
        'datetime_modified',
        )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
        'text',
        'stars',
        'active',
        'datetime_modified',
    )
