from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction
import pytest

# Req 2
def test_dish():
    dishA = Dish("CheeseCake", 10.0)
    dishB = Dish("Espetinho", 20.0)

    dishA.AddIngredientDependency(Ingredient("queijo mussarela"), 10)

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("CheeseCake", "1000")

    with pytest.raises(ValueError, match="Dish price must be greater then zero."):
        Dish("CheeseCake", -100)

    assert dishA == 'CheeseCake'

    assert hash(dishA) == hash(dishA)
    assert hash(dishA) != hash(dishB)


    assert dishA == dishA
    assert dishA != dishB

    assert repr(dishA) == "Dish('CheeseCake', R$10.00)"

    assert dishA.name == "CheeseCake"
    assert dishA.price == 10.0

    assert dishA.recipe == {}

    assert dishA.get_restrictions() == {Restrictions.ANIMAL_DERIVED, Restrictions.LACTOSE}
    assert dishA.get_ingredients() == {Ingredient("queijo mussarela")}
