/**
 * Home Page JavaScript
 * Handles testimonials loading and interactive elements
 */

document.addEventListener('DOMContentLoaded', function() {
    console.log('Home page loaded, initializing components');
    
    // Load testimonials from API
    loadTestimonials();
    
    // Initialize interactive elements
    initializeInteractiveElements();
});

/**
 * Load testimonials from API and display them
 */
function loadTestimonials() {
    fetch('/api/testimonials')
        .then(response => response.json())
        .then(testimonials => {
            const container = document.getElementById('testimonials-container');
            if (!container) {
                console.warn('Testimonials container not found');
                return;
            }
            
            testimonials.forEach(testimonial => {
                const testimonialHtml = `
                    <div class="bg-background shadow-card-custom hover:shadow-elegant transition-all duration-300 rounded-lg p-6">
                        <div class="flex items-center mb-4">
                            ${Array(testimonial.rating).fill().map(() => '<i data-lucide="star" class="w-5 h-5 text-yellow-500 fill-current"></i>').join('')}
                        </div>
                        <blockquote class="text-muted-foreground mb-4">
                            "${testimonial.content}"
                        </blockquote>
                        <div class="flex items-center gap-3">
                            <img 
                                src="${testimonial.image}" 
                                alt="${testimonial.name}"
                                class="w-12 h-12 rounded-full object-cover"
                            />
                            <div>
                                <div class="font-semibold text-foreground">${testimonial.name}</div>
                                <div class="text-sm text-muted-foreground">${testimonial.role}</div>
                            </div>
                        </div>
                    </div>
                `;
                container.innerHTML += testimonialHtml;
            });
            
            // Initialize Lucide icons for testimonials
            if (typeof lucide !== 'undefined') {
                lucide.createIcons();
            }
        })
        .catch(error => {
            console.error('Error loading testimonials:', error);
        });
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