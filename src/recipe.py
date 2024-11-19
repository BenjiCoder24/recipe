from src.ingredient import Ingredient

class Recipe:
    def __init__(self, data):
        self.title = data.get('title')
        self.ingredients = [Ingredient(i['name']) for i in data.get('extendedIngredients', [])]
        self.instructions = data.get('instructions')
        self.image_url = data.get('image')
        self.source_url = data.get('sourceUrl')
        self.nutrition_info = data.get('nutrition', {})

    def matches_ingredients(self, user_ingredients):
        recipe_ingredient_names = {ing.name for ing in self.ingredients}
        user_ingredient_names = {ing.name for ing in user_ingredients}
        return recipe_ingredient_names.issubset(user_ingredient_names)
