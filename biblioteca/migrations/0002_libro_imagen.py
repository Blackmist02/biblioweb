# Generated by Django 5.0.6 on 2024-06-03 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='libros'),
        ),
    ]
