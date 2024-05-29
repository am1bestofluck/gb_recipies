import pdb
from django.db.models import QuerySet
from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from django.db.models import QuerySet
from random import choice
from pathlib import Path
from cook_house.models import User


class Command(BaseCommand):
    help = "Forge random users"

    def add_arguments(self, parser):
        parser.add_argument("quantity", type=int)

    def handle(self, *args, **options):
        # pdb.set_trace()
        print(options['quantity'])
        for i in range(options['quantity']):
            username = lorem_ipsum.words(count=1, common=False)
            first_name = lorem_ipsum.words(count=1, common=False).title()
            last_name = lorem_ipsum.words(count=1, common=False).title()
            email = f"{lorem_ipsum.words(1, common=False)}{lorem_ipsum.words(1, common=False)}@{lorem_ipsum.words(1, common=False)}.noway"
            is_staff = False
            is_active = True
            password = "123"
            User.objects.create_user(username=username, first_name=first_name,
                                     last_name=last_name, email=email,
                                     is_active=is_active, is_staff=is_staff,
                                     password=password)
