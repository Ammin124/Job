from django.db import models
NEWSLETTER_OPTION =[
    ('Full Tile', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Internship', 'Internship'),
]

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    designation = models.CharField(max_length=110)
    def __str__(self):
        return self.name

class Skills(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Location(models.Model):
    permanentAddress = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=25)
    zip = models.CharField(max_length=9)
    def __str__(self):
        return self.country


class Job(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.TextField(null=True)
    expiry = models.DateField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    salary = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null= True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null= True)
    skills = models.ManyToManyField(Skills)
    option = models.CharField(max_length=12, choices=NEWSLETTER_OPTION, default="Full Time")

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-id']