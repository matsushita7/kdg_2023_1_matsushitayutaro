# Generated by Django 3.2 on 2024-01-26 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snsapp', '0016_coment_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coment',
            name='likes',
        ),
        migrations.AddField(
            model_name='coment',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
