/**
 * Get Started Page JavaScript
 * Handles form submission and file upload functionality
 */

document.addEventListener('DOMContentLoaded', function() {
    console.log('Get Started page loaded');
    
    const form = document.getElementById('schedule-form');
    const fileInput = document.getElementById('resume');
    const uploadIcon = document.getElementById('upload-icon');
    const uploadText = document.getElementById('upload-text');
    const submitButton = form.querySelector('button[type="submit"]');

    if (!form) {
        console.error('Form not found');
        return;
    }

    console.log('Form found:', form);
    console.log('Submit button found:', submitButton);

    // File upload handling
    fileInput.addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (file) {
            console.log('File selected:', file.name);
            // Update upload area to show selected file
            uploadIcon.innerHTML = '<i data-lucide="file-text" class="w-8 h-8 text-primary-600"></i>';
            uploadText.textContent = `Selected: ${file.name}`;
            
            // Initialize Lucide icons for the new icon
            if (window.lucide) {
                window.lucide.createIcons();
            }
        }
    });

    // Direct click handler for submit button
    submitButton.addEventListener('click', function(e) {
        console.log('=== SUBMIT BUTTON CLICKED ===');
        e.preventDefault();
        
        // Check if form is valid
        if (!form.checkValidity()) {
            console.log('Form validation failed');
            form.reportValidity();
            return;
        }
        
        console.log('Form is valid, proceeding with submission');
        handleFormSubmission();
    });

    // Form submission handler (also triggered by form submit event)
    form.addEventListener('submit', function(e) {
        console.log('=== FORM SUBMIT EVENT TRIGGERED ===');
        e.preventDefault();
        handleFormSubmission();
    });

    // Function to handle form submission
    function handleFormSubmission() {
        console.log('Form submission started');
        
        const originalText = submitButton.innerHTML;
        
        console.log('Submit button found:', submitButton);
        console.log('Original button text:', originalText);
        
        // Show loading state
        submitButton.innerHTML = '<i data-lucide="loader-2" class="w-5 h-5 animate-spin"></i> Submitting...';
        submitButton.disabled = true;
        
        // Initialize Lucide icons for the loading spinner
        if (window.lucide) {
            window.lucide.createIcons();
        }

        // Create FormData object
        const formData = new FormData(form);
        
        // Log form data for debugging
        console.log('Form data:');
        for (let [key, value] of formData.entries()) {
            if (key === 'resume') {
                console.log(`${key}:`, value.name, value.size, value.type);
            } else {
                console.log(`${key}:`, value);
            }
        }

        console.log('Submitting to /api/submit-form...');

        // Submit form data
        fetch('/api/submit-form', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            console.log('Response received:', response.status, response.statusText);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Response data:', data);
            if (data.success) {
                // Show success message
                showToast('success', data.message);
                
                // Redirect to scheduling page after a short delay
                setTimeout(() => {
                    console.log('Redirecting to:', data.redirect_url);
                    window.location.href = data.redirect_url;
                }, 2000);
            } else {
                // Show error message
                showToast('error', data.message || 'An error occurred. Please try again.');
                
                // Reset button
                submitButton.innerHTML = originalText;
                submitButton.disabled = false;
            }
        })
        .catch(error => {
            console.error('Fetch error:', error);
            showToast('error', 'An error occurred. Please try again.');
            
            // Reset button
            submitButton.innerHTML = originalText;
            submitButton.disabled = false;
        });
    }

    // Toast notification function
    function showToast(type, message) {
        console.log('Showing toast:', type, message);
        const toastContainer = document.getElementById('toast-container');
        if (!toastContainer) {
            console.error('Toast container not found');
            return;
        }
        
        const toast = document.createElement('div');
        
        const bgColor = type === 'success' ? 'bg-green-500' : 'bg-red-500';
        const icon = type === 'success' ? 'check-circle' : 'x-circle';
        
        toast.className = `${bgColor} text-white px-6 py-4 rounded-lg shadow-lg mb-4 flex items-center gap-2`;
        toast.innerHTML = `
            <i data-lucide="${icon}" class="w-5 h-5"></i>
            <span>${message}</span>
        `;
        
        toastContainer.appendChild(toast);
        
        // Initialize Lucide icons
        if (window.lucide) {
            window.lucide.createIcons();
        }
        
        // Remove toast after 5 seconds
        setTimeout(() => {
            toast.remove();
        }, 5000);
    }

    // Initialize Lucide icons
    if (window.lucide) {
        window.lucide.createIcons();
    }
}); 