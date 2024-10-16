import pytest
from praktikum.ingredient import Ingredient
from data import TestBurger

class TestIngredient:

    @pytest.mark.parametrize("ingredient_data", TestBurger.INGREDIENT_PARAMS)
    def test_ingredient_get_price(self, ingredient_data):
        ingredient = Ingredient(ingredient_data["type"], ingredient_data["name"], ingredient_data["price"])
        assert ingredient.get_price() == ingredient_data["price"]

    @pytest.mark.parametrize("ingredient_data", TestBurger.INGREDIENT_PARAMS)
    def test_ingredient_get_name(self, ingredient_data):
        ingredient = Ingredient(ingredient_data["type"], ingredient_data["name"], ingredient_data["price"])
        assert ingredient.get_name() == ingredient_data["name"]

    @pytest.mark.parametrize("ingredient_data", TestBurger.INGREDIENT_PARAMS)
    def test_ingredient_get_type(self, ingredient_data):
        ingredient = Ingredient(ingredient_data["type"], ingredient_data["name"], ingredient_data["price"])
        assert ingredient.get_type() == ingredient_data["type"]


