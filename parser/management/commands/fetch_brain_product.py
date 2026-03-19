from django.core.management.base import BaseCommand
from django.http import Http404

from parser.models import Parser
from parser.utils import ParserUtils, BrainMobileParse


class Command(BaseCommand):
    help = "Fetch product from brain.com.ua"

    def handle(self, *args, **options):
        url = 'https://brain.com.ua/ukr/Mobilniy_telefon_Apple_iPhone_16_Pro_Max_256GB_Black_Titanium-p1145443.html'
        parser = ParserUtils(parse_url=url)
        soup = parser.get_html()
        print("Початок роботи...")
        if not soup:
            return self.stderr.write("Помилка: Не вдалося отримати HTML")

        mobile = BrainMobileParse(soup=soup)

        data = mobile.get_data()

        self.stdout.write(str(data))

        product, created = Parser.objects.update_or_create(
            name=data['full_name'],
            color=data['color'],
            memory=data['memory'],

            manufacturer=data['manufacturer'],
            price_ordinary=data['price_ordinary'],
            price_promotional=data['price_promotional'],

            product_code=data['product_code'],

            number_of_reviews=data['number_of_reviews'],
            screen_diagonal=data['screen_diagonal'],
            display_resolution=data['display_resolution'],

            characteristics=data['characteristics'],

            images=data['photos'],

        )

        self.stdout.write(str(product))
