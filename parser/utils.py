import re

from bs4 import BeautifulSoup

import requests
from pprint import pprint


class ParserUtils:
    def __init__(self, parse_url: str):
        self.parse_url = parse_url
        self.soup = None

    def get_html(self):
        if self.soup is not None:
            return self.soup

        try:
            response = requests.get(self.parse_url, timeout=5)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            return None
        except requests.exceptions.RequestException:
            return None
        soup = BeautifulSoup(response.content, 'html.parser')
        self.soup = soup
        return soup


class BrainMobileParse:
    def __init__(self, soup: BeautifulSoup):
        self.soup = soup

    def get_characteristics(self):
        characteristics = self.soup.find("div", id="br-characteristics")
        if characteristics is not None:
            characteristics_dict = {}
            for rows in characteristics.find_all("div"):
                spans = rows.find_all("span", recursive=False)
                if len(spans) == 2:
                    key = spans[0].text.strip()
                    value = spans[1].text.strip()
                    characteristics_dict[key] = value
            return characteristics_dict
        return {}

    def get_full_name(self):
        results_full_name = self.soup.find("h1", class_="desktop-only-title")
        if results_full_name:
            return results_full_name.text.strip()
        return None

    def get_color(self):
        try:
            color = self.get_characteristics().get("Колір")
        except AttributeError:
            return None

        return color

    def get_memory(self):
        try:
            memory = self.get_characteristics().get("Вбудована пам'ять")
        except AttributeError:
            return None

        return memory

    def get_manufacturer(self):
        try:
            manufacturer = self.get_characteristics().get("Виробник")
        except AttributeError:
            return None

        return manufacturer

    def get_screen_diagonal(self):
        try:
            screen_diagonal = self.get_characteristics().get("Діагональ екрану")
        except AttributeError:
            return None

        return screen_diagonal

    def get_display_resolution(self):
        try:
            display_resolution = self.get_characteristics().get("Роздільна здатність екрану")
        except AttributeError:
            return None

        return display_resolution

    def get_product_code(self):
        product_code = self.soup.find("div", id="product_code")
        if product_code:
            spans = product_code.find_all("span", recursive=False)
            return spans[1].text.strip()
        return None

    def get_number_of_reviews(self):
        try:
            reviews_block = self.soup.find("div", id="reviews")
            a_tag = reviews_block.find("a", recursive=False)
            match = re.search(r'\d+', a_tag.text)
            return int(match.group())
        except (AttributeError, TypeError):
            return None

    def get_price_is_ordinary(self):
        try:
            price_block = self.soup.find("div", class_="br-pr-price main-price-block")
            price_span = price_block.find("span")
            price_text = price_span.text.strip().replace(" ", "")
            return int(price_text)
        except (AttributeError, TypeError, ValueError):
            return None

    def get_all_photos(self):
        try:
            img_tags = self.soup.find_all("img", class_="br-main-img")
            img_urls = [img['src'] for img in img_tags if img.get('src')]
            return img_urls
        except AttributeError:
            return []

    def get_promotional_price(self):
        promo_block = self.soup.find("div", class_="br-pr-price sale-price-block")
        if promo_block:
            span = promo_block.find("span")
            if span:
                return int(span.text.strip().replace(" ", ""))
        return None

    def get_data(self):
        return {
            "full_name": self.get_full_name(),
            "color": self.get_color(),
            "memory": self.get_memory(),
            "manufacturer": self.get_manufacturer(),
            "screen_diagonal": self.get_screen_diagonal(),
            "display_resolution": self.get_display_resolution(),
            "product_code": self.get_product_code(),
            "number_of_reviews": self.get_number_of_reviews(),

            "price_ordinary": self.get_price_is_ordinary(),
            "price_promotional": self.get_promotional_price(),
            "photos": self.get_all_photos(),
            "characteristics": self.get_characteristics()
        }


if __name__ == '__main__':
    url = 'https://brain.com.ua/ukr/Mobilniy_telefon_Apple_iPhone_16_Pro_Max_256GB_Black_Titanium-p1145443.html'
    parser = ParserUtils(parse_url=url)
    soup = parser.get_html()
    mobile = BrainMobileParse(soup=soup)

    data = {
        "full_name": mobile.get_full_name(),
        "color": mobile.get_color(),
        "memory": mobile.get_memory(),
        "manufacturer": mobile.get_manufacturer(),
        "price_ordinary": mobile.get_price_is_ordinary(),
        "price_promotional": mobile.get_promotional_price(),
        "photos": mobile.get_all_photos(),
        "product_code": mobile.get_product_code(),
        "number_of_reviews": mobile.get_number_of_reviews(),
        "screen_diagonal": mobile.get_screen_diagonal(),
        "display_resolution": mobile.get_display_resolution(),
        "characteristics": mobile.get_characteristics()
    }

    pprint(data)
