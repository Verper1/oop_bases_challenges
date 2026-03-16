import pytest
from level_2.a_user_from_functions_to_class import User

@pytest.mark.parametrize("test_username", [("большой босс")], ids=["username_capitalized"])
def test__make_username_capitalized__username_capitalized(test_username: str) -> None:
    user = User()  # Arrange

    username_capitalized = user.make_username_capitalized(test_username)  # Act

    assert username_capitalized == "Большой босс"  # Assert


@pytest.mark.parametrize("test_username, test_user_id, test_name",
                         [("Большой босс", 232, "Виталя")],
                         ids=["short_user_description"])
def test__generate_short_user_description__short_user_description_was_given(
        test_username: str,
        test_user_id: int,
        test_name: str) -> None:
    user = User()  # Arrange

    short_user_description = user.generate_short_user_description(test_username,
                                                                test_user_id,
                                                                test_name)  # Act

    assert short_user_description == f'User with id 232 has Большой босс username and Виталя name'  # Assert

