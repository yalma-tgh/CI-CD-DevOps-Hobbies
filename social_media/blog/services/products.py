from django.db.models import QuerySet
from social_media.blog.models import Product


def create_product(name: str) -> QuerySet[Product]:
    return Product.objects.create(name=name)