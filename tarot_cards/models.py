from django.db import models

# Create your models here.
class TarotCard(models.Model):
    title = models.CharField(max_length=30)
    tag = models.CharField(max_length=30)
    src = models.URLField()
    group = models.CharField(max_length=15)
    text = models.TextField()
