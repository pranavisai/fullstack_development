import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django

django.setup()

import random 
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=10):
    for entry in range (N):

        fake_first = fakegen.first_name()
        fake_last = fakegen.last_name()
        fake_email = fakegen.email()

        user_data = User.objects.get_or_create(First_name = fake_first, Last_name = fake_last, Email = fake_email)[0]    

if __name__=='__main__':
    print("Starting the population")
    populate(15)
    print("populating complete!")