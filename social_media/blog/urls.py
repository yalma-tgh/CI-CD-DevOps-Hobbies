from django.urls import path, include
from social_media.blog.apis.products import ProductApi

urlpatterns = [
    path('product/', ProductApi.as_view(),name="product"),
]