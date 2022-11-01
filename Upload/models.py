from django.db import models

# Create your models here.

class Uploads(models.Model):
    image = models.ImageField(upload_to="images", blank=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class UploadFile(models.Model):
    file = models.FileField(upload_to="file", blank=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.description