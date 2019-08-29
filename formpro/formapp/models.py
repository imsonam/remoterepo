from django.db import models

class FormData(models.Model):
    name=models.CharField(max_length=100)
    sal=models.IntegerField()
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=200)
    location=models.CharField(max_length=100)