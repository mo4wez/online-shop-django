from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Product, Comment


class CommentsInline(admin.StackedInline):
    model = Comment
    fields = ['user', 'text', 'stars', 'active',]
    extra = 1


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = [
        'title',
        'description',
        'price',
        'active',
        ]
    
    inlines = [
        CommentsInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'product',
        'text',
        'stars',
        'active',
        'datetime_modified',
    ]
