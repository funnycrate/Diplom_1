import pytest
from data import TestBurger
from praktikum.bun import Bun

class TestBun:

    @pytest.mark.parametrize("bun_data", TestBurger.BUN_PARAMS)
    def test_bun_get_name(self, bun_data):
        bun = Bun(bun_data["name"], bun_data["price"])
        assert bun.get_name() == bun_data["name"]

    @pytest.mark.parametrize("bun_data", TestBurger.BUN_PARAMS)
    def test_bun_get_price(self, bun_data):
        bun = Bun(bun_data["name"], bun_data["price"])
        assert bun.get_price() == bun_data["price"]

