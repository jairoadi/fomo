
import os
#initialize django environement
os.environ['DJANGO_SETTINGS_MODULE'] = 'fomo.settings'
import django
django.setup()

from account.models import FomoUser

#user 1
user1 = FomoUser();
user1.address = "Provo, UT 84602"
user1.city = "Provo"
user1.gender = "Female"
user1.phone = "801-422-4636"
user1.state = "UTAH"
user1.stateinitial = "UT"
user1.zipcode = "84602"
user1.save()


#user 2
user2 = FomoUser();
user2.address = "Provo, UT 84602"
user2.city = "Provo"
user2.gender = "Female"
user2.phone = "801-422-4636"
user2.state = "UTAH"
user2.stateinitial = "UT"
user2.zipcode = "84602"
user2.save()

#user 3
user3 = FomoUser();
user3.address = "Provo, UT 84602"
user3.city = "Provo"
user3.gender = "Female"
user3.phone = "801-422-4636"
user3.state = "UTAH"
user3.stateinitial = "UT"
user3.zipcode = "84602"
user3 .save()


