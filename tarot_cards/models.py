from django.contrib import admin
from django.db import models
from django.utils.html import format_html

# Create your models here.
class TarotCard(models.Model):
    title = models.CharField(max_length=30)
    tag = models.CharField(max_length=30)
    src = models.URLField()
    group = models.CharField(max_length=15)
    text = models.TextField()


    def __str__(self):
        return f"{self.title}"




