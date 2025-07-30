from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash, current_app
from werkzeug.utils import secure_filename
from datetime import datetime
import os
from app.utils import allowed_file, send_consultation_email, send_confirmation_email

# Create blueprints
main_bp = Blueprint('main', __name__)
api_bp = Blueprint('api', __name__, url_prefix='/api')

# Main routes
@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/get-started')
def get_started():
    return render_template('get_started.html')

@main_bp.route('/login')
def login():
    return render_template('login.html')

@main_bp.route('/profile')
def profile():
    return render_template('profile.html')

@main_bp.route('/resume-builder')
def resume_builder():
    return render_template('resume_builder.html')

@main_bp.route('/upload-resume', methods=['POST'])
def upload_resume():
    print("=== UPLOAD RESUME ROUTE HIT ===")
    print(f"Request method: {request.method}")
    print(f"Request files: {list(request.files.keys())}")
    print(f"Request form data: {dict(request.form)}")
    
    if 'resume' not in request.files:
        print("No resume file in request")
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['resume']
    email = request.form.get('email')
    
    if not email:
        return jsonify({'error': 'Email is required'}), 400
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    print(f"File: {file.filename}")
    print(f"Email: {email}")
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Send consultation email to admin
        admin_email_sent = send_consultation_email(email, filename, file_path)
        
        # Send confirmation email to user
        user_email_sent = send_confirmation_email(email, filename)
        
        # Process Google Drive upload and notification asynchronously
        try:
            import asyncio
            from app.google_drive_utils import process_resume_upload
            
            # Run async Google Drive operations
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
            drive_result = loop.run_until_complete(
                process_resume_upload(file_path, filename, email)
            )
            
            loop.close()
            
            print(f"Google Drive result: {drive_result}")
            
        except Exception as e:
            print(f"Google Drive processing error: {e}")
            drive_result = {
                'success': False,
                'error': str(e)
            }
        
        # Log the submission (in production, save to database)
        submission_log = {
            'email': email,
            'resume_filename': filename,
            'submitted_at': datetime.now().isoformat(),
            'admin_email_sent': admin_email_sent,
            'user_email_sent': user_email_sent,
            'drive_upload_success': drive_result.get('success', False),
            'drive_file_id': drive_result.get('drive_upload', {}).get('file_id'),
            'drive_web_link': drive_result.get('drive_upload', {}).get('web_view_link'),
            'notification_sent': drive_result.get('notification_sent', False)
        }
        
        print(f"New consultation request: {submission_log}")
        print("=== SUCCESS: Returning success response ===")
        
        return jsonify({
            'success': True,
            'message': f'Consultation request submitted successfully! We have received your resume and will contact you within 24 hours.',
            'redirect_url': 'https://zcal.co/jobsimplified/30min',
            'email_sent': user_email_sent,
            'drive_upload': drive_result.get('success', False),
            'drive_link': drive_result.get('drive_upload', {}).get('web_view_link')
        })
    
    print("=== ERROR: Invalid file type ===")
    return jsonify({'error': 'Invalid file type. Please upload PDF, DOC, or DOCX files only.'}), 400

@main_bp.route('/schedule-consultation', methods=['POST'])
def schedule_consultation():
    """
    Handle consultation scheduling with email and resume
    """
    if 'resume' not in request.files:
        return jsonify({'error': 'No resume file provided'}), 400
    
    file = request.files['resume']
    email = request.form.get('email')
    
    if not email:
        return jsonify({'error': 'Email is required'}), 400
    
    if file.filename == '':
        return jsonify({'error': 'No resume file selected'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Send consultation email to admin with resume attachment
        admin_email_sent = send_consultation_email(email, filename, file_path)
        
        # Send confirmation email to user
        user_email_sent = send_confirmation_email(email, filename)
        
        # Log the consultation request
        consultation_log = {
            'email': email,
            'resume_filename': filename,
            'submitted_at': datetime.now().isoformat(),
            'admin_email_sent': admin_email_sent,
            'user_email_sent': user_email_sent,
            'action': 'consultation_scheduled'
        }
        
        print(f"Consultation scheduled: {consultation_log}")
        
        return jsonify({
            'success': True,
            'message': 'Your consultation has been scheduled! Check your email for confirmation.',
            'redirect_url': 'https://zcal.co/jobsimplified/30min',
            'email_sent': user_email_sent,
            'consultation_id': f"CONS_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        })
    
    return jsonify({'error': 'Invalid file type. Please upload PDF, DOC, or DOCX files only.'}), 400

# API routes
@api_bp.route('/testimonials')
def get_testimonials():
    testimonials = [
        {
            "name": "Sarah Johnson",
            "role": "Software Engineer",
            "content": "After months of job hunting with no success, AJFM changed everything. Within 3 weeks, I had 4 interview requests and landed a position that exceeded my salary expectations.",
            "rating": 5,
            "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=400&h=400&fit=crop&crop=face"
        },
        {
            "name": "Michael Chen",
            "role": "Marketing Manager", 
            "content": "AJFM saved me countless hours of searching and applying. Their team found opportunities I hadn't discovered and handled all the application details perfectly.",
            "rating": 5,
            "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop&crop=face"
        },
        {
            "name": "Emily Rodriguez",
            "role": "Product Manager",
            "content": "As a busy parent, I didn't have time to apply for jobs effectively. AJFM understood my goals and secured multiple interviews within a month.",
            "rating": 5,
            "image": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=400&h=400&fit=crop&crop=face"
        }
    ]
    return jsonify(testimonials) 