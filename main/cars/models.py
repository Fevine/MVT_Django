from django.db import models

# Create your models here.


class Car(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.title
