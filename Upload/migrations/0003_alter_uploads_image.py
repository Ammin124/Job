# Generated by Django 4.1.2 on 2022-10-27 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Upload', '0002_alter_uploads_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploads',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]