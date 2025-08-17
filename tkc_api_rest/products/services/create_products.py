from tkc_api_rest.products.models import Product
from tkc_api_rest.orders.models import Order


def create_products(order: Order, products: list):
    product_instances = [
        Product(
            name=product["name"],
            external_id=product["product_id"],
            order=order,
        )
        for product in products
    ]
    return Product.objects.bulk_create(product_instances)
