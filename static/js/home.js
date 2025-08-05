/**
 * Home Page JavaScript
 * Handles testimonials loading and interactive elements
 */

document.addEventListener('DOMContentLoaded', function() {
    // Load testimonials
    loadTestimonials();
    
    // Initialize Lucide icons
    if (window.lucide) {
        window.lucide.createIcons();
    }
});

async function loadTestimonials() {
    try {
        const response = await fetch('/api/testimonials');
        const testimonials = await response.json();
        
        const container = document.getElementById('testimonials-container');
        if (!container) return;
        
        container.innerHTML = testimonials.map(testimonial => `
            <div class="bg-white rounded-lg p-6 shadow-card-custom hover:shadow-card-hover transition-shadow-smooth">
                <div class="flex items-center mb-4">
                    <div class="flex text-yellow-400">
                        ${'★'.repeat(testimonial.rating)}${'☆'.repeat(5 - testimonial.rating)}
                    </div>
                </div>
                <p class="text-gray-700 mb-4 italic">"${testimonial.content}"</p>
                <div class="border-t border-gray-200 pt-4">
                    <div class="font-semibold text-gray-900">${testimonial.name}</div>
                    <div class="text-sm text-gray-600">${testimonial.role} at ${testimonial.company}</div>
                </div>
            </div>
        `).join('');
        
    } catch (error) {
        console.error('Error loading testimonials:', error);
    }
}

/**
 * Initialize interactive elements on the home page
 */
function initializeInteractiveElements() {
    // Add hover effects to cards
    const cards = document.querySelectorAll('.shadow-card-custom');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.classList.add('shadow-card-hover');
        });
        
        card.addEventListener('mouseleave', function() {
            this.classList.remove('shadow-card-hover');
        });
    });

    // Add smooth scrolling to anchor links
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add loading states to CTA buttons
    const ctaButtons = document.querySelectorAll('.bg-primary, .border-white');
    ctaButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Add loading state
            const originalText = this.textContent;
            this.textContent = 'Loading...';
            this.disabled = true;
            
            // Reset after a short delay (simulating loading)
            setTimeout(() => {
                this.textContent = originalText;
                this.disabled = false;
            }, 1000);
        });
    });
} 