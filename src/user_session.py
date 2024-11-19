from src.ingredient import Ingredient

class UserSession:
    def __init__(self):
        self.ingredients = []
        self.recipes = []

    def add_ingredient(self, ingredient_name):
        ingredient = Ingredient(ingredient_name)
        self.ingredients.append(ingredient)

    def clear_ingredients(self):
        self.ingredients = []
