import pytest
from unittest.mock import Mock, patch
from praktikum.burger import Burger
from data import TestBurger

@patch('praktikum.ingredient_types.INGREDIENT_TYPE_FILLING', 'MOCK_FILLING')
@patch('praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE', 'MOCK_SAUCE')
class TestBurgerClass:

    # Параметризация теста на добавление ингредиента
    @pytest.mark.parametrize("ingredient_data", TestBurger.INGREDIENT_PARAMS)
    def test_burger_add_ingredient(self, ingredient_data):
        # Создаем мок ингредиента, используя данные из параметров
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = ingredient_data["name"]
        mock_ingredient.get_price.return_value = ingredient_data["price"]
        mock_ingredient.get_type.return_value = ingredient_data["type"]

        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        # Проверяем, что ингредиент добавлен
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].get_name() == ingredient_data["name"]
        assert burger.ingredients[0].get_price() == ingredient_data["price"]
        assert burger.ingredients[0].get_type() == ingredient_data["type"]

    # Параметризация теста на общую цену
    @pytest.mark.parametrize("bun_data, ingredient_data1, ingredient_data2, expected_total", [
        (TestBurger.BUN_PARAMS[0], TestBurger.INGREDIENT_PARAMS[0], TestBurger.INGREDIENT_PARAMS[1], 400),
        (TestBurger.BUN_PARAMS[1], TestBurger.INGREDIENT_PARAMS[1], TestBurger.INGREDIENT_PARAMS[0], 600),
    ])
    def test_burger_total_price(self, mock_bun, mock_ingredient1, mock_ingredient2, bun_data, ingredient_data1, ingredient_data2, expected_total):
        # Мокаем булку и ингредиенты на основе параметров
        mock_bun.get_name.return_value = bun_data["name"]
        mock_bun.get_price.return_value = bun_data["price"]

        mock_ingredient1.get_name.return_value = ingredient_data1["name"]
        mock_ingredient1.get_price.return_value = ingredient_data1["price"]
        mock_ingredient1.get_type.return_value = ingredient_data1["type"]

        mock_ingredient2.get_name.return_value = ingredient_data2["name"]
        mock_ingredient2.get_price.return_value = ingredient_data2["price"]
        mock_ingredient2.get_type.return_value = ingredient_data2["type"]

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        # Проверяем общую цену
        assert burger.get_price() == expected_total

    # Тест на удаление ингредиента
    def test_burger_remove_ingredient(self, mock_bun, mock_ingredient1, mock_ingredient2):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        # Удаляем первый ингредиент
        burger.remove_ingredient(0)

        # Проверяем, что ингредиент удалён
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient2

    # Тест на перемещение ингредиента
    def test_burger_move_ingredient(self, mock_bun, mock_ingredient1, mock_ingredient2):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        # Перемещаем второй ингредиент на первое место
        burger.move_ingredient(1, 0)

        # Проверяем, что ингредиенты поменялись местами
        assert burger.ingredients[0] == mock_ingredient2
        assert burger.ingredients[1] == mock_ingredient1

    def test_burger_get_receipt(self, mock_bun, mock_ingredient1, mock_ingredient2):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        expected_receipt = (
            f'(==== {mock_bun.get_name.return_value} ====)\n'
            f'= {mock_ingredient1.get_type.return_value.lower()} {mock_ingredient1.get_name.return_value} =\n'
            f'= {mock_ingredient2.get_type.return_value.lower()} {mock_ingredient2.get_name.return_value} =\n'
            f'(==== {mock_bun.get_name.return_value} ====)\n\n'
            f'Price: {mock_bun.get_price.return_value * 2 + mock_ingredient1.get_price.return_value + mock_ingredient2.get_price.return_value}'
        )

        assert burger.get_receipt() == expected_receipt
