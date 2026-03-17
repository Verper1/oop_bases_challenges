"""У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""

class BankAccount:
    """Класс для логики работы банковских операций."""
    def __init__(self, owner_full_name: str, balance: float) -> None:
        """Инициализатор для класса BankAccount."""
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, amount: float) -> None:
        """Повышает баланс на введенную сумму."""
        self.balance += amount

    def decrease_balance(self, amount: float) -> None:
        """Понижает баланс на введенную сумму."""
        self.balance -= amount


class CreditAccount(BankAccount):
    """Класс для логики работы кредитования."""
    def is_eligible_for_credit(self) -> bool:
        """Проверка на право выдать кредит."""
        return self.balance > 1000


if __name__ == '__main__':
    user_bank_account = BankAccount("Петров Олег Петрович", 52.5)
    user_credit_account = CreditAccount("Петров Олег Петрович", 52.5)

    print(user_bank_account.balance)

    user_bank_account.increase_balance(50)
    print(user_bank_account.balance)

    user_bank_account.decrease_balance(52)
    print(user_bank_account.balance)

    user_credit_account.increase_balance(23)
    print(user_credit_account.balance)

    user_credit_account.decrease_balance(11)
    print(user_credit_account.balance)

    print(user_credit_account.is_eligible_for_credit())
    user_credit_account.increase_balance(1200)
    print(user_credit_account.is_eligible_for_credit())

