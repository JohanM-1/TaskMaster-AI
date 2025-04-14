# Color Palette Usage Guide

## Colors Breakdown

- `palette-dark (#000e11)`: Deep charcoal - perfect for main text and strong contrasts
- `palette-navy (#1b3f44)`: Rich navy - ideal for headers and primary elements
- `palette-rose (#ba9484)`: Muted rose - great for accent elements and highlights
- `palette-sand (#c2bf96)`: Warm sand - excellent for secondary backgrounds
- `palette-light (#e0e0c9)`: Soft light - perfect for main backgrounds

## Recommended Usage

### Text Colors

```html
<p class="text-palette-dark">Main content text</p>
<h1 class="text-palette-navy">Headers</h1>
<span class="text-palette-rose">Accent text</span>
```

### Background Applications

```html
<div class="bg-palette-light">Main container</div>
<div class="bg-palette-sand">Secondary sections</div>
<div class="bg-palette-navy text-palette-light">Feature blocks</div>
```

### Modern Design Prompt

This color palette suggests a modern, organic, and sophisticated design approach:

1. Use plenty of white space
2. Implement a minimalist layout with clear hierarchy
3. Utilize the palette-light as the primary background
4. Apply palette-navy for main interactive elements
5. Use palette-rose sparingly for call-to-action buttons or highlights
6. Incorporate palette-sand for subtle section differentiation
7. Reserve palette-dark for main text content

### Example Component Structure

````html
<div class="bg-palette-light min-h-screen p-8">
    <nav class="bg-palette-navy text-palette-light p-4 rounded-lg">
        <!-- Navigation content -->
    </nav>
    
    <main class="my-8">
        <h1 class="text-palette-navy text-4xl font-light mb-6">Welcome</h1>
        
        <div class="bg-palette-sand bg-opacity-50 p-6 rounded-lg">
            <p class="text-palette-dark">Main content area</p>
            
            <button class="bg-palette-rose text-white px-4 py-2 rounded-md hover:opacity-90 transition">
                Call to Action
            </button>
        </div>
    </main>
</div>
````

This palette creates a calm, professional appearance while maintaining modern design principles through its earthy, muted tones.

### Form Styling

Forms should follow a floating label design pattern with the established color scheme:

```html
<form class="max-w-md mx-auto bg-palette-light p-6 rounded-lg">
  <div class="relative z-0 w-full mb-5 group">
      <input type="email" 
             name="floating_email" 
             id="floating_email" 
             class="block py-2.5 px-0 w-full text-sm text-palette-dark bg-transparent border-0 border-b-2 border-palette-navy appearance-none focus:outline-none focus:ring-0 focus:border-palette-rose peer" 
             placeholder=" " 
             required />
      <label for="floating_email" 
             class="peer-focus:font-medium absolute text-sm text-palette-navy duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 peer-focus:text-palette-rose peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">
        Email address
      </label>
  </div>

  <!-- Input group example -->
  <div class="grid md:grid-cols-2 md:gap-6">
    <div class="relative z-0 w-full mb-5 group">
        <input type="text" 
               name="floating_first_name" 
               id="floating_first_name" 
               class="block py-2.5 px-0 w-full text-sm text-palette-dark bg-transparent border-0 border-b-2 border-palette-navy appearance-none focus:outline-none focus:ring-0 focus:border-palette-rose peer" 
               placeholder=" " 
               required />
        <label for="floating_first_name" 
               class="peer-focus:font-medium absolute text-sm text-palette-navy duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 peer-focus:text-palette-rose peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">
          First name
        </label>
    </div>
    <!-- Add similar structure for other inputs -->
  </div>

  <button type="submit" 
          class="w-full sm:w-auto px-5 py-2.5 text-center bg-palette-navy hover:bg-opacity-90 text-palette-light rounded-lg transition-all focus:ring-4 focus:ring-palette-rose focus:ring-opacity-50">
    Submit
  </button>
</form>
```

Key Form Styling Points:

1. Use `bg-palette-light` for form container background
2. Apply `text-palette-dark` for input text
3. Use `border-palette-navy` for default input borders
4. Change to `border-palette-rose` on focus
5. Style labels with `text-palette-navy`
6. Transform labels to `text-palette-rose` on focus
7. Style submit buttons with `bg-palette-navy` and `text-palette-light`
8. Add `hover:bg-opacity-90` for subtle hover effects
9. Include `focus:ring-palette-rose` for accessible focus states
