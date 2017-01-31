from django.db import models
from django.contrib.auth.models import AbstractUser


Gender_Option = [
    ['male', 'Male'],
    ['female', 'Female'],
    ['transgender', 'Transgender'],
    ['undefined', 'Undefined'],
]


class FomoUser(AbstractUser):
    #already inherited email, first and last name
    gender = models.TextField(null = True, blank = True, choices = Gender_Option)
    address = models.TextField(null = True, blank = True)
    city = models.TextField(null = True, blank = True)
    state = models.TextField(null = True, blank = True)
    stateinitial = models.TextField(null = True, blank = True)
    zipcode = models.TextField(null = True, blank = True)
    phone = models.TextField(null = True, blank = True)
