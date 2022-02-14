from main.models import Product
from main.serializers import ProductSerializer
from main.tests.factories import PriceHistoryFactory, ProductFactory
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status



@pytest.mark.django_db
def test__get_products_by_price__success():
    client = APIClient()
    product_in_response = ProductFactory()
    product_not_in_response = ProductFactory()
    PriceHistoryFactory(product=product_in_response, price=200)
    PriceHistoryFactory(product=product_not_in_response, price=1000)

    path = reverse("product-products-by-price")
    response = client.get(path, {"value": 200})
    assert response.status_code == status.HTTP_200_OK
    assert (
        ProductSerializer(Product.objects.all(), many=True).data
        != response.data
    )
    assert Product.objects.filter(prices__price__lte=200).count() == len(
        response.data
    )
    assert [ProductSerializer(product_in_response).data] == response.data
