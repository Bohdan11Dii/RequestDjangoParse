from django.db import models


class Parser(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=100)
    memory = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)

    price_ordinary = models.DecimalField(max_digits=10, decimal_places=2)
    price_promotional = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    product_code = models.CharField(max_length=100, unique=True)

    number_of_reviews = models.IntegerField(null=True,
                                            blank=True)
    screen_diagonal = models.CharField(max_length=100)
    display_resolution = models.CharField(max_length=100)

    characteristics = models.JSONField()
    images = models.JSONField()  # список URL

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
