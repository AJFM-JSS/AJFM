# Apply Boost Studio

A modern resume builder and job application service built with Flask, serving a beautiful frontend with all the functionality of the original React application.

## Features

- **Modern Web Application**: Built with Flask backend and responsive HTML/CSS/JS frontend
- **Resume Upload & Processing**: Secure file upload with validation
- **Professional UI**: Beautiful, responsive design using Tailwind CSS
- **Interactive Forms**: Real-time validation and user feedback
- **API Endpoints**: RESTful API for testimonials and file uploads
- **Mobile Responsive**: Works perfectly on all devices

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Tailwind CSS
- **Icons**: Lucide Icons
- **File Handling**: Werkzeug

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

Follow these steps to run the project locally:

```sh
# Step 1: Clone the repository
git clone <YOUR_GIT_URL>

# Step 2: Navigate to the project directory
cd apply-boost-studio

# Step 3: Create a virtual environment
python3 -m venv venv

# Step 4: Activate the virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Step 5: Install dependencies
pip install -r requirements.txt

# Step 6: Start the development server
python app.py
```

The development server will start and provide an instant preview of your application at `http://localhost:5001`.

## Available Scripts

- `python app.py` - Start the Flask development server
- `pip install -r requirements.txt` - Install Python dependencies

## Project Structure

```
apply-boost-studio/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── home.html         # Home page
│   ├── get_started.html  # Get Started page
│   ├── login.html        # Login page
│   ├── profile.html      # Profile page
│   └── resume_builder.html # Resume builder page
├── static/               # Static files
│   ├── css/
│   │   └── style.css     # Custom styles
│   ├── js/
│   │   └── main.js       # Main JavaScript
│   └── images/           # Image assets
└── uploads/              # Uploaded files (created automatically)
```

## Available Routes

- `/` - Home page with hero section, features, pricing, and testimonials
- `/get-started` - Get Started page with resume upload form
- `/login` - Login page
- `/profile` - User profile page
- `/resume-builder` - Resume builder tool
- `/upload-resume` - API endpoint for resume uploads (POST)
- `/schedule-consultation` - API endpoint for consultation scheduling (POST)
- `/api/testimonials` - API endpoint for testimonials (GET)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Deployment

For production deployment, consider using:
- Gunicorn or uWSGI as WSGI server
- Nginx as reverse proxy
- Environment variables for configuration
- Database for user management (SQLAlchemy)

Example with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```
