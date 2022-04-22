from django.db import models

# Create your models here.

class Landmark(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id}: {self.name} is located at {self.address}"
