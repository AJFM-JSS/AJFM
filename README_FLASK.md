# Apply Boost Studio - Flask Version

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

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd apply-boost-studio
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your browser and go to `http://localhost:5000`

## Available Routes

- `/` - Home page with hero section, features, pricing, and testimonials
- `/get-started` - Get Started page with resume upload form
- `/login` - Login page
- `/profile` - User profile page
- `/resume-builder` - Resume builder tool
- `/upload-resume` - API endpoint for resume uploads (POST)
- `/api/testimonials` - API endpoint for testimonials (GET)

## Features in Detail

### Home Page (`/`)
- Hero section with call-to-action buttons
- How it works section with 4-step process
- Pricing plans with feature comparison
- Customer testimonials loaded via API
- Final CTA section

### Get Started Page (`/get-started`)
- Email collection form
- Resume upload with drag-and-drop interface
- Form validation (email required, resume required)
- Automatic redirect to scheduling after successful upload
- Toast notifications for user feedback

### Resume Builder (`/resume-builder`)
- Comprehensive resume creation form
- Real-time preview
- Professional formatting
- Export functionality

### File Upload System
- Secure file handling with Werkzeug
- File type validation (PDF, DOC, DOCX)
- File size limits
- Automatic file organization in uploads folder

## API Endpoints

### GET `/api/testimonials`
Returns JSON array of customer testimonials.

**Response:**
```json
[
  {
    "name": "Sarah Johnson",
    "role": "Software Engineer",
    "content": "After months of job hunting...",
    "rating": 5,
    "image": "https://images.unsplash.com/..."
  }
]
```

### POST `/upload-resume`
Handles resume file uploads.

**Request:**
- `email` (form field): User's email address
- `resume` (file): Resume file (PDF, DOC, DOCX)

**Response:**
```json
{
  "success": true,
  "message": "Resume filename.pdf uploaded successfully for user@example.com",
  "redirect_url": "https://zcal.co/jobsimplified/30min"
}
```

## Customization

### Styling
- Modify `static/css/style.css` for custom styles
- Update Tailwind configuration in `templates/base.html`
- Add new CSS classes as needed

### JavaScript
- Edit `static/js/main.js` for frontend functionality
- Add new interactive features
- Modify form validation logic

### Templates
- All HTML templates are in the `templates/` directory
- Use Jinja2 templating for dynamic content
- Extend `base.html` for consistent layout

## Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
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

## Security Considerations

- Change the secret key in `app.py` for production
- Implement proper user authentication
- Add CSRF protection for forms
- Use HTTPS in production
- Implement rate limiting for file uploads
- Add input sanitization

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support or questions, please contact the development team or create an issue in the repository. 