# Recipe App by Benji Mager

## Summary
I built an app using the Python **Streamlit** library to generate a recipe search website. Users can input ingredients, which are captured in a `Recipe` class object. When the **Find Recipes** button is pressed, the contents of the `Recipe` object are sent as an API call to [Spoonacular](https://api.spoonacular.com). The results of the request are displayed on the page.

I have hosted this application on Streamlit Community Cloud, and it can be accessed at **[benjamin.streamlit.app](https://benjamin.streamlit.app)**.

![Recipe App Screenshot](https://github.com/user-attachments/assets/2fb92485-7178-478e-a74b-8430e5df4070)

---

## Project Overview

### Streamlit
I used **Streamlit**, a Python framework that allows me to create webpages without writing HTML code.

### Object-Oriented Design
The app follows an object-oriented design pattern:
- Logic and data are encapsulated in class objects.
- Examples include `ingredient.py` and `recipe.py`.
- All class definition files are stored in the `src` directory.

### Main Program
The main program is `app.py`, which:
1. Retrieves various API keys for accessing external systems.
2. Builds the HTML output by creating an `AppUI` object.
3. Triggers the UI generation with:

```python
# Initialize and run the app UI
app_ui = AppUI(api_client, user_session)  # Create AppUI object
app_ui.run()  # Trigger HTML generation
```

### HTML Output
The entire HTML output page is defined in the `display_recipe_details` method within the `AppUI` class (`app_ui.py` in the `src` directory):

```python
class AppUI:
    def __init__(self, api_client, user_session):  # Constructor
        self.api_client = api_client
        self.user_session = user_session

    def run(self):  # Generates the HTML page
        st.title("Recipe Suggestion App")
        self.display_ingredient_input()
        if st.button("Find Recipes"):
            self.find_and_display_recipes()

    def display_recipe_details(self, recipe):  # Generates recipe details page
        st.header(recipe.title)
        st.image(recipe.image_url, use_container_width=True)
        st.subheader("Ingredients")
        for ing in recipe.ingredients:
            st.write(f"- {ing.name}")
        st.subheader("Instructions")
        st.markdown(recipe.instructions, unsafe_allow_html=True)
```

When a button is pressed or an input is processed, supporting methods in `app_ui.py` handle the interactions. For example:

```python
def display_ingredient_input(self):
    ingredient_input = st.text_input("Enter an ingredient:")
    if st.button("Add Ingredient"):
        self.user_session.add_ingredient(ingredient_input)
    st.write("Your Ingredients:")
    for ing in self.user_session.ingredients:
        st.write(f"- {ing.name}")
```

---

## How to Run the Program

Run the app with the following command in your terminal:
```bash
streamlit run app.py
```

Alternatively, access the hosted version at **[benjamin.streamlit.app](https://benjamin.streamlit.app)**.

---

## API Integration
The `RecipeAPIClient` class is responsible for connecting to the [Spoonacular API](https://api.spoonacular.com) and returning recipe data in JSON format. Here's a snippet:

```python
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
        return response.json()

    def get_recipe_details(self, recipe_id):
        endpoint = f'{self.base_url}/recipes/{recipe_id}/information'
        params = {'apiKey': self.api_key}
        response = requests.get(endpoint, params=params)
        return response.json()
```

---

## Open Items
1. **Recipe API Integration**:
   - The **Find Recipes** button is functional, but I'm still working on fine-tuning the integration with the Spoonacular API.
2. **Python Environment Issues**:
   - I encountered issues after upgrading macOS, which disrupted my Python environment. I plan to resolve this today.

---

Thank you for exploring my Recipe App project!

