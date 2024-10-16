import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:

    # Тест на проверку доступных булок
    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()

        # Проверяем, что список булок не пустой и содержит 3 элемента
        assert len(buns) == 3

        # Проверяем тип данных
        for bun in buns:
            assert isinstance(bun, Bun)

        # Проверяем конкретные булки
        assert buns[0].get_name() == "black bun"
        assert buns[0].get_price() == 100
        assert buns[1].get_name() == "white bun"
        assert buns[1].get_price() == 200
        assert buns[2].get_name() == "red bun"
        assert buns[2].get_price() == 300

    # Тест на проверку доступных ингредиентов
    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()

        # Проверяем, что список ингредиентов не пустой и содержит 6 элементов
        assert len(ingredients) == 6

        # Проверяем тип данных
        for ingredient in ingredients:
            assert isinstance(ingredient, Ingredient)

        # Проверяем конкретные ингредиенты
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[0].get_type() == "SAUCE"
        assert ingredients[0].get_price() == 100
        assert ingredients[5].get_name() == "sausage"
        assert ingredients[5].get_type() == "FILLING"
        assert ingredients[5].get_price() == 300
