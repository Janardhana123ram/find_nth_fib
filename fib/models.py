from django.db import models

class Fibonacci(models.Model):
    n = models.IntegerField(default=0)
    nth = models.IntegerField(default=0)
    status = models.CharField(max_length=100, default="pending")
