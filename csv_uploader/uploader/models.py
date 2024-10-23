from django.db import models

# Create your models here.

class Records(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} - {self.class_name}'