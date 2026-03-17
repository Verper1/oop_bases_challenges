from level_3.d_alcohol_product import AlcoholProduct
from freezegun import freeze_time

@freeze_time("2026-03-16 11:00:00")
def test__is_available__i_can_buy_beer_now_because_11_am():
    beer = AlcoholProduct("beer", 75, 3)

    assert beer.is_available() == "По паре баночек можно)"

@freeze_time("2026-03-17 1:00:00")
def test__is_available__i_can_not_buy_beer_now_because_1_am():
    beer = AlcoholProduct("beer", 75, 3)

    assert beer.is_available() == "Спать((("
