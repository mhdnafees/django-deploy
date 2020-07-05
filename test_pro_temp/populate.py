import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','test_pro_temp.settings')

import django
django.setup()

from test_app_temp.models import Person
from faker import Faker

fakegen = Faker()

def populate(N=1):

    for entry in range(N):
        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.ascii_free_email()

        userls = Person.objects.create(f_name=fake_fname,l_name=fake_lname,email_id=fake_email)

if __name__ == '__main__':
    print("Populating DB")
    populate(15)
    print("DONE!!")
