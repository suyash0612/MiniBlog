from django.db import models

# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()

# class SignupChoiceModel(models.Model):
#     userperm = models.CharField(max_length=20,choices=(('admin','admin'),('author','author'),('subscriber','subscriber')))
