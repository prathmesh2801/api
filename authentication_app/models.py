from django.db import models

# Create your models here.

from django.db import models

class Register(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    birthplace = models.CharField(max_length=100,null=True, blank=True)
    education = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.email
