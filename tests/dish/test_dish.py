# from src.models.dish import Dish
# from src.models.ingredient import Ingredient, Restriction
# import pytest

# # Req 2
# def test_dish():
#     dishA = Dish("CheeseCake", 10.0)
#     dishB = Dish("Espetinho", 20.0)

#     dishA.add_ingredient_dependency(Ingredient("queijo mussarela"), 10)

#     with pytest.raises(TypeError, match="Dish price must be float."):
#         Dish("CheeseCake", "1000")

#     with pytest.raises(ValueError, match="Dish price must be greater then zero."):
#         Dish("CheeseCake", -100)

#     assert dishA.name == 'CheeseCake'

#     assert hash(dishA) == hash(dishA)
#     assert hash(dishA) != hash(dishB)


#     assert dishA == dishA
  
#     assert repr(dishA) == "Dish('CheeseCake', R$10.00)"

#     assert dishA.get_restrictions() == {Restrictions.ANIMAL_DERIVED, Restrictions.LACTOSE,}
#     assert dishA.get_ingredients() == {Ingredient("queijo mussarela")}

from src.models.ingredient import Ingredient, Restriction
from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    dish1 = Dish("lasanha", 5.0)
    dish2 = Dish("manteiga", 4.0)

    dish1.add_ingredient_dependency(Ingredient("bacon"), 200)

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("lasanha", "xablau")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("lasanha", 0)

    assert dish1.name == "lasanha"

    assert hash(dish1) != hash(dish2)
    assert hash(dish1) == hash(dish1)

    assert dish1 == dish1

    assert repr(dish1) == "Dish('lasanha', R$5.00)"

    assert dish1.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }

    assert dish1.get_ingredients() == {Ingredient("bacon")}