# Generated by Django 3.2 on 2024-02-02 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snsapp', '0025_alter_coment_user_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='comment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='snsapp.coment'),
            preserve_default=False,
        ),
    ]