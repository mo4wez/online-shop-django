# Generated by Django 4.2.4 on 2023-09-04 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_comment_stars'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product/product_image/', verbose_name='image'),
        ),
    ]
