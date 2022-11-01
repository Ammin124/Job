# Generated by Django 4.1.2 on 2022-10-28 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Upload', '0003_alter_uploads_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='file')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
