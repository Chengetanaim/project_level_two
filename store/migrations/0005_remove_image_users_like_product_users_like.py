# Generated by Django 4.1.1 on 2023-02-09 17:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0004_image_image_store_image_created_e6fffe_idx'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='users_like',
        ),
        migrations.AddField(
            model_name='product',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='images_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
