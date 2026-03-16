"""У нас есть класс Product, который содержит в себе информацию о продукте.

Еще у нас есть класс AlcoholProduct, но метод is_available для него не подходит, так как
алкоголь нельзя продавать с 5 утра до 11 вечера.

Задания:
    1. Переопределите метод is_available в классе AlcoholProduct с использованием super()
    2. is_available у AlcoholProduct должен возвращать False если сейчас часы между 5 утра и 11 вечера.
       Для определения текущего часа можно использовать datetime.now().hour
    3. Создайте экземпляр класса AlcoholProduct и проверьте, можно ли сейчас продавать алкоголь.
"""
from datetime import datetime


class Product:
    """Класс для логики продукта в системе."""
    def __init__(self, title: str, price: float, stock_quantity: int) -> None:
        """Инициализатор класса Product."""
        self.title = title
        self.price = price
        self.stock_quantity = stock_quantity

    def get_discounted_price(self, discount_percentage: int) -> float:
        """Возвращает рассчитанную скидку на товар."""
        return self.price * (1 - discount_percentage / 100)

    def is_available(self) -> int:
        """Проверяет есть ли товар в наличии."""
        return self.stock_quantity >= 0


class AlcoholProduct(Product):
    """Класс для логики алкогольного продукта в системе."""
    def is_available(self) -> str:  # error: Return type "str" of "is_available" incompatible with return type "int" in supertype "Product"  [override]
        """Проверка есть ли товар на складе и можно ли сейчас его продавать."""
        is_available_check = super().is_available() and 5 < datetime.now().hour < 23
        if is_available_check:
            return "По паре баночек можно)"
        else:
            return "Спать((("

        # return super().is_available() and 5 < datetime.now().hour < 23


# if __name__ == '__main__':
#     beer = AlcoholProduct("beer", 75, 3)
#
#     print(beer.is_available())
