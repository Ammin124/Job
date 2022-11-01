from django.db import models

# Create your models here.
invoice_type_choice =[
    ('Weekly', 'Weekly'),
    ('Monthly', 'Monthly'),
    ('Internship', 'Internship'),
]

class Registeration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=77)
    option = models.CharField(max_length=22, choices=invoice_type_choice, default='Monthly')

    def __str__(self):
        return self.first_name