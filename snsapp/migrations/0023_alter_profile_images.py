# Generated by Django 3.2 on 2024-01-31 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snsapp', '0022_alter_coment_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='images',
            field=models.ImageField(blank=True, default='sns/icon.png', null=True, upload_to=''),
        ),
    ]