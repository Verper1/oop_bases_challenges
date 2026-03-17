import pytest
from level_2.b_user_should_be_banned import User

@pytest.mark.parametrize("test_name, test_surname, test_age, expected",
                         [
                             ("Виталя", 'Wilhelm', 35, "Пользователь забанен."),
                             ("Виталя", "Крутой", 105, "Пользователя нет в бан листе.")
                         ],
                         ids=[
                             "User should be banned",
                             "User should not be banned"
                         ])
def test__user_should_be_banned__test_varios_params(test_name: str,
                                                    test_surname: str,
                                                    test_age: int,
                                                    expected: str) -> None:
    user = User(name=test_name, surname=test_surname, age=test_age)  # Arrange

    user_should_be_banned = user.user_should_be_banned()  # Act

    assert user_should_be_banned == expected  # Assert
