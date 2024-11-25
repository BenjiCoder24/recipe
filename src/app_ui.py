import streamlit as st
from src.recipe import Recipe

class AppUI:
    def __init__(self, api_client, user_session, data_manager):
        self.api_client = api_client
        self.user_session = user_session
        self.data_manager = data_manager

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
        st.subheader("Recipe Suggestions")
        for recipe in recipes:
            with st.expander(recipe.title):
                # Cache or fetch recipe details
                recipe_details = self.data_manager.get_cached_recipe(recipe.id)
                if not recipe_details:
                    recipe_details = self.api_client.get_recipe_details(recipe_id=recipe.id)
                    self.data_manager.cache_recipe(recipe.id, recipe_details)
                detailed_recipe = Recipe(recipe_details)
                self.display_recipe_details(detailed_recipe)

    def display_recipe_details(self, recipe):
        # Display the recipe image with updated parameter
        st.image(recipe.image_url, caption=recipe.title, use_container_width=True)
        st.subheader("Ingredients")
        for ing in recipe.ingredients:
            st.write(f"- {ing.name}")
        
        st.subheader("Instructions")
        if recipe.instructions:
            # Use st.markdown to render HTML in instructions
            st.markdown(recipe.instructions, unsafe_allow_html=True)
        else:
            st.write("No instructions available.")
        
        if recipe.source_url:
            st.markdown(f"[View Source Recipe]({recipe.source_url})", unsafe_allow_html=True)
