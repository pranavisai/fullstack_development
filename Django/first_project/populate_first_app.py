import os

##configuring settings for the project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django

# this will setup and configure the django settings
django.setup()

## Fake script
import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

#creating an instance for this faker object
fakegen = Faker()

topics = ['Search', 'Social', 'MarkertPlace', 'News', 'Games']

#function to add topic
def add_topic():
    
    #get_or_create will either create or retrieve the existing in the model. This returns a tuple.
    #random.choice is a method to choose randomly
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

#default N is given here to populate
def populate(N=5):

    for entry in range(N):

        #get the topic for the entry
        top = add_topic()

        #create the fake data for the entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create new webpage entry
        webpg = Webpage.objects.get_or_create(topic = top, url = fake_url, name = fake_name)[0]

        #create fake accessrecord for webpage
        acc_rec = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]

if __name__== '__main__':
    print("populating script")
    populate(20)
    print("populating complete!")
