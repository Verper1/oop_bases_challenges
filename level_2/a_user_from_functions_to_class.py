"""У нас есть функции для работы с пользователем, но хочется работать с ним через класс.

Задания:
    1. Создайте класс User и перенесите всю логику работы с пользователем туда.
"""
import dataclasses


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class User:
    """Класс юзера для хранения инфы о человеке."""
    user_id: int
    username: str
    name: str

    def make_username_capitalized(self) -> str:
        """Возвращает строку с большой буквы."""
        return self.username.capitalize()

    def generate_short_user_description(self) -> str:
        """Создаёт краткое описание юзера."""
        return f'User with id {self.user_id} has {self.username} username and {self.name} name'

