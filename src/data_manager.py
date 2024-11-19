class DataManager:
    def __init__(self):
        self.cache = {}

    def get_cached_recipe(self, recipe_id):
        return self.cache.get(recipe_id)

    def cache_recipe(self, recipe_id, data):
        self.cache[recipe_id] = data
