# Generated by Django 3.2 on 2024-02-02 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snsapp', '0024_alter_coment_user_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coment',
            name='user_record',
            field=models.TextField(blank=True, null=True),
        ),
    ]