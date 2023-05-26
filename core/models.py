from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True)
    street = models.CharField(max_length=50)
    post_code = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)