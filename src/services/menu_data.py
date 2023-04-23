import csv
from models.dish import Dish

from models.ingredient import Ingredient

class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        with open(source_path, "r") as csv_file:
            csv_reader = list(csv.DictReader(csv_file, delimiter=","))
            current_dish = Dish(csv_reader[0]["dish"], float(csv_reader[0]["price"]))
        
            current_dish.add_ingredient_dependency(
                Ingredient(csv_reader[0]["ingredient"]),
                int(csv_file[0]["recipe_amount"]), 
            )

            self.dishes.add(current_dish)

        for row in csv_reader[1:]:
            new_dish = Dish(row_menu["dish"], float(row_menu["price"]))
            new_ingredient = Ingredient(row_menu["ingredient"])
            amount = int(row_menu["recipe_amount"])
            dish_menu = list(self.dishes)[0]

            if new_dish.name == dish_menu.name:
                current_dish.add_ingredient_dependency(new_ingredient, amount)
            else:
                current_dish = new_dish
                current_dish.add_ingredient_dependency(new_ingredient, amount)
                new_dish.add_ingredient_dependency(new_ingredient, amount)