from django.db import models
import uuid


# Create your models here.
class Keyboard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    switch = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Mouse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    dpi = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    weight = models.IntegerField()
    brand = models.CharField(max_length=100)
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.name
