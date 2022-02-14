import factory


class UnitFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "main.MeasurementUnit"

    title = "штука"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "main.Product"

    title = "ноутбуки"
    unit = factory.SubFactory(UnitFactory)


class PriceHistoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "main.PriceHistory"

    price = factory.Faker("pydecimal", min_value=100, max_value=1000)
    date_from = "2022-02-14"
    product = factory.SubFactory(ProductFactory)
