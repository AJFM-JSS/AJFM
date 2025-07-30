import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
from config import EMAIL_CONFIG

def allowed_file(filename):
    """Check if uploaded file has allowed extension"""
    ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def send_consultation_email(user_email, resume_filename, resume_path):
    """
    Send consultation scheduling email to admin with user details and resume attachment
    """
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_CONFIG['sender_email']
        msg['To'] = EMAIL_CONFIG['admin_email']
        msg['Subject'] = f'New Consultation Request - {user_email}'
        
        # Email body
        body = f"""
        New consultation request received!
        
        User Details:
        - Email: {user_email}
        - Resume: {resume_filename}
        - Submitted: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        
        Please schedule a consultation call with this user.
        Scheduling link: https://zcal.co/jobsimplified/30min
        
        Best regards,
        Apply Boost Studio System
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Attach resume file
        if os.path.exists(resume_path):
            with open(resume_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
            
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename= {resume_filename}'
            )
            msg.attach(part)
        
        # Send email
        server = smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
        server.starttls()
        server.login(EMAIL_CONFIG['sender_email'], EMAIL_CONFIG['sender_password'])
        text = msg.as_string()
        server.sendmail(EMAIL_CONFIG['sender_email'], EMAIL_CONFIG['admin_email'], text)
        server.quit()
        
        return True
    except Exception as e:
        print(f"Email sending failed: {str(e)}")
        return False

def send_confirmation_email(user_email, resume_filename):
    """
    Send confirmation email to user
    """
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_CONFIG['sender_email']
        msg['To'] = user_email
        msg['Subject'] = 'Consultation Request Received - Apply Boost Studio'
        
        body = f"""
        Thank you for your consultation request!
        
        We have received your resume ({resume_filename}) and will be in touch shortly to schedule your consultation call.
        
        Next Steps:
        1. Our team will review your resume
        2. We'll contact you within 24 hours to schedule your consultation
        3. During the call, we'll discuss your job search goals and how we can help
        
        You can also schedule your consultation directly here:
        https://zcal.co/jobsimplified/30min
        
        If you have any questions, please don't hesitate to reach out.
        
        Best regards,
        The Apply Boost Studio Team
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
        server.starttls()
        server.login(EMAIL_CONFIG['sender_email'], EMAIL_CONFIG['sender_password'])
        text = msg.as_string()
        server.sendmail(EMAIL_CONFIG['sender_email'], user_email, text)
        server.quit()
        
        return True
    except Exception as e:
        print(f"Confirmation email sending failed: {str(e)}")
        return False 