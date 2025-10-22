# config.py
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
class Settings:
    """Holds all configuration settings for the test framework."""

    # Core API Configuration
    BASE_API_URL: str = os.getenv("SPREE_BASE_URL", "https://demo.spreecommerce.org")

    # Authentication Tokens
    ADMIN_AUTH_TOKEN: str = os.getenv("ADMIN_AUTH_TOKEN")
    CUSTOMER_AUTH_TOKEN: str = os.getenv("CUSTOMER_AUTH_TOKEN")

    def __init__(self):
        # Ensure critical tokens are present
        if not self.ADMIN_AUTH_TOKEN:
            raise ValueError("ADMIN_AUTH_TOKEN not found in environment variables.")
        if not self.CUSTOMER_AUTH_TOKEN:
            print("Warning: CUSTOMER_AUTH_TOKEN not found. Some tests may fail.")


# Create a single settings instance to be imported across the project
settings = Settings()