# Color Palette Usage Guide

## Colors Breakdown

- `palette-dark (#000e11)`: Deep charcoal - perfect for main text and strong contrasts
- `palette-navy (#1b3f44)`: Rich navy - ideal for headers and primary elements
- `palette-rose (#ba9484)`: Muted rose - great for accent elements and highlights
- `palette-sand (#c2bf96)`: Warm sand - excellent for secondary backgrounds
- `palette-light (#e0e0c9)`: Soft light - perfect for main backgrounds

## Dark Mode Implementation

For dark mode support, use Tailwind's `dark:` prefix. The color scheme should invert appropriately:

- Light backgrounds become dark (`palette-light` → `palette-dark`)
- Dark text becomes light (`palette-dark` → `palette-light`)
- Accent colors adjust opacity for better visibility

## Recommended Usage

### Text Colors

```html
<p class="text-palette-dark dark:text-palette-light">Main content text</p>
<h1 class="text-palette-navy dark:text-palette-light">Headers</h1>
<span class="text-palette-rose dark:text-palette-rose">Accent text</span>
```

### Background Applications

```html
<div class="bg-palette-light dark:bg-palette-dark">Main container</div>
<div class="bg-palette-sand dark:bg-palette-navy">Secondary sections</div>
<div class="bg-palette-navy dark:bg-palette-dark text-palette-light">Feature blocks</div>
```

### Modern Design Prompt

This color palette creates a responsive design that adapts to both light and dark modes:

1. Use plenty of white space
2. Implement a minimalist layout with clear hierarchy
3. Light mode:
   - Use palette-light as primary background
   - Apply palette-navy for interactive elements
   - Use palette-dark for text
4. Dark mode:
   - Use palette-dark as primary background
   - Apply palette-navy or palette-rose for interactive elements
   - Use palette-light for text
5. Use palette-rose sparingly for accents in both modes
6. Ensure sufficient contrast in both modes

### Example Component Structure

````html
<div class="bg-palette-light dark:bg-palette-dark min-h-screen p-8">
    <nav class="bg-palette-navy dark:bg-palette-dark text-palette-light p-4 rounded-lg">
        <!-- Navigation content -->
    </nav>
    
    <main class="my-8">
        <h1 class="text-palette-navy dark:text-palette-light text-4xl font-light mb-6">Welcome</h1>
        
        <div class="bg-palette-sand dark:bg-palette-navy bg-opacity-50 dark:bg-opacity-30 p-6 rounded-lg">
            <p class="text-palette-dark dark:text-palette-light">Main content area</p>
            
            <button class="bg-palette-rose dark:bg-palette-rose text-white px-4 py-2 rounded-md hover:opacity-90 dark:hover:opacity-80 transition">
                Call to Action
            </button>
        </div>
    </main>
</div>
````

This palette creates a calm, professional appearance while maintaining modern design principles through its earthy, muted tones.

### Form Styling

Forms should adapt to both light and dark modes while maintaining accessibility:

```html
<form class="max-w-md mx-auto bg-palette-light dark:bg-palette-dark p-6 rounded-lg">
    <div class="relative z-0 w-full mb-5 group">
        <input type="email" 
               name="floating_email" 
               id="floating_email" 
               class="block py-2.5 px-0 w-full text-sm 
                      text-palette-dark dark:text-palette-light 
                      bg-transparent border-0 border-b-2 
                      border-palette-navy dark:border-palette-sand 
                      appearance-none focus:outline-none focus:ring-0 
                      focus:border-palette-rose dark:focus:border-palette-rose 
                      peer" 
               placeholder=" " 
               required />
        <label for="floating_email" 
               class="peer-focus:font-medium absolute text-sm 
                      text-palette-navy dark:text-palette-sand 
                      duration-300 transform -translate-y-6 scale-75 
                      top-3 -z-10 origin-[0] peer-focus:start-0 
                      peer-focus:text-palette-rose 
                      dark:peer-focus:text-palette-rose 
                      peer-placeholder-shown:scale-100 
                      peer-placeholder-shown:translate-y-0 
                      peer-focus:scale-75 peer-focus:-translate-y-6">
            Email address
        </label>
    </div>

    <button type="submit" 
            class="w-full py-2 px-4 border border-transparent rounded-md 
                   shadow-sm text-sm font-medium text-white 
                   bg-palette-navy dark:bg-palette-rose 
                   hover:bg-opacity-90 dark:hover:bg-opacity-80 
                   transition focus:outline-none focus:ring-2 
                   focus:ring-offset-2 focus:ring-palette-navy 
                   dark:focus:ring-palette-rose">
        Submit
    </button>
</form>
```

### Hover and Focus States

Remember to include dark mode variants for interactive states:

```html
<!-- Button hover states -->
<button class="bg-palette-navy dark:bg-palette-rose 
               hover:bg-opacity-90 dark:hover:bg-opacity-80">
    Action
</button>

<!-- Link hover states -->
<a class="text-palette-navy dark:text-palette-light 
          hover:text-palette-rose dark:hover:text-palette-rose">
    Link
</a>

<!-- Input focus states -->
<input class="border-palette-sand dark:border-palette-navy 
              focus:border-palette-rose dark:focus:border-palette-rose">
```

### Dark Mode Transitions

For smooth theme switching, add transition properties:

```html
<div class="transition-colors duration-200 
            bg-palette-light dark:bg-palette-dark">
    Content
</div>
```

Remember to test all components in both light and dark modes to ensure proper contrast and readability.
