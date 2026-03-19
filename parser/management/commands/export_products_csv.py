import csv

from django.core.management import BaseCommand
from parser.models import Parser


class Command(BaseCommand):
    help = 'Export products csv'

    def handle(self, *args, **options):

        with open("products.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "color", "characteristics"])
            for parser in Parser.objects.all():
                writer.writerow([parser.name, parser.color, parser.characteristics])
        self.stdout.write(self.style.SUCCESS("CSV exported successfully"))
