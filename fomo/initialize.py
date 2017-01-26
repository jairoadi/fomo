from datetime import datetime
from django.contrib.auth.models import AbstractUser
import os

#initialize django environement
os.environ['DJANGO_SETTINGS_MODULE'] = 'fomo.settings'
import django
django.setup()

from account.models import FomoUser
