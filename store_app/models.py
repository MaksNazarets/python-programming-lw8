from django.db import models


class Warehouse(models.Model):
    address = models.CharField(max_length=255)
    warehouse_manager = models.CharField(max_length=70)
    phone = models.CharField(max_length=20)

    def to_dict(self):
        return {
            'address': self.address,
            'warehouse_manager': self.warehouse_manager,
            'phone': self.phone,
        }


class Product(models.Model):
    type = models.CharField(max_length=255)
    clothing_name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity_in_stock = models.IntegerField()
    price = models.FloatField()

    def to_dict(self):
        return {
            'type': self.type,
            'clothing_name': self.clothing_name,
            'manufacturer': self.manufacturer,
            'warehouse': self.warehouse,
            'quantity_in_stock': self.quantity_in_stock,
            'price': self.price,
        }


class Client(models.Model):
    client_name = models.CharField(max_length=70)
    client_address = models.CharField(max_length=255)
    client_phone = models.CharField(max_length=20)

    def to_dict(self):
        return {
            'client_name': self.client_name,
            'client_address': self.client_address,
            'client_phone': self.client_phone,
        }


class Sale(models.Model):
    sale_date = models.DateField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_purchased = models.IntegerField()
    discount = models.FloatField()

    def to_dict(self):
        return {
            'sale_date': self.sale_date,
            'client': self.client,
            'product': self.product,
            'quantity_purchased': self.quantity_purchased,
            'discount': self.discount,
        }
