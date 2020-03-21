from django.db import models
from django.contrib import admin
from django.utils.safestring import mark_safe


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

    def __str__(self):
        return str(self.date) + " / " + self.name + " / " + str(self.price) + " PLN"

    def url(self):
        return mark_safe(f"<a target='_blank' href='https://www.myprotein.pl/{self.external_id}.html'>CHECK ME</a>")

    url.allow_tags = True
