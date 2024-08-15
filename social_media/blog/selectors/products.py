from django.db.models import QuerySet
from social_media.blog.models import Product


def get_products() -> QuerySet[Product]:
    return Product.objects.all()