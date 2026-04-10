import factory
from factory.fuzzy import FuzzyChoice, FuzzyDecimal
from service.models import Product, Category

class ProductFactory(factory.Factory):
    """Creates fake products for testing"""

    class Meta:
        """Maps factory to data model"""
        model = Product

    id = factory.Sequence(lambda n: n)

    # Task: Gunakan FuzzyChoice untuk nama produk
    name = FuzzyChoice(
        choices=[
            "Hat", "Pants", "Shirt", "Apple", "Banana", 
            "Pots", "Towels", "Ford", "Chevy", "Hammer", "Wrench"
        ]
    )

    # Task: Gunakan faker untuk deskripsi
    description = factory.Faker("text")

    # Task: Gunakan FuzzyDecimal untuk harga (min: 0.5, max: 2000.0, precision: 2)
    price = FuzzyDecimal(0.5, 2000.0, 2)

    # Task: Gunakan FuzzyChoice untuk status ketersediaan
    available = FuzzyChoice(choices=[True, False])

    # Task: Gunakan FuzzyChoice untuk kategori (mengambil dari Enum Category)
    category = FuzzyChoice(
        choices=[
            Category.UNKNOWN,
            Category.CLOTHS,
            Category.FOOD,
            Category.HOUSEWARES,
            Category.AUTOMOTIVE,
            Category.TOOLS,
        ]
    )