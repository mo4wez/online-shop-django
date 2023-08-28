from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse
from django.contrib.auth import get_user_model

class Product(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})


class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    PRODUCT_STAR = [
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Normal'),
        ('4', 'Good'),
        ('5', 'Perfect'),
    ]

    product = models.ForeignKey(to=Product, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(to=get_user_model(), related_name="comments", on_delete=models.CASCADE)
    text = models.TextField()
    stars = models.CharField(max_length=10, choices=PRODUCT_STAR)
    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    # manager
    objects = models.Manager()
    active_comments_manager = ActiveCommentsManager()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.product.id})
    
    