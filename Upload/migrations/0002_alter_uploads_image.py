# Generated by Django 4.1.2 on 2022-10-26 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploads',
            name='image',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
    ]
