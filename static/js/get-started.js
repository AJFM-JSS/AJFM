/**
 * Get Started Page JavaScript
 * Handles form submission and file upload functionality
 */

document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded, setting up form handlers');
    
    const form = document.getElementById('schedule-form');
    const fileInput = document.getElementById('resume');
    const uploadIcon = document.getElementById('upload-icon');
    const uploadText = document.getElementById('upload-text');
    
    console.log('Form element:', form);
    console.log('Form ID:', form ? form.id : 'No form');
    console.log('Form action:', form ? form.action : 'No form');
    console.log('Form method:', form ? form.method : 'No form');
    console.log('File input element:', fileInput);
    console.log('File input ID:', fileInput ? fileInput.id : 'No file input');

    // Handle file upload display
    fileInput.addEventListener('change', function(e) {
        console.log('=== FILE INPUT CHANGE ===');
        console.log('Event:', e);
        console.log('Files:', e.target.files);
        
        const file = e.target.files[0];
        if (file) {
            console.log('File selected:', file.name);
            console.log('File size:', file.size);
            console.log('File type:', file.type);
            uploadText.textContent = file.name;
            uploadIcon.style.display = 'none';
        } else {
            console.log('No file selected');
            uploadText.textContent = 'Click to upload your resume (PDF, DOC, DOCX)';
            uploadIcon.style.display = 'block';
        }
    });

    // Handle form submission
    try {
        // Also add click handler to button for debugging
        const submitButton = form.querySelector('button[type="submit"]');
        console.log('Submit button found:', submitButton);
        
        submitButton.addEventListener('click', function(e) {
            console.log('=== SUBMIT BUTTON CLICKED ===');
            console.log('Event:', e);
            console.log('Button element:', this);
            console.log('Button text:', this.textContent);
            console.log('Button type:', this.type);
            console.log('Button form:', this.form);
            console.log('Form valid:', this.form ? this.form.checkValidity() : 'No form');
            
            // Prevent default button behavior
            e.preventDefault();
            e.stopPropagation();
            
            // Handle form submission directly here
            console.log('Handling form submission directly from button click...');
            handleFormSubmission();
        });
        
        form.addEventListener('submit', function(e) {
            console.log('=== FORM SUBMIT EVENT TRIGGERED ===');
            console.log('Event:', e);
            console.log('Event type:', e.type);
            console.log('Event target:', e.target);
            console.log('Form element:', this);
            console.log('Form action:', this.action);
            console.log('Form method:', this.method);
            console.log('Form valid:', this.checkValidity());
            console.log('Form elements count:', this.elements.length);
            
            e.preventDefault();
            console.log('Form submission started');
            
            // Handle form submission
            handleFormSubmission();
        });
        
        // Function to handle form submission
        function handleFormSubmission() {
            console.log('=== HANDLE FORM SUBMISSION FUNCTION ===');
            
            const email = document.getElementById('email').value;
            const resume = fileInput.files[0];
            
            console.log('=== FORM DATA COLLECTION ===');
            console.log('Email field value:', email);
            console.log('Email field element:', document.getElementById('email'));
            console.log('Resume file:', resume);
            console.log('Resume file name:', resume ? resume.name : 'No file');
            console.log('Resume file size:', resume ? resume.size : 'No file');
            console.log('Resume file type:', resume ? resume.type : 'No file');
            
            if (!email) {
                console.log('=== VALIDATION ERROR: EMAIL ===');
                console.log('Email is empty or invalid');
                showToast('Email Required', 'Please provide your email address to continue.', 'error');
                return;
            }
            
            if (!resume) {
                console.log('=== VALIDATION ERROR: RESUME ===');
                console.log('No resume file selected');
                showToast('Resume Required', 'Please upload your resume to continue.', 'error');
                return;
            }
            
            // Create FormData for file upload
            const formData = new FormData();
            formData.append('email', email);
            formData.append('resume', resume);
            
            console.log('=== FORM DATA PREPARATION ===');
            console.log('FormData created:', formData);
            console.log('FormData entries:');
            for (let [key, value] of formData.entries()) {
                console.log(`  ${key}:`, value);
            }
            console.log('Submitting to /upload-resume...');
            
            // Submit to Flask backend using upload-resume route
            console.log('=== FETCH REQUEST STARTING ===');
            console.log('URL:', '/upload-resume');
            console.log('Method:', 'POST');
            console.log('Body type:', 'FormData');
            
            fetch('/upload-resume', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                console.log('=== FETCH RESPONSE RECEIVED ===');
                console.log('Response status:', response.status);
                console.log('Response status text:', response.statusText);
                console.log('Response headers:', response.headers);
                console.log('Response ok:', response.ok);
                return response.json();
            })
            .then(data => {
                console.log('=== RESPONSE DATA PARSED ===');
                console.log('Response data:', data);
                if (data.success) {
                    console.log('=== SUCCESS HANDLING ===');
                    console.log('Success flag is true');
                    showToast('Success!', 'Your resume has been submitted successfully! We will contact you within 24 hours.', 'success');
                    // Open scheduling link in new tab immediately
                    console.log('Opening scheduling link in new tab...');
                    window.open('https://zcal.co/jobsimplified/30min', '_blank');
                    console.log('Scheduling link opened');
                } else {
                    console.log('=== ERROR HANDLING ===');
                    console.log('Success flag is false');
                    console.log('Error message:', data.error);
                    showToast('Error', data.error, 'error');
                }
            })
            .catch(error => {
                console.log('=== FETCH ERROR ===');
                console.error('Fetch error:', error);
                console.error('Error name:', error.name);
                console.error('Error message:', error.message);
                console.error('Error stack:', error.stack);
                showToast('Error', 'Something went wrong. Please try again.', 'error');
            });
        }
    } catch (error) {
        console.log('=== SETUP ERROR ===');
        console.error('Error setting up form submission:', error);
        console.error('Error name:', error.name);
        console.error('Error message:', error.message);
        console.error('Error stack:', error.stack);
    }
});

/**
 * Show toast notification
 * @param {string} title - Toast title
 * @param {string} message - Toast message
 * @param {string} type - Toast type (success, error, info)
 */
function showToast(title, message, type = 'info') {
    const container = document.getElementById('toast-container');
    const toast = document.createElement('div');
    
    const bgColor = type === 'error' ? 'bg-red-500' : type === 'success' ? 'bg-green-500' : 'bg-blue-500';
    
    toast.className = `${bgColor} text-white px-4 py-3 rounded-lg shadow-lg mb-2 max-w-sm`;
    toast.innerHTML = `
        <div class="font-semibold">${title}</div>
        <div class="text-sm opacity-90">${message}</div>
    `;
    
    container.appendChild(toast);
    
    // Remove toast after 5 seconds
    setTimeout(() => {
        toast.remove();
    }, 5000);
} 