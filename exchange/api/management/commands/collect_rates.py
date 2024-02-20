from datetime import datetime

import requests
from django.core.management.base import BaseCommand

from api.models import Currency


class Command(BaseCommand):
    help = "Collect currency exchange rates from CBR daily_json.js and store them in the database"

    def handle(self, *args, **options):
        response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
        rates = response.json().get("Valute")

        for charcode, data in rates.items():
            currency, created = Currency.objects.get_or_create(
                charcode=charcode,
                date=datetime.now().date(),
                defaults={"rate": data.get("Value")},
            )
            if not created:
                currency.rate = data.get("Value")
                currency.save()
