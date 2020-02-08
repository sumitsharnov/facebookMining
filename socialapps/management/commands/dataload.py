import os
import json
import facebook
import requests
import shutil
from django.core.management import BaseCommand

from socialapps.management.commands.facebook import Fb
from socialapps.models import Item

class Command(BaseCommand):
    def handle(self, *args, **options):
        fb = Fb()
        print("Connecting to facebook")
        print(Item.objects.values('image_url').count())
        token = 'EAArJ24yFWawBAAanO1bnYMirhQkiGB0EPK2eymCwgX2Q1ho70PuGbHZBTIZB4KPePvB3AzFyEITCTcpDMjaQvsyk6PCz7HlcYgqikouZAAj6I3Jprox45znidOcZBu2muixF9HQ8ryEtvIZBT8j0RZAVH93ioNceS65Vbuv5wcBgZDZD'
        graph = facebook.GraphAPI(token)
        fb.fb(graph)
