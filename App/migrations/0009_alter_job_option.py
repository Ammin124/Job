# Generated by Django 4.1.2 on 2022-10-29 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_alter_job_descriptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='option',
            field=models.CharField(choices=[('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Internship', 'Internship')], default='Dhaka', max_length=12),
        ),
    ]
