import os

import faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE','second_project.settings')

import django
django.setup()

import random
from second_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()

topics = ['Search', 'Marketplace','News','Social media']

def add_topic():
    t = Topic.objects.get_or_create(name = random.choice(topics))[0]
    t.save()
    return t

def populate(n=5):

    for entry in range(n):

        # Get topic for entry
        topic_new = add_topic()

        # Generate fake data for entry using external Library Faker

        fake_name = fakegen.company()
        fake_url = fakegen.url()
        fake_date = fakegen.date()

        # created dummy data for Webpage model
        webpg = Webpage.objects.get_or_create(topic= topic_new, url = fake_url, name= fake_name)[0]
        webpg.save()

        # created dummmy data for AccessRecord model
        access_record = AccessRecord.objects.get_or_create(webpage= webpg, date = fake_date)[0]
        access_record.save()
        


if __name__ == '__main__':
    print("Populating data")
    populate(10)
    print("Population complete.....check your webpage!!")

