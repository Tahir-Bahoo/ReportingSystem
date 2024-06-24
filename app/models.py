from django.db import models

# Create your models here.


class ExcelFile(models.Model):
    file = models.FileField(upload_to="excel") 

    def __str__(self):
        return self.file.name
    