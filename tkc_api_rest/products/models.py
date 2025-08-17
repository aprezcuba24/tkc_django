from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    external_id = models.CharField(max_length=50, unique=True)
    order = models.ForeignKey("orders.Order", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
