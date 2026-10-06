import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

# SQLite Database Location in dataset directory
DB_PATH = os.path.join(PROJECT_ROOT, "dataset", "skillbridge.sqlite")

# Application Settings
SECRET_KEY = os.environ.get("SECRET_KEY", "skillbridge-enterprise-secret-key-2026")
DEBUG = os.environ.get("FLASK_DEBUG", "True").lower() == "true"
PORT = int(os.environ.get("PORT", 5000))
