import os
import sys

# Add root directory to sys.path so 'app' can be imported in Vercel Serverless environment
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from app.main import app

# Vercel looks for 'app' as the WSGI application callable
if __name__ == "__main__":
    app.run()

