# Generated by Django 3.2 on 2024-01-14 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snsapp', '0002_remove_coment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='coment',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]