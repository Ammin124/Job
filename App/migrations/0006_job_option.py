# Generated by Django 4.1.2 on 2022-10-28 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_skills_job_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='option',
            field=models.CharField(choices=[('W', 'Weekly'), ('M', 'Monthly'), ('I', 'Internship')], default=False, max_length=2),
        ),
    ]
