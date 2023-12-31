# Generated by Django 4.2.4 on 2023-09-11 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=700, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='order',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در'),
        ),
        migrations.AlterField(
            model_name='order',
            name='datetime_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='ویرایش شده در'),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=120, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='پرداخت شده؟'),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=120, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_notes',
            field=models.CharField(max_length=700, verbose_name='یادداشت سفارش'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='تلفن همراه'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
