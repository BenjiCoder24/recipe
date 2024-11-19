import streamlit as st
from src.recipe import Recipe

class AppUI:
    def __init__(self, api_client, user_session):
        self.api_client = api_client
        self.user_session = user_session

    def run(self):
        st.title("Recipe Suggestion App")
        self.display_ingredient_input()
        if st.button("Find Recipes"):
            self.find_and_display_recipes()

    def display_ingredient_input(self):
        ingredient_input = st.text_input("Enter an ingredient:")
        if st.button("Add Ingredient"):
            self.user_session.add_ingredient(ingredient_input)
        st.write("Your Ingredients:")
        for ing in self.user_session.ingredients:
            st.write(f"- {ing.name}")

    def find_and_display_recipes(self):
        recipes_data = self.api_client.search_recipes(self.user_session.ingredients)
        self.user_session.recipes = [Recipe(data) for data in recipes_data]
        self.display_recipe_suggestions(self.user_session.recipes)

    def display_recipe_suggestions(self, recipes):
        for recipe in recipes:
            if st.button(recipe.title):
                recipe_details = self.api_client.get_recipe_details(recipe_id=recipe.id)
                detailed_recipe = Recipe(recipe_details)
                self.display_recipe_details(detailed_recipe)

    def display_recipe_details(self, recipe):
        st.header(recipe.title)
        st.image(recipe.image_url)
        st.subheader("Ingredients")
        for ing in recipe.ingredients:
            st.write(f"- {ing.name}")
        st.subheader("Instructions")
        st.write(recipe.instructions)
