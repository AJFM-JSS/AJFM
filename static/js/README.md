# JavaScript File Organization

This directory contains all JavaScript files for the Apply Boost Studio application, organized in a modular structure for better maintainability and performance.

## File Structure

```
static/js/
├── main.js          # Global JavaScript functionality
├── utils.js         # Common utility functions
├── home.js          # Home page specific functionality
├── get-started.js   # Get Started page functionality
├── resume-builder.js # Resume Builder page functionality
└── README.md        # This documentation file
```

## File Descriptions

### `main.js`
- **Purpose**: Global JavaScript functionality and initialization
- **Features**:
  - Lucide icons initialization
  - Global interactive elements (hover effects, loading states)
  - Mobile navigation handling
  - Global form validation setup
- **Loaded on**: All pages

### `utils.js`
- **Purpose**: Common utility functions used across multiple pages
- **Features**:
  - `showToast()` - Display toast notifications
  - `validateEmail()` - Email validation
  - `validatePhone()` - Phone number validation
  - `showFieldError()` / `clearFieldError()` - Form field error handling
  - `formatPhoneNumber()` - Phone number formatting
  - `handleFileUpload()` - File upload validation
  - `debounce()` / `throttle()` - Performance optimization functions
  - URL parameter handling functions
- **Loaded on**: All pages (via base.html)

### `home.js`
- **Purpose**: Home page specific functionality
- **Features**:
  - Testimonials loading from API
  - Interactive elements initialization
  - Smooth scrolling for anchor links
  - CTA button loading states
- **Loaded on**: Home page only

### `get-started.js`
- **Purpose**: Get Started page form handling
- **Features**:
  - File upload display management
  - Form submission to `/upload-resume` endpoint
  - Success/error handling with toast notifications
  - Redirect to scheduling link on success
- **Loaded on**: Get Started page only

### `resume-builder.js`
- **Purpose**: Resume Builder page functionality
- **Features**:
  - Real-time resume preview updates
  - Dynamic experience section management
  - Form data collection and validation
  - Resume generation and download
  - Draft saving/loading functionality
- **Loaded on**: Resume Builder page only

## Loading Order

1. **utils.js** - Loaded first in base.html
2. **main.js** - Loaded second in base.html
3. **Page-specific JS** - Loaded last via `{% block extra_scripts %}`

## Best Practices

### Adding New JavaScript Files

1. **Create the file** in `static/js/` directory
2. **Add script tag** to the appropriate template:
   ```html
   {% block extra_scripts %}
   <script src="{{ url_for('static', filename='js/your-file.js') }}"></script>
   {% endblock %}
   ```

### Function Naming Conventions

- **Global functions**: camelCase (e.g., `showToast`)
- **Page-specific functions**: descriptive names (e.g., `loadTestimonials`)
- **Private functions**: underscore prefix (e.g., `_updatePreview`)

### Error Handling

- Always wrap DOM manipulation in try-catch blocks
- Use console.log for debugging
- Provide fallbacks for missing elements

### Performance Considerations

- Use `debounce()` for frequent events (resize, scroll)
- Use `throttle()` for continuous events (mousemove)
- Minimize DOM queries by caching selectors
- Use event delegation for dynamic content

## Dependencies

- **Lucide Icons**: Loaded from CDN in base.html
- **Tailwind CSS**: Loaded from CDN in base.html
- **Utils.js**: Required by all other scripts

## Testing

To test JavaScript functionality:

1. **Open browser console** to see debug messages
2. **Check for errors** in the console
3. **Test form submissions** and verify API calls
4. **Verify toast notifications** appear correctly
5. **Test responsive behavior** on different screen sizes

## Troubleshooting

### Common Issues

1. **Script not loading**: Check file path and template inclusion
2. **Functions undefined**: Ensure utils.js loads before other scripts
3. **DOM elements not found**: Add null checks before manipulation
4. **Event listeners not working**: Verify element exists before adding listener

### Debug Mode

Enable debug logging by setting:
```javascript
window.DEBUG = true;
```

This will enable additional console logging throughout the application. 