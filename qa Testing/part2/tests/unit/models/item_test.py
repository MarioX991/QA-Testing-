from unittest import TestCase
from models.item import ItemModel


class ItemTest(TestCase):
    """
    We wrote tests for:
        - test for init method
        - test for json method
    """
    def test_create_item(self):
        item = ItemModel("test", 19.99)
        print("----------------\n")
        print(item.name)
        self.assertEqual(item.name, "test",
                         "The name of the item after creation does not equal the constructor argument")
        self.assertEqual(item.price, 19.99,
                         "The price of the item after creation does not equal the constructor argument")

    def test_item_json(self):
        item = ItemModel("test", 13.44)
        expected_output = {
            "name": "test",
            "price": 13.44
        }

        self.assertDictEqual(item.json(), expected_output,
                             f"The JSON export of the item is incorrect. Recived {item.json()} expected {expected_output}")
