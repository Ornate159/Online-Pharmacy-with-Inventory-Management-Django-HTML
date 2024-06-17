# Generated by Django 5.0.6 on 2024-06-14 23:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_userprofile_address_userprofile_contact_number_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available_pharmacies',
            field=models.ManyToManyField(blank=True, related_name='available_products', to=settings.AUTH_USER_MODEL),
        ),
    ]