from django.db import models

class Commodity(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PriceRecord(models.Model):
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.commodity.name} - {self.price}"
