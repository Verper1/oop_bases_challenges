"""
У нас есть различные типы классы для различных типов продуктов. Но мы ничего не знаем о том что происходит, когда мы вызываем
эти методы, хотелось бы простейшего логирования

Задания:
    1. Создайте класс PrintLoggerMixin и метод log у него, который будет принтить переданное в него сообщение.
    2. Используйте этот миксин, чтобы залогировать все методы у PremiumProduct и DiscountedProduct.
       Добавьте миксин и используйте новый метод во всех методах основных классов.
    3. Вызовите у экземпляров PremiumProduct и DiscountedProduct все возможные методы и убедитесь, что вызовы логируются.
"""

class PrintLoggerMixin:
    def log(self, message):
        print("LOGGING:", message)


class Product(PrintLoggerMixin):
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

        self.log(f"init={self.__class__.__name__} title={self.title}, price={self.price}")

    def get_info(self):
        self.log(f'Product {self.title} with price {self.price}')
        return f'Product {self.title} with price {self.price}'


class PremiumProduct(Product):
    def increase_price(self):
        self.price *= 1.2
        self.log(f"price = {self.price}")

    def get_info(self):
        base_info = super().get_info()
        self.log(f'{base_info} (Premium)')
        return f'{base_info} (Premium)'


class DiscountedProduct(Product):
    def decrease_price(self):
        self.price /= 1.2
        self.log(f"price = {self.price}")

    def get_info(self):
        base_info = super().get_info()
        self.log(f'{base_info} (Discounted)')
        return f'{base_info} (Discounted)'


if __name__ == '__main__':
    # Пример использования
    premium = PremiumProduct("Laptop", 1500)
    discounted = DiscountedProduct("Headphones", 300)

    # Вызов всех методов
    print("--- PremiumProduct ---")
    premium.get_info()
    premium.increase_price()
    premium.get_info()

    print("--- DiscountedProduct ---")
    discounted.get_info()
    discounted.decrease_price()
    discounted.get_info()

