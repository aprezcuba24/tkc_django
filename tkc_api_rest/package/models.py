from django.db import models


class Package(models.Model):
    types = (
        ("SHIPPING", "Shipping"),
        ("RECEIVING", "Receiving"),
    )

    code = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField()
    weight = models.FloatField()
    volume = models.FloatField()
    package_type = models.CharField(max_length=50, choices=types, default="SHIPPING")

    def __str__(self):
        return f"Package {self.code} - {self.weight}kg"