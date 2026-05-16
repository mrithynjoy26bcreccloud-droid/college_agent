import os
import sys

# Add the backend directory to sys.path so we can import 'app'
backend_path = os.path.join(os.path.dirname(__file__), "..", "backend")
sys.path.append(backend_path)

from app.main import app

# Vercel needs the app object to be named 'app'
# This is already handled by 'from app.main import app'
