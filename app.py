import streamlit as st
import os
from dotenv import load_dotenv

from src.app_ui import AppUI
from src.recipe_api_client import RecipeAPIClient
from src.user_session import UserSession

# Load environment variables
load_dotenv()

# Retrieve the API keys from environment variables
STREAMLIT_LICENSE_KEY = os.getenv('STREAMLIT_LICENSE_KEY')
RECIPE_API_KEY = os.getenv('RECIPE_API_KEY')  # Add this to your .env file if needed

# Initialize the API client and user session
api_client = RecipeAPIClient(api_key=RECIPE_API_KEY)
user_session = UserSession()

# Initialize and run the app UI
app_ui = AppUI(api_client, user_session)
app_ui.run()
