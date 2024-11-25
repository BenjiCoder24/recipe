# recipe App from Benji Mager

Summary:
I built an app that uses the python Streamlit library to generate a recipe search website. When the user inputs ingredients then they are captured in a Recipe class object. Then the user presses Find Recipe button then the Recipe object content will be passed as an API call to https://api.spoonacular.com. The result of this request will be displayed in the below section but I’m still working on this section.

![image](https://github.com/user-attachments/assets/2fb92485-7178-478e-a74b-8430e5df4070)


Project Overview 

I used a tool called Streamlit that allows me to create a webpage in python without the need of coding HTML code. 

I tried encapsulating the logic and data in class objects following the object-oriented pattern. A good example is the ingredient.py and recipe.py. All object class definition files are in the “src” directory. 

The main program is the class app.py. This class get the various API keys that are needed for access external systems and, most importantly, builds the HTML output page by creating an AppUI class object and triggers the generation to of the code app_ui.run()
 
# Initialize and run the app UI
app_ui = AppUI(api_client, user_session) #create AppUI Object
app_ui.run() #trigger HTML generation

The complete HTML output page is defined in the display_recipe_details method in the app_ui.py class in the src directory.

class AppUI:
   def __init__(self, api_client, user_session): # constructor
       self.api_client = api_client
       self.user_session = user_session


   def run(self): #run method that is called from the App class to generate the HTML page
       st.title("Recipe Suggestion App")
       self.display_ingredient_input()
       if st.button("Find Recipes"):
           self.find_and_display_recipes()



def display_recipe_details(self, recipe): #generates html page
       st.header(recipe.title)
       st.image(recipe.image_url)
       st.subheader("Ingredients")
       for ing in recipe.ingredients:
           st.write(f"- {ing.name}")
       st.subheader("Instructions")
       st.write(recipe.instructions)

When a button is pressed or an input is processed, then the other methods in the app_ui.py class are called to process them 



   def display_ingredient_input(self):
       ingredient_input = st.text_input("Enter an ingredient:")
       if st.button("Add Ingredient"):
           self.user_session.add_ingredient(ingredient_input)
       st.write("Your Ingredients:")
       for ing in self.user_session.ingredients:
           st.write(f"- {ing.name}")


 

The program is started with the command line



API call to retrieve recipe data

The class RecipeAPIClient is used to connect to the https://api.spoonacular.com and return it as a json for the website to display.

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



Open items:
I’m still working on the recipe API integration, the the Recipies button is currently not working.
I also have an issue with the python environment after my MacOs was upgraded. I think I will have this fixed later today.
