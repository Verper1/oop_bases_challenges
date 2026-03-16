"""Нам необходимо проверить, находится ли фамилия пользователя в списке запрещенных.

Задания:
    1. Создайте класс юзера, у которого параметры: имя, фамилия, возраст.
    2. Добавьте ему метод should_be_banned, который проверяет, должен ли быть пользователь забанен.
       Пользователя стоит забанить, если его фамилия находится в SURNAMES_TO_BAN.
"""
import dataclasses

SURNAMES_TO_BAN = ['Vaughn', 'Wilhelm', 'Santaros', 'Porter', 'Smith']

@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class User:
    """Класс для хранения инфо о юзере и проверки юзера на бан."""
    name: str
    surname: str
    age: int

    @staticmethod
    def user_should_be_banned(surname:str, SURNAMES_TO_BAN: list[str]) -> str:
        """Проверяет есть ли юзер в списке забаненных и есть, то банит его."""
        if surname in SURNAMES_TO_BAN:
            return "Пользователь забанен."
        else:
            return "Пользователя нет в бан листе."
