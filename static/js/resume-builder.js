/**
 * Resume Builder Page JavaScript
 * Handles form interactions and resume preview functionality
 */

document.addEventListener('DOMContentLoaded', function() {
    console.log('Resume builder page loaded');
    
    initializeResumeBuilder();
});

/**
 * Initialize resume builder functionality
 */
function initializeResumeBuilder() {
    const form = document.querySelector('form');
    const inputs = form.querySelectorAll('input, textarea');
    const previewSection = document.querySelector('.border.border-gray-200');
    
    // Add real-time preview updates
    inputs.forEach(input => {
        input.addEventListener('input', function() {
            updateResumePreview();
        });
    });
    
    // Handle "Add Another Experience" button
    const addExperienceBtn = document.querySelector('button[type="button"]');
    if (addExperienceBtn && addExperienceBtn.textContent.includes('Add Another Experience')) {
        addExperienceBtn.addEventListener('click', function() {
            addExperienceSection();
        });
    }
    
    // Handle form submission
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        generateResume();
    });
    
    // Handle "Save Draft" button
    const saveDraftBtn = document.querySelector('button:contains("Save Draft")');
    if (saveDraftBtn) {
        saveDraftBtn.addEventListener('click', function() {
            saveDraft();
        });
    }
}

/**
 * Update the resume preview with form data
 */
function updateResumePreview() {
    const form = document.querySelector('form');
    const previewSection = document.querySelector('.border.border-gray-200');
    
    if (!form || !previewSection) return;
    
    // Get form data
    const formData = new FormData(form);
    const data = {};
    for (let [key, value] of formData.entries()) {
        data[key] = value;
    }
    
    // Update preview sections
    updatePreviewSection('name', data.name || 'Your Name', '.text-2xl.font-bold');
    updatePreviewSection('title', data.title || 'Software Engineer', '.text-gray-600');
    updatePreviewSection('email', data.email || 'email@example.com', '.text-sm.text-gray-500');
    updatePreviewSection('phone', data.phone || '(555) 123-4567', '.text-sm.text-gray-500');
    updatePreviewSection('location', data.location || 'San Francisco, CA', '.text-sm.text-gray-500');
    updatePreviewSection('summary', data.summary || 'Your professional summary will appear here...', '.text-gray-700.text-sm');
    updatePreviewSection('skills', data.skills || 'Your skills will appear here...', '.text-sm.text-gray-700:last-child');
}

/**
 * Update a specific section in the preview
 * @param {string} fieldName - Form field name
 * @param {string} value - Value to display
 * @param {string} selector - CSS selector for the preview element
 */
function updatePreviewSection(fieldName, value, selector) {
    const element = document.querySelector(selector);
    if (element) {
        if (fieldName === 'contact') {
            // Handle contact information (email, phone, location)
            const contactInfo = [];
            if (value.email) contactInfo.push(value.email);
            if (value.phone) contactInfo.push(value.phone);
            if (value.location) contactInfo.push(value.location);
            element.textContent = contactInfo.join(' | ');
        } else {
            element.textContent = value;
        }
    }
}

/**
 * Add a new experience section to the form
 */
function addExperienceSection() {
    const experienceContainer = document.querySelector('.space-y-4');
    if (!experienceContainer) return;
    
    const newExperience = document.createElement('div');
    newExperience.className = 'border border-gray-200 rounded-lg p-4 space-y-4';
    newExperience.innerHTML = `
        <div class="flex justify-between items-center">
            <h4 class="font-medium">Work Experience</h4>
            <button type="button" class="text-red-500 hover:text-red-700" onclick="removeExperience(this)">
                <i data-lucide="trash-2" class="w-4 h-4"></i>
            </button>
        </div>
        <div class="grid md:grid-cols-2 gap-4">
            <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Job Title</label>
                <input type="text" name="job_title[]" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent" />
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Company</label>
                <input type="text" name="company[]" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent" />
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Start Date</label>
                <input type="month" name="start_date[]" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent" />
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">End Date</label>
                <input type="month" name="end_date[]" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent" />
            </div>
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Description</label>
            <textarea name="job_description[]" rows="3" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent"></textarea>
        </div>
    `;
    
    experienceContainer.appendChild(newExperience);
    
    // Initialize Lucide icons for the new section
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }
}

/**
 * Remove an experience section
 * @param {HTMLElement} button - The remove button element
 */
function removeExperience(button) {
    const experienceSection = button.closest('.border.border-gray-200');
    if (experienceSection) {
        experienceSection.remove();
    }
}

/**
 * Generate the final resume
 */
function generateResume() {
    const form = document.querySelector('form');
    if (!form) return;
    
    // Show loading state
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;
    submitBtn.textContent = 'Generating...';
    submitBtn.disabled = true;
    
    // Collect form data
    const formData = new FormData(form);
    
    // Simulate resume generation (in a real app, this would send to backend)
    setTimeout(() => {
        // Create download link
        const resumeData = {
            name: formData.get('name') || 'Your Name',
            title: formData.get('title') || 'Software Engineer',
            email: formData.get('email') || 'email@example.com',
            phone: formData.get('phone') || '(555) 123-4567',
            location: formData.get('location') || 'San Francisco, CA',
            summary: formData.get('summary') || 'Professional summary...',
            skills: formData.get('skills') || 'Skills...'
        };
        
        // Create and download PDF (simplified - in real app, use a PDF library)
        downloadResume(resumeData);
        
        // Reset button
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
        
        showToast('Success!', 'Your resume has been generated successfully!', 'success');
    }, 2000);
}

/**
 * Download the generated resume
 * @param {Object} resumeData - Resume data object
 */
function downloadResume(resumeData) {
    // Create a simple text version for demo
    const resumeText = `
RESUME

${resumeData.name}
${resumeData.title}
${resumeData.email} | ${resumeData.phone} | ${resumeData.location}

PROFESSIONAL SUMMARY
${resumeData.summary}

SKILLS
${resumeData.skills}
    `;
    
    // Create download link
    const blob = new Blob([resumeText], { type: 'text/plain' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${resumeData.name.replace(/\s+/g, '_')}_resume.txt`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
}

/**
 * Save current form data as draft
 */
function saveDraft() {
    const form = document.querySelector('form');
    if (!form) return;
    
    const formData = new FormData(form);
    const draftData = {};
    
    for (let [key, value] of formData.entries()) {
        draftData[key] = value;
    }
    
    // Save to localStorage (in a real app, this would save to backend)
    localStorage.setItem('resume_draft', JSON.stringify(draftData));
    
    showToast('Draft Saved', 'Your resume draft has been saved successfully!', 'success');
}

/**
 * Load saved draft
 */
function loadDraft() {
    const draftData = localStorage.getItem('resume_draft');
    if (!draftData) return;
    
    const data = JSON.parse(draftData);
    const form = document.querySelector('form');
    
    if (!form) return;
    
    // Populate form fields
    Object.keys(data).forEach(key => {
        const field = form.querySelector(`[name="${key}"]`);
        if (field) {
            field.value = data[key];
        }
    });
    
    // Update preview
    updateResumePreview();
    
    showToast('Draft Loaded', 'Your saved draft has been loaded!', 'info');
} 