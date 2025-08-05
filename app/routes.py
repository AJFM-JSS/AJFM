from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from werkzeug.utils import secure_filename
import json

# Create blueprints
main_bp = Blueprint('main', __name__)
api_bp = Blueprint('api', __name__, url_prefix='/api')

@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/get-started')
def get_started():
    return render_template('get_started.html')

@main_bp.route('/resume-builder')
def resume_builder():
    return render_template('resume_builder.html')

@main_bp.route('/login')
def login():
    return render_template('login.html')

@main_bp.route('/profile')
def profile():
    return render_template('profile.html')

@api_bp.route('/submit-form', methods=['POST'])
def submit_form():
    try:
        print("=== SUBMIT FORM ROUTE HIT ===")
        
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone', '')
        
        print(f"Form data received: name={name}, email={email}, phone={phone}")
        
        # Handle file upload
        resume_file = request.files.get('resume')
        resume_filename = None
        file_path = None
        
        if resume_file and resume_file.filename:
            print(f"Resume file received: {resume_file.filename}")
            # Secure the filename
            resume_filename = secure_filename(resume_file.filename)
            
            # Save file to uploads directory
            upload_folder = 'uploads'
            os.makedirs(upload_folder, exist_ok=True)
            file_path = os.path.join(upload_folder, resume_filename)
            resume_file.save(file_path)
            print(f"Resume saved to: {file_path}")
        else:
            print("No resume file received")
        
        # Send email notification (commented out for now to avoid email errors)
        email_sent = send_notification_email(name, email, phone, resume_filename)
        print("Email notification sent")
        
        # Delete resume file after successful email
        if email_sent and file_path and os.path.exists(file_path):
            try:
                os.remove(file_path)
                print(f"✅ Resume file deleted: {file_path}")
            except Exception as e:
                print(f"❌ Error deleting resume file: {e}")
        
        return jsonify({
            'success': True,
            'message': 'Form submitted successfully! We\'ll be in touch soon.',
            'redirect_url': 'https://zcal.co/jobsimplified/30min'
        })
        
    except Exception as e:
        print(f"=== FORM SUBMISSION ERROR: {str(e)} ===")
        return jsonify({
            'success': False,
            'message': f'Error submitting form: {str(e)}'
        }), 500

def send_notification_email(name, email, phone, resume_filename):
    """Send email notification to applyjobsforme9876@gmail.com"""
    
    # Email configuration
    sender_email = os.environ.get('SENDER_EMAIL')  # Replace with your email
    sender_password = os.environ.get('SENDER_PASSWORD')  # Replace with your app password
    recipient_email = "applyjobsforme9876@gmail.com"
    print(f"Sender email: {sender_email}")
    print(f"Sender password: {sender_password}")
    
    # Check if email credentials are configured
    if not sender_email or not sender_password:
        print("⚠️  Email credentials not configured. Skipping email notification.")
        print("📧 To enable email notifications, set environment variables:")
        print("   SENDER_EMAIL=your-email@gmail.com")
        print("   SENDER_PASSWORD=your-app-password")
        return False
    
    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = "applyjobsforme9876@gmail.com"
    msg['Subject'] = f"New AJFM Lead: {name}"
    
    # Email body
    body = f"""
    New lead submitted through AJFM website:
    
    Name: {name}
    Email: {email}
    Phone: {phone if phone else 'Not provided'}
    
    Resume: {resume_filename if resume_filename else 'Not uploaded'}
    
    Please follow up with this potential client.
    """
    
    msg.attach(MIMEText(body, 'plain'))
    
    # Attach resume if uploaded
    if resume_filename:
        try:
            with open(f"uploads/{resume_filename}", "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
            
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename= {resume_filename}',
            )
            msg.attach(part)
            print(f"✅ Resume attached: {resume_filename}")
        except Exception as e:
            print(f"❌ Error attaching resume: {e}")
    
    # Send email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print("✅ Email sent successfully to", recipient_email)
        return True
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        print("💡 Make sure your Gmail app password is correct and 2FA is enabled")
        return False

@api_bp.route('/testimonials')
def get_testimonials():
    """Return testimonials data"""
    testimonials = [
        {
            "name": "Sarah",
            "role": "Software Engineer",
            "company": "Amazon",
            "content": "AJFM helped me land my dream job in just 4 weeks. The personalized approach made all the difference.",
            "rating": 5
        },
        {
            "name": "Arvind Swamy",
            "role": "Software Engineer III",
            "company": "Walmart",
            "content": "I was spending hours on applications with no results. AJFM turned that around completely.",
            "rating": 5
        },
        {
            "name": "Mansi",
            "role": "Product Manager",
            "company": "Oracle",
            "content": "The weekly updates and personalized applications helped me get multiple interviews. Highly recommended!",
            "rating": 5
        }
    ]
    return jsonify(testimonials) 