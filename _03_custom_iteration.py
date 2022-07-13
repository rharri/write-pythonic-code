"""Supporting iteration with a custom type"""


from decimal import Decimal
import locale
from typing import Iterator


class Item:
    def __init__(self, name: str, price: Decimal) -> None:
        self.name: str = name
        self.price: Decimal = price


class ShoppingCart:
    def __init__(self) -> None:
        self.items: list[Item] = []

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def __iter__(self) -> Iterator[Item]:
        return self.items.__iter__()


cart = ShoppingCart()
cart.add_item(Item("apple", Decimal("2.99")))
cart.add_item(Item("cheese", Decimal("6.79")))
cart.add_item(Item("lettuce", Decimal("1.69")))

locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

print("Shopping List:")
for index, item in enumerate(cart):
    print(f"{index+1}. {item.name:<10} {locale.currency(item.price):>5}")
