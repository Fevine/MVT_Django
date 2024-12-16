from django.db import models

# Create your models here.


class Car(models.Model):
    title = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.title
