"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""

from d_bank_account_increase_balance import BankAccount

class BankAccountUpdated(BankAccount):
    def decrease_balance(self, outcome: float) -> float | ValueError:
        if self.balance - outcome < 0:
            raise ValueError("Ошибка! Баланс не может быть отрицательным.")
        self.balance -= outcome
        return self.balance


if __name__ == '__main__':
    spam: BankAccountUpdated = BankAccountUpdated("Олегов Олег Олегович", 250.32)
    print(spam.show_balance())
    spam.decrease_balance(200.12)
    print(spam.show_balance())
    spam.decrease_balance(255.18)
    print(spam.show_balance())
