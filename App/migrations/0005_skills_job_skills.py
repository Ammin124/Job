# Generated by Django 4.1.2 on 2022-10-22 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_author_job_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='skills',
            field=models.ManyToManyField(to='App.skills'),
        ),
    ]
