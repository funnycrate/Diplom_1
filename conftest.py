import pytest
from unittest.mock import Mock
from data import TestBurger

@pytest.fixture(scope='class')
def mock_bun():
    bun_data = TestBurger.BUN_PARAMS[0]
    mock_bun = Mock()
    mock_bun.get_name.return_value = bun_data["name"]
    mock_bun.get_price.return_value = bun_data["price"]
    return mock_bun

@pytest.fixture(scope='class')
def mock_ingredient1():
    # Используем данные первого ингредиента из INGREDIENT_PARAMS
    ingredient_data = TestBurger.INGREDIENT_PARAMS[0]
    mock_ingredient1 = Mock()
    mock_ingredient1.get_price.return_value = ingredient_data["price"]
    mock_ingredient1.get_name.return_value = ingredient_data["name"]
    mock_ingredient1.get_type.return_value = ingredient_data["type"]
    return mock_ingredient1

@pytest.fixture(scope='class')
def mock_ingredient2():
    # Используем данные второго ингредиента из INGREDIENT_PARAMS
    ingredient_data = TestBurger.INGREDIENT_PARAMS[1]
    mock_ingredient2 = Mock()
    mock_ingredient2.get_price.return_value = ingredient_data["price"]
    mock_ingredient2.get_name.return_value = ingredient_data["name"]
    mock_ingredient2.get_type.return_value = ingredient_data["type"]
    return mock_ingredient2


@pytest.fixture(scope='class')
def mock_database(mock_bun, mock_ingredient1, mock_ingredient2):
    mock_db = Mock()

    # Замокаем метод available_buns
    mock_db.available_buns.return_value = [mock_bun]

    # Замокаем метод available_ingredients
    mock_db.available_ingredients.return_value = [mock_ingredient1, mock_ingredient2]

    return mock_db