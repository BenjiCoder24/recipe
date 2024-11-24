# Import required libraries
import streamlit as st
import os
from dotenv import load_dotenv

# Import your custom classes
from src.app_ui import AppUI
from src.recipe_api_client import RecipeAPIClient
from src.user_session import UserSession

# Load environment variables from a .env file
load_dotenv()

# Retrieve API keys from the environment variables
# These are used for secure access to the Streamlit license and recipe API
STREAMLIT_LICENSE_KEY = os.getenv('STREAMLIT_LICENSE_KEY')
RECIPE_API_KEY = os.getenv('RECIPE_API_KEY')  # Ensure this key is stored in your .env file

# Use Streamlit's session_state to keep objects persistent between user interactions
# Initialize UserSession, RecipeAPIClient, and AppUI only once

# Check if the `user_session` object already exists in session_state
# If it doesn't, create a new instance and store it
if "user_session" not in st.session_state:
    st.session_state.user_session = UserSession()

# Check if the `api_client` object already exists in session_state
# If it doesn't, create a new instance with the Recipe API key and store it
if "api_client" not in st.session_state:
    st.session_state.api_client = RecipeAPIClient(api_key=RECIPE_API_KEY)

# Check if the `app_ui` object already exists in session_state
# If it doesn't, create a new instance of AppUI with the API client and user session
if "app_ui" not in st.session_state:
    st.session_state.app_ui = AppUI(st.session_state.api_client, st.session_state.user_session)

# Run the app UI using the persisted instance in session_state
# This ensures that the user's session (e.g., added ingredients) remains intact
st.session_state.app_ui.run()
