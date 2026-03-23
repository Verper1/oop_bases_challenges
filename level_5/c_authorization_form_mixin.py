"""
У нас есть класс формы и метод для валидации в нем. Мы хотим создать форму для авторизации, где нам важно чтобы юзернэйм
существовал в базе данных

Задания:
    1. Напишите логику метода valid_form в классе AuthorizationFormMixin таким образом, чтобы там была проверка и из
       класса Form и проверка на то что юзернэйм есть в списке USERNAMES_IN_DB. Нужно использовать super() в этом методе
    2. Создайте класс AuthorizationForm, который будет наследником и от Form и от AuthorizationFormMixin
    3. Создайте экземпляр класса AuthorizationForm и вызовите у него метод valid_form. Должны отрабатывать обе проверки:
       и на длину пароля и на наличия юзернэйма в базе
"""
USERNAMES_IN_DB = ['Alice_2023', 'BobTheBuilder', 'CrazyCoder', 'DataDiva', 'EpicGamer', 'JavaJunkie']


class Form:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def valid_form(self):
        return len(self.password) > 8


class AuthorizationFormMixin:
    def valid_form(self):
        return super().valid_form() and self.username in USERNAMES_IN_DB


class AuthorizationForm(AuthorizationFormMixin, Form):
    pass


if __name__ == '__main__':
    good_user = AuthorizationForm('Alice_2023', "123456789")
    print(good_user.valid_form())

    correct_nick_but_incorrect_pass = AuthorizationForm('Alice_2023', "12345678")
    print(correct_nick_but_incorrect_pass.valid_form())

    correct_pass_but_wrong_nick = AuthorizationForm('Alice_202321', "123456789")
    print(correct_pass_but_wrong_nick.valid_form())
