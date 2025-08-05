from flask import Flask
import os
from dotenv import load_dotenv
from config import EMAIL_CONFIG

def create_app():
    """Application factory pattern for creating Flask app"""
    # Load environment variables from .env file
    load_dotenv()
    
    # Get the root directory (where templates and static folders are located)
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    app = Flask(__name__, 
                template_folder=os.path.join(root_dir, 'templates'),
                static_folder=os.path.join(root_dir, 'static'))
    app.secret_key = 'your-secret-key-here'  # Change this in production
    
    # Configuration
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}
    
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    
    # Ensure upload folder exists
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    
    # Register blueprints
    from app.routes import main_bp, api_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)
    
    return app 