from django.db import models

class Order(models.Model):
    code = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField()
    weight = models.FloatField()
    volume = models.FloatField()
    package = models.ForeignKey("package.Package", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Order {self.code} - {self.weight}kg"
