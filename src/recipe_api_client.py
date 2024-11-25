import requests

class RecipeAPIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.spoonacular.com'

    def search_recipes(self, ingredients):
        endpoint = f'{self.base_url}/recipes/findByIngredients'
        params = {
            'ingredients': ','.join(ing.name for ing in ingredients),
            'number': 10,
            'apiKey': self.api_key
        }
        response = requests.get(endpoint, params=params)
        try:
            # Ensure the response is parsed as JSON
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching recipes: {e}")
            return []  # Return an empty list on error

    def get_recipe_details(self, recipe_id):
        endpoint = f'{self.base_url}/recipes/{recipe_id}/information'
        params = {'apiKey': self.api_key}
        response = requests.get(endpoint, params=params)
        try:
            # Ensure the response is parsed as JSON
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching recipe details: {e}")
            return {}
