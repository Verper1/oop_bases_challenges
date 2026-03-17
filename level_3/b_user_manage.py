"""У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    """Класс для логики работы менеджера."""
    def __init__(self) -> None:
        """Инициализатор класса UserManager."""
        self.usernames: list[str] = []

    def add_user(self, username: str) -> None:
        """Добавляет юзера в список usernames."""
        self.usernames.append(username)

    def get_users(self) -> list[str]:
        """Возвращает список usernames."""
        return self.usernames


class AdminManager(UserManager):
    """Класс для логики работы админ менеджера."""
    def ban_username(self, usename: str) -> None | str:
        """Убирает юзера из списка usernames или возвращает строку, если такого пользователя нет."""
        if usename in self.usernames:
            self.usernames.remove(usename)
            return None
        else:
            return "Такого пользователя не существует."


class SuperAdminManager(AdminManager):
    """Класс для логики работы супермегадупер менеджера."""
    def ban_all_users(self) -> None:
        """Очищает весь список usernames."""
        self.usernames.clear()

if __name__ == '__main__':
    # --- UserManager ---
    user_manager = UserManager()

    user_manager.add_user("Иван")
    user_manager.add_user("Петр")

    print("UserManager users:", user_manager.get_users())

    # --- AdminManager ---
    admin_manager = AdminManager()

    admin_manager.add_user("Сергей")
    admin_manager.add_user("Анна")

    print("AdminManager users:", admin_manager.get_users())

    admin_manager.ban_username("Сергей")
    print("AdminManager users after ban:", admin_manager.get_users())

    print(admin_manager.ban_username("Не существует"))

    # --- SuperAdminManager ---
    super_admin_manager = SuperAdminManager()

    super_admin_manager.add_user("User1")
    super_admin_manager.add_user("User2")

    print("SuperAdminManager users:", super_admin_manager.get_users())

    super_admin_manager.ban_username("User1")
    print("After banning User1:", super_admin_manager.get_users())

    super_admin_manager.ban_all_users()
    print("After banning all users:", super_admin_manager.get_users())
