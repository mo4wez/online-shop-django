from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    title = models.CharField(max_length=32, verbose_name=_('Title'))
    description = RichTextField(verbose_name=_('Description'))
    short_description = models.TextField(blank=True, verbose_name=_('Short Description'))
    price = models.PositiveIntegerField(default=0, verbose_name=_('Price'))
    active = models.BooleanField(default=True, verbose_name=_('Active'))
    image = models.ImageField(upload_to='product/product_cover/', blank=True, verbose_name=_('image'))

    datetime_created = models.DateTimeField(default=timezone.now)
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
        ('1', _('Very Bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Perfect')),
    ]

    product = models.ForeignKey(to=Product, related_name="comments", verbose_name=_('Product'), on_delete=models.CASCADE)
    user = models.ForeignKey(to=get_user_model(), related_name="comments", verbose_name=_("User"), on_delete=models.CASCADE)
    text = models.TextField(verbose_name=_("Leave cocmment here"))
    stars = models.CharField(max_length=10, verbose_name=_("Your score to this product"), choices=PRODUCT_STAR)
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
    
    