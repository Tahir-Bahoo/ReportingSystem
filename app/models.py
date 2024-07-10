from django.db import models

# Create your models here.


class ExcelFile(models.Model):
    file = models.FileField(upload_to="excel") 

    def __str__(self):
        return self.file.name
    

class Iframe(models.Model):
    title = models.CharField(max_length=300)
    iframe_link = models.TextField()

    def __str__(self):
        return self.title
        