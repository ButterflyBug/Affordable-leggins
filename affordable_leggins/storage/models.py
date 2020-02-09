from django.db import models


class Size(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Leggin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    price = models.FloatField()
    rrp = models.FloatField()
    external_id = models.IntegerField()
    sizes = models.ManyToManyField(Size)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
