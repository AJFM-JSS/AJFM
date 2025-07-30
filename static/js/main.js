/**
 * Main JavaScript file for Apply Boost Studio
 * Handles global initialization and common functionality
 */

document.addEventListener('DOMContentLoaded', function() {
    console.log('Main JavaScript loaded');
    
    // Initialize Lucide icons
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }

    // Initialize global interactive elements
    initializeGlobalElements();
    
    // Handle mobile navigation
    initializeMobileNavigation();
    
    // Handle global form validations
    initializeGlobalFormValidations();
});

function initializeGlobalElements() {
    // Add hover effects to cards globally
    const cards = document.querySelectorAll('.shadow-card-custom');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.classList.add('shadow-card-hover');
        });
        
        card.addEventListener('mouseleave', function() {
            this.classList.remove('shadow-card-hover');
        });
    });

    // Add loading states to submit buttons globally
    const submitButtons = document.querySelectorAll('button[type="submit"]');
    submitButtons.forEach(button => {
        button.addEventListener('click', function() {
            if (this.form && this.form.checkValidity()) {
                this.classList.add('loading');
                this.disabled = true;
            }
        });
    });
}

function initializeMobileNavigation() {
    // Mobile menu toggle (if needed)
    const mobileMenuButton = document.querySelector('[data-mobile-menu]');
    const mobileMenu = document.querySelector('[data-mobile-menu-items]');
    
    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
        });
    }
}

function initializeGlobalFormValidations() {
    // Real-time form validation for all forms
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input, textarea, select');
        
        inputs.forEach(input => {
            input.addEventListener('blur', function() {
                validateField(this);
            });
            
            input.addEventListener('input', function() {
                clearFieldError(this);
            });
        });
    });
}

function validateField(field) {
    const value = field.value.trim();
    const type = field.type;
    const required = field.hasAttribute('required');
    
    // Clear previous errors
    clearFieldError(field);
    
    // Check if required field is empty
    if (required && !value) {
        showFieldError(field, 'This field is required');
        return false;
    }
    
    // Email validation
    if (type === 'email' && value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            showFieldError(field, 'Please enter a valid email address');
            return false;
        }
    }
    
    // Phone validation
    if (type === 'tel' && value) {
        const phoneRegex = /^[\+]?[1-9][\d]{0,15}$/;
        if (!phoneRegex.test(value.replace(/[\s\-\(\)]/g, ''))) {
            showFieldError(field, 'Please enter a valid phone number');
            return false;
        }
    }
    
    return true;
}

// Note: Utility functions are now in utils.js
// showToast, validateEmail, validatePhone, showFieldError, clearFieldError, 
// formatPhoneNumber, and handleFileUpload are available from utils.js

// Export functions for use in other scripts
window.ApplyBoostStudio = {
    showToast,
    formatPhoneNumber,
    handleFileUpload,
    validateField
}; 