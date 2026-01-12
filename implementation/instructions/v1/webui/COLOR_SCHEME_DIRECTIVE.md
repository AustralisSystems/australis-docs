# COLOR SCHEME DIRECTIVE
## Mandatory Color Usage Guidelines for WebUI Factory

**Status:** ENFORCED
**Applies To:** All WebUI template generation, component creation, and styling operations
**Priority:** CRITICAL - Non-compliance prevents deployment

---

## 1. Core Principle

**NEVER use hardcoded color values.** All colors MUST use DaisyUI semantic utilities or Tailwind v4 color scheme tokens to ensure full theme compatibility (light/dark/custom themes) and component library integration.

---

## 2. Prohibited Color Patterns

### ❌ FORBIDDEN - Hardcoded Colors
```html
<!-- WRONG - hardcoded colors -->
<div class="bg-white text-black border-gray-200">
<div class="bg-gray-50 text-gray-900">
<div class="bg-blue-500 text-white">
<button class="bg-red-600 hover:bg-red-700">
```

### ❌ FORBIDDEN - Named Color Utilities
```html
<!-- WRONG - named color utilities -->
<div class="bg-red-500">
<div class="text-blue-600">
<div class="border-green-400">
<span class="bg-yellow-200">
```

---

## 3. Required Color Patterns

### ✅ CORRECT - DaisyUI Semantic Classes

#### Background Colors
```html
<!-- Base/Surface Colors -->
<div class="bg-base-100">      <!-- Primary background -->
<div class="bg-base-200">      <!-- Secondary background (elevated) -->
<div class="bg-base-300">      <!-- Tertiary background (more elevated) -->
<div class="bg-base-content">  <!-- Content background (inverse) -->
```

#### Text Colors
```html
<!-- Semantic Text Colors -->
<span class="text-base-content">        <!-- Primary text -->
<span class="text-neutral-content">     <!-- Neutral text -->
<span class="text-primary-content">     <!-- Text on primary bg -->
<span class="text-secondary-content">   <!-- Text on secondary bg -->
<span class="text-accent-content">      <!-- Text on accent bg -->
```

#### Border Colors
```html
<!-- Semantic Borders -->
<div class="border border-base-300">     <!-- Default border -->
<div class="border border-primary">      <!-- Primary colored border -->
<div class="border border-neutral">      <!-- Neutral border -->
```

#### Component Semantic Colors
```html
<!-- Action/State Colors -->
<button class="btn btn-primary">     <!-- Primary action -->
<button class="btn btn-secondary">   <!-- Secondary action -->
<button class="btn btn-accent">      <!-- Accent action -->
<button class="btn btn-ghost">       <!-- Subtle action -->
<button class="btn btn-neutral">     <!-- Neutral action -->

<!-- Status Colors -->
<div class="alert alert-info">       <!-- Informational -->
<div class="alert alert-success">    <!-- Success state -->
<div class="alert alert-warning">    <!-- Warning state -->
<div class="alert alert-error">      <!-- Error state -->

<!-- Badge Status -->
<span class="badge badge-info">      <!-- Info badge -->
<span class="badge badge-success">   <!-- Success badge -->
<span class="badge badge-warning">   <!-- Warning badge -->
<span class="badge badge-error">     <!-- Error badge -->
```

---

## 4. DaisyUI Component Classes (REQUIRED)

### Form Components
```html
<!-- Input Fields -->
<input class="input input-bordered">           <!-- Standard input -->
<input class="input input-sm input-bordered">  <!-- Small input -->
<input class="input input-lg input-bordered">  <!-- Large input -->
<input class="input input-primary">            <!-- Primary styled input -->

<!-- Select Dropdowns -->
<select class="select select-bordered">        <!-- Standard select -->
<select class="select select-sm">              <!-- Small select -->
<select class="select select-primary">         <!-- Primary styled select -->

<!-- Textarea -->
<textarea class="textarea textarea-bordered">  <!-- Standard textarea -->
<textarea class="textarea textarea-primary">   <!-- Primary styled textarea -->

<!-- Checkbox & Radio -->
<input type="checkbox" class="checkbox">               <!-- Standard checkbox -->
<input type="checkbox" class="checkbox checkbox-primary"> <!-- Primary checkbox -->
<input type="radio" class="radio radio-primary">       <!-- Primary radio -->

<!-- Toggle -->
<input type="checkbox" class="toggle toggle-primary">  <!-- Toggle switch -->
```

### Layout Components
```html
<!-- Cards -->
<div class="card bg-base-100 shadow-md">      <!-- Standard card -->
<div class="card card-compact bg-base-200">   <!-- Compact card -->
<div class="card card-bordered">              <!-- Bordered card -->

<!-- Drawers/Sidebars -->
<div class="drawer">                          <!-- Drawer container -->
<div class="drawer-side bg-base-200">         <!-- Sidebar background -->

<!-- Navbar -->
<div class="navbar bg-base-100">              <!-- Navbar with base bg -->

<!-- Tables -->
<table class="table">                         <!-- Standard table -->
<tr class="hover">                            <!-- Hoverable row -->
<tr class="active">                           <!-- Active row -->
```

### Interactive Components
```html
<!-- Buttons -->
<button class="btn btn-primary">              <!-- Primary button -->
<button class="btn btn-secondary">            <!-- Secondary button -->
<button class="btn btn-accent">               <!-- Accent button -->
<button class="btn btn-ghost">                <!-- Ghost button -->
<button class="btn btn-link">                 <!-- Link button -->

<!-- Modal -->
<dialog class="modal">                        <!-- Modal container -->
<div class="modal-box bg-base-100">           <!-- Modal content box -->

<!-- Dropdown -->
<div class="dropdown">                        <!-- Dropdown container -->
<ul class="dropdown-content menu bg-base-100 shadow-lg"> <!-- Dropdown menu -->
```

---

## 5. Theme Support Requirements

### Light/Dark Theme Compatibility
All components MUST work in:
- Light theme (`data-theme="light"`)
- Dark theme (`data-theme="dark"`)
- Custom themes (e.g., `data-theme="corporate"`, `data-theme="cyberpunk"`)

### Theme Switching
```html
<!-- HTML root element with theme attribute -->
<html lang="en" data-theme="light">

<!-- Theme switcher example -->
<select data-choose-theme>
  <option value="light">Light</option>
  <option value="dark">Dark</option>
  <option value="corporate">Corporate</option>
  <option value="cyberpunk">Cyberpunk</option>
</select>
```

### CSS Custom Properties (Tailwind v4)
```css
/* Use CSS variables for dynamic theming */
.custom-component {
  background: oklch(var(--b1));        /* Base-100 color */
  color: oklch(var(--bc));             /* Base-content color */
  border-color: oklch(var(--b3));      /* Base-300 color */
}
```

---

## 6. Migration Rules for Existing Code

### Pattern Replacement Matrix

| ❌ Old Pattern | ✅ New Pattern | Usage |
|---------------|---------------|-------|
| `bg-white` | `bg-base-100` | Primary background |
| `bg-gray-50` | `bg-base-200` | Elevated background |
| `bg-gray-100` | `bg-base-300` | More elevated background |
| `bg-gray-900` | `bg-base-content` | Inverse background |
| `text-black` | `text-base-content` | Primary text |
| `text-gray-600` | `text-base-content/70` | Muted text |
| `text-gray-400` | `text-base-content/50` | Very muted text |
| `text-white` | `text-base-100` or `text-primary-content` | Light text |
| `border-gray-200` | `border-base-300` | Default border |
| `border-gray-300` | `border-neutral` | Neutral border |
| `bg-blue-500` | `bg-primary` | Primary action background |
| `bg-green-500` | `bg-success` | Success background |
| `bg-red-500` | `bg-error` | Error background |
| `bg-yellow-500` | `bg-warning` | Warning background |
| `text-blue-600` | `text-primary` | Primary text |
| `text-green-600` | `text-success` | Success text |
| `text-red-600` | `text-error` | Error text |

---

## 7. Validation Checklist

Before deploying any WebUI component or template:

- [ ] No hardcoded hex/rgb/rgba color values in HTML or CSS
- [ ] No `bg-{color}-{shade}` classes (e.g., `bg-gray-50`, `bg-blue-500`)
- [ ] No `text-{color}-{shade}` classes (e.g., `text-black`, `text-red-600`)
- [ ] No `border-{color}-{shade}` classes (e.g., `border-gray-200`)
- [ ] All backgrounds use `bg-base-{n}` or semantic classes
- [ ] All text uses `text-base-content` or semantic classes
- [ ] All borders use `border-base-{n}` or semantic classes
- [ ] All buttons use `btn btn-{variant}` classes
- [ ] All form inputs use DaisyUI component classes
- [ ] Component tested in both light and dark themes
- [ ] Component tested with at least 2 custom themes

---

## 8. Code Review Triggers

**AUTOMATIC REJECTION** if code contains:
- Any `bg-white`, `bg-black`, `bg-gray-*` class
- Any `text-white`, `text-black`, `text-gray-*` class
- Any `border-gray-*` class
- Any hardcoded hex colors (`#FFFFFF`, `#000000`, etc.)
- Any RGB/RGBA color functions in inline styles

**REQUIRE JUSTIFICATION** if code contains:
- CSS custom properties not derived from DaisyUI tokens
- Inline styles with color values
- Third-party component libraries with hardcoded colors

---

## 9. Implementation Examples

### ✅ CORRECT - Full Page Template
```html
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <title>User Dashboard</title>
  <link href="/static/css/output.css" rel="stylesheet">
</head>
<body class="bg-base-100">
  <div class="drawer lg:drawer-open">
    <!-- Sidebar -->
    <div class="drawer-side bg-base-200">
      <label for="drawer" class="drawer-overlay"></label>
      <ul class="menu p-4">
        <li><a class="text-base-content">Home</a></li>
        <li><a class="text-base-content">Users</a></li>
      </ul>
    </div>

    <!-- Main Content -->
    <div class="drawer-content">
      <div class="navbar bg-base-100 border-b border-base-300">
        <h1 class="text-2xl font-bold text-base-content">Dashboard</h1>
      </div>

      <main class="p-6">
        <div class="card bg-base-100 shadow-md">
          <div class="card-body">
            <h2 class="card-title text-base-content">User Statistics</h2>
            <p class="text-base-content/70">Active users today</p>
            <div class="stats bg-base-200">
              <div class="stat">
                <div class="stat-value text-primary">1,234</div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</body>
</html>
```

### ✅ CORRECT - Form Component
```html
<form class="space-y-4">
  <div class="form-control">
    <label class="label">
      <span class="label-text text-base-content">Email</span>
    </label>
    <input type="email" class="input input-bordered w-full" />
  </div>

  <div class="form-control">
    <label class="label">
      <span class="label-text text-base-content">Status</span>
    </label>
    <select class="select select-bordered w-full">
      <option>Active</option>
      <option>Inactive</option>
    </select>
  </div>

  <div class="form-control">
    <label class="label cursor-pointer">
      <span class="label-text text-base-content">Subscribe</span>
      <input type="checkbox" class="toggle toggle-primary" />
    </label>
  </div>

  <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

### ✅ CORRECT - Data Table
```html
<div class="overflow-x-auto bg-base-100 rounded-lg shadow">
  <table class="table">
    <thead class="bg-base-200">
      <tr>
        <th class="text-base-content">Name</th>
        <th class="text-base-content">Status</th>
        <th class="text-base-content">Actions</th>
      </tr>
    </thead>
    <tbody>
      <tr class="hover">
        <td class="text-base-content">John Doe</td>
        <td><span class="badge badge-success">Active</span></td>
        <td>
          <button class="btn btn-sm btn-ghost">Edit</button>
          <button class="btn btn-sm btn-error">Delete</button>
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

---

## 10. Enforcement Protocol

### During Code Generation
1. AI must scan all generated HTML/CSS for prohibited patterns
2. AI must replace hardcoded colors with semantic equivalents
3. AI must document any edge cases requiring manual review

### During Code Review
1. Automated linting must flag prohibited color patterns
2. Manual review required for any inline styles with colors
3. Theme compatibility testing MANDATORY before deployment

### Exceptions Process
If hardcoded colors are absolutely necessary (rare):
1. Document technical justification
2. Get approval from tech lead
3. Add TODO comment with migration plan
4. Track as technical debt

---

## 11. User Customization Requirements

### MANDATORY User Controls

All WebUI applications MUST provide users with the ability to:
1. **Select Theme** - Choose from available themes (light, dark, custom)
2. **Adjust Brightness** - Fine-tune base colors for comfort
3. **Save Preferences** - Persist theme and customization choices
4. **Reset to Defaults** - Restore original theme settings

---

### 11.1 Theme Selector Implementation

#### Basic Theme Switcher (Required)
```html
<!-- Theme selection dropdown -->
<div class="form-control">
  <label class="label">
    <span class="label-text text-base-content">Theme</span>
  </label>
  <select
    data-choose-theme
    class="select select-bordered w-full"
    onchange="saveThemePreference(this.value)"
  >
    <option value="light">Light</option>
    <option value="dark">Dark</option>
    <option value="corporate">Corporate</option>
    <option value="cyberpunk">Cyberpunk</option>
    <option value="cupcake">Cupcake</option>
    <option value="forest">Forest</option>
    <option value="luxury">Luxury</option>
    <option value="dracula">Dracula</option>
  </select>
</div>
```

#### Theme Switcher with Icons (Enhanced UX)
```html
<!-- Theme toggle button (light/dark) -->
<label class="swap swap-rotate btn btn-ghost btn-circle">
  <input
    type="checkbox"
    data-toggle-theme="light,dark"
    onchange="saveThemePreference(this.checked ? 'dark' : 'light')"
  />

  <!-- Sun icon -->
  <svg class="swap-off fill-current w-6 h-6" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
    <path d="M5.64,17l-.71.71a1,1,0,0,0,0,1.41,1,1,0,0,0,1.41,0l.71-.71A1,1,0,0,0,5.64,17ZM5,12a1,1,0,0,0-1-1H3a1,1,0,0,0,0,2H4A1,1,0,0,0,5,12Zm7-7a1,1,0,0,0,1-1V3a1,1,0,0,0-2,0V4A1,1,0,0,0,12,5ZM5.64,7.05a1,1,0,0,0,.7.29,1,1,0,0,0,.71-.29,1,1,0,0,0,0-1.41l-.71-.71A1,1,0,0,0,4.93,6.34Zm12,.29a1,1,0,0,0,.7-.29l.71-.71a1,1,0,1,0-1.41-1.41L17,5.64a1,1,0,0,0,0,1.41A1,1,0,0,0,17.66,7.34ZM21,11H20a1,1,0,0,0,0,2h1a1,1,0,0,0,0-2Zm-9,8a1,1,0,0,0-1,1v1a1,1,0,0,0,2,0V20A1,1,0,0,0,12,19ZM18.36,17A1,1,0,0,0,17,18.36l.71.71a1,1,0,0,0,1.41,0,1,1,0,0,0,0-1.41ZM12,6.5A5.5,5.5,0,1,0,17.5,12,5.51,5.51,0,0,0,12,6.5Zm0,9A3.5,3.5,0,1,1,15.5,12,3.5,3.5,0,0,1,12,15.5Z"/>
  </svg>

  <!-- Moon icon -->
  <svg class="swap-on fill-current w-6 h-6" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
    <path d="M21.64,13a1,1,0,0,0-1.05-.14,8.05,8.05,0,0,1-3.37.73A8.15,8.15,0,0,1,9.08,5.49a8.59,8.59,0,0,1,.25-2A1,1,0,0,0,8,2.36,10.14,10.14,0,1,0,22,14.05,1,1,0,0,0,21.64,13Zm-9.5,6.69A8.14,8.14,0,0,1,7.08,5.22v.27A10.15,10.15,0,0,0,17.22,15.63a9.79,9.79,0,0,0,2.1-.22A8.11,8.11,0,0,1,12.14,19.73Z"/>
  </svg>
</label>
```

---

### 11.2 Brightness Adjustment Controls (Required)

Users MUST be able to adjust base color brightness for visual comfort.

#### Implementation Pattern
```html
<!-- Brightness adjustment controls -->
<div class="form-control">
  <label class="label">
    <span class="label-text text-base-content">Theme Brightness</span>
    <span class="label-text-alt text-base-content/70" id="brightness-value">100%</span>
  </label>

  <!-- Brightness slider -->
  <input
    type="range"
    min="50"
    max="150"
    value="100"
    step="5"
    class="range range-primary"
    id="brightness-slider"
    onchange="adjustBrightness(this.value)"
    oninput="updateBrightnessLabel(this.value)"
  />

  <div class="w-full flex justify-between text-xs px-2 text-base-content/50">
    <span>Darker</span>
    <span>Default</span>
    <span>Brighter</span>
  </div>
</div>

<!-- Separate controls for light/dark themes -->
<details class="collapse collapse-arrow bg-base-200">
  <summary class="collapse-title text-base-content">
    Advanced Color Adjustments
  </summary>
  <div class="collapse-content space-y-4">

    <!-- Light theme brightness -->
    <div class="form-control">
      <label class="label">
        <span class="label-text text-base-content">Light Theme Brightness</span>
        <span class="label-text-alt" id="light-brightness">100%</span>
      </label>
      <input
        type="range"
        min="70"
        max="130"
        value="100"
        class="range range-sm"
        id="light-brightness-slider"
        onchange="adjustLightBrightness(this.value)"
      />
      <span class="text-xs text-base-content/70 mt-1">
        Adjust if light theme is too bright
      </span>
    </div>

    <!-- Dark theme brightness -->
    <div class="form-control">
      <label class="label">
        <span class="label-text text-base-content">Dark Theme Brightness</span>
        <span class="label-text-alt" id="dark-brightness">100%</span>
      </label>
      <input
        type="range"
        min="70"
        max="130"
        value="100"
        class="range range-sm"
        id="dark-brightness-slider"
        onchange="adjustDarkBrightness(this.value)"
      />
      <span class="text-xs text-base-content/70 mt-1">
        Adjust if dark theme is too dark or too bright
      </span>
    </div>

    <!-- Contrast adjustment -->
    <div class="form-control">
      <label class="label">
        <span class="label-text text-base-content">Color Contrast</span>
        <span class="label-text-alt" id="contrast-value">Normal</span>
      </label>
      <input
        type="range"
        min="80"
        max="120"
        value="100"
        step="10"
        class="range range-sm"
        id="contrast-slider"
        onchange="adjustContrast(this.value)"
      />
      <div class="w-full flex justify-between text-xs px-2 text-base-content/50">
        <span>Low</span>
        <span>Normal</span>
        <span>High</span>
      </div>
    </div>

    <!-- Reset button -->
    <button
      class="btn btn-sm btn-outline w-full"
      onclick="resetColorCustomizations()"
    >
      Reset to Defaults
    </button>
  </div>
</details>
```

---

### 11.3 CSS Implementation (Required)

Brightness adjustments MUST be implemented using CSS custom properties and filters.

```css
/* Apply brightness adjustments to root element */
:root[data-theme="light"] {
  --brightness-adjustment: 1;
  --contrast-adjustment: 1;
}

:root[data-theme="dark"] {
  --brightness-adjustment: 1;
  --contrast-adjustment: 1;
}

/* Apply adjustments to base backgrounds */
html[data-theme] {
  filter:
    brightness(var(--brightness-adjustment))
    contrast(var(--contrast-adjustment));
}

/* Alternative: Adjust CSS color variables directly */
:root[data-theme="light"][data-brightness="dim"] {
  --b1: 95 5% 95%;  /* Slightly dimmer than default 100% */
  --b2: 90 5% 90%;
  --b3: 85 5% 85%;
}

:root[data-theme="dark"][data-brightness="bright"] {
  --b1: 225 6% 20%;  /* Slightly brighter than default 13% */
  --b2: 225 6% 17%;
  --b3: 225 6% 14%;
}
```

---

### 11.4 JavaScript Implementation (Required)

```javascript
// Theme and brightness management
class ThemeCustomizer {
  constructor() {
    this.loadSavedPreferences();
    this.initializeControls();
  }

  // Load saved preferences from localStorage
  loadSavedPreferences() {
    const saved = localStorage.getItem('themePreferences');
    if (saved) {
      const prefs = JSON.parse(saved);
      this.applyTheme(prefs.theme || 'light');
      this.applyBrightness(prefs.brightness || 100);
      this.applyLightBrightness(prefs.lightBrightness || 100);
      this.applyDarkBrightness(prefs.darkBrightness || 100);
      this.applyContrast(prefs.contrast || 100);
    }
  }

  // Save preferences to localStorage
  savePreferences() {
    const prefs = {
      theme: this.getCurrentTheme(),
      brightness: this.getBrightness(),
      lightBrightness: this.getLightBrightness(),
      darkBrightness: this.getDarkBrightness(),
      contrast: this.getContrast(),
      timestamp: new Date().toISOString()
    };
    localStorage.setItem('themePreferences', JSON.stringify(prefs));

    // Optionally sync to server for cross-device preferences
    this.syncToServer(prefs);
  }

  // Apply theme
  applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    this.savePreferences();
  }

  // Apply brightness adjustment
  applyBrightness(value) {
    const brightness = value / 100;
    document.documentElement.style.setProperty('--brightness-adjustment', brightness);
    this.savePreferences();
  }

  // Apply light theme specific brightness
  applyLightBrightness(value) {
    if (this.getCurrentTheme() === 'light') {
      const brightness = value / 100;
      document.documentElement.style.setProperty('--brightness-adjustment', brightness);
    }
    this.savePreferences();
  }

  // Apply dark theme specific brightness
  applyDarkBrightness(value) {
    if (this.getCurrentTheme() === 'dark') {
      const brightness = value / 100;
      document.documentElement.style.setProperty('--brightness-adjustment', brightness);
    }
    this.savePreferences();
  }

  // Apply contrast adjustment
  applyContrast(value) {
    const contrast = value / 100;
    document.documentElement.style.setProperty('--contrast-adjustment', contrast);
    this.savePreferences();
  }

  // Reset to defaults
  resetToDefaults() {
    this.applyTheme('light');
    this.applyBrightness(100);
    this.applyLightBrightness(100);
    this.applyDarkBrightness(100);
    this.applyContrast(100);

    // Reset UI controls
    document.getElementById('brightness-slider').value = 100;
    document.getElementById('light-brightness-slider').value = 100;
    document.getElementById('dark-brightness-slider').value = 100;
    document.getElementById('contrast-slider').value = 100;
  }

  // Sync preferences to server (optional)
  async syncToServer(prefs) {
    try {
      await fetch('/api/user/preferences/theme', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(prefs)
      });
    } catch (error) {
      console.warn('Failed to sync theme preferences:', error);
    }
  }

  // Get current values
  getCurrentTheme() {
    return document.documentElement.getAttribute('data-theme') || 'light';
  }

  getBrightness() {
    return parseInt(document.getElementById('brightness-slider')?.value || 100);
  }

  getLightBrightness() {
    return parseInt(document.getElementById('light-brightness-slider')?.value || 100);
  }

  getDarkBrightness() {
    return parseInt(document.getElementById('dark-brightness-slider')?.value || 100);
  }

  getContrast() {
    return parseInt(document.getElementById('contrast-slider')?.value || 100);
  }
}

// Initialize theme customizer
const themeCustomizer = new ThemeCustomizer();

// Helper functions for inline event handlers
function saveThemePreference(theme) {
  themeCustomizer.applyTheme(theme);
}

function adjustBrightness(value) {
  themeCustomizer.applyBrightness(value);
}

function adjustLightBrightness(value) {
  themeCustomizer.applyLightBrightness(value);
}

function adjustDarkBrightness(value) {
  themeCustomizer.applyDarkBrightness(value);
}

function adjustContrast(value) {
  themeCustomizer.applyContrast(value);
}

function updateBrightnessLabel(value) {
  document.getElementById('brightness-value').textContent = value + '%';
}

function resetColorCustomizations() {
  themeCustomizer.resetToDefaults();
}
```

---

### 11.5 Backend API Requirements (Optional but Recommended)

#### Save User Preferences Endpoint
```python
# FastAPI endpoint for saving theme preferences
@router.post("/api/user/preferences/theme")
async def save_theme_preferences(
    preferences: ThemePreferences,
    current_user: User = Depends(get_current_user)
):
    """
    Save user's theme and color customization preferences.
    Allows cross-device synchronization.
    """
    await db.user_preferences.update_one(
        {"user_id": current_user.id},
        {"$set": {
            "theme": preferences.theme,
            "brightness": preferences.brightness,
            "light_brightness": preferences.light_brightness,
            "dark_brightness": preferences.dark_brightness,
            "contrast": preferences.contrast,
            "updated_at": datetime.utcnow()
        }},
        upsert=True
    )
    return {"success": True}

# Pydantic model
class ThemePreferences(BaseModel):
    theme: str = "light"
    brightness: int = Field(default=100, ge=50, le=150)
    light_brightness: int = Field(default=100, ge=70, le=130)
    dark_brightness: int = Field(default=100, ge=70, le=130)
    contrast: int = Field(default=100, ge=80, le=120)
```

---

### 11.6 Accessibility Considerations

**CRITICAL:** All brightness adjustments MUST maintain WCAG contrast ratios.

```javascript
// Validate contrast after brightness adjustment
function validateContrast(brightness, contrast) {
  // Calculate effective contrast ratio
  const effectiveContrast = (contrast / 100) * (brightness / 100);

  // Warn if below WCAG AA threshold
  if (effectiveContrast < 0.7) {  // Approximation for 4.5:1 ratio
    showWarning(
      'Your brightness settings may reduce text readability. ' +
      'Consider adjusting contrast or brightness for better visibility.'
    );
  }
}

// Show accessibility warning
function showWarning(message) {
  const alert = document.createElement('div');
  alert.className = 'alert alert-warning shadow-lg';
  alert.innerHTML = `
    <div>
      <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current flex-shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
      </svg>
      <span>${message}</span>
    </div>
  `;
  document.body.appendChild(alert);
  setTimeout(() => alert.remove(), 5000);
}
```

---

### 11.7 User Preference Persistence Strategy

1. **localStorage** (Client-side, immediate)
   - Saves instantly
   - Works offline
   - Per-device only

2. **Server API** (Cross-device sync)
   - Syncs across devices
   - Requires authentication
   - Persists long-term

3. **Cookie fallback** (Legacy support)
   - Compatible with older browsers
   - Limited size (4KB)
   - Domain-specific

**Recommended:** Use localStorage + Server API hybrid approach.

---

### 11.8 Implementation Checklist

All WebUI applications MUST include:

- [ ] Theme selector dropdown/toggle (minimum: light/dark)
- [ ] Brightness adjustment slider (50-150% range)
- [ ] Separate light theme brightness control
- [ ] Separate dark theme brightness control
- [ ] Contrast adjustment control
- [ ] Reset to defaults button
- [ ] localStorage persistence
- [ ] Visual feedback on changes (real-time preview)
- [ ] WCAG contrast validation warnings
- [ ] Accessibility labels (ARIA)
- [ ] Keyboard navigation support
- [ ] Mobile-friendly controls
- [ ] Optional: Server API sync
- [ ] Optional: Cross-device preference sync

---

## 12. User Customization Implementation Guide

### 12.1 Theme Selection Interface

Users MUST be able to select from all available DaisyUI themes plus custom themes.

**Required Theme Options:**
- Light (default)
- Dark
- Corporate
- Cyberpunk
- Synthwave
- Retro
- Valentine
- Aqua
- Custom (user-defined)

**Implementation Example:**

```html
<!-- Theme Selector Component -->
<div class="form-control">
  <label class="label">
    <span class="label-text">Select Theme</span>
  </label>
  <select id="theme-selector" class="select select-bordered w-full" onchange="changeTheme(this.value)">
    <option value="light">Light</option>
    <option value="dark">Dark</option>
    <option value="corporate">Corporate</option>
    <option value="cyberpunk">Cyberpunk</option>
    <option value="synthwave">Synthwave</option>
    <option value="retro">Retro</option>
    <option value="valentine">Valentine</option>
    <option value="aqua">Aqua</option>
    <option value="custom">Custom</option>
  </select>
</div>

<script>
function changeTheme(theme) {
  // Apply theme to document
  document.documentElement.setAttribute('data-theme', theme);

  // Save to localStorage
  localStorage.setItem('user-theme', theme);

  // Optional: Sync to server
  if (typeof syncThemeToServer === 'function') {
    syncThemeToServer(theme);
  }

  // Show confirmation
  showToast(`Theme changed to ${theme}`, 'success');
}

// Apply saved theme on page load
document.addEventListener('DOMContentLoaded', () => {
  const savedTheme = localStorage.getItem('user-theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);
  document.getElementById('theme-selector').value = savedTheme;
});
</script>
```

---

### 12.2 Color Adjustment Controls

Users MUST be able to adjust base colors for accessibility and personal preference.

**Required Color Adjustment Sliders:**
- Base-100 (Primary background)
- Base-200 (Secondary background)
- Base-300 (Borders/dividers)
- Primary color hue
- Accent color hue

**Implementation Example:**

```html
<!-- Color Adjustment Panel -->
<div class="card bg-base-100 shadow-xl">
  <div class="card-body">
    <h2 class="card-title">Customize Colors</h2>

    <!-- Base-100 Adjustment -->
    <div class="form-control">
      <label class="label">
        <span class="label-text">Background Lightness</span>
        <span class="label-text-alt" id="base100-value">100%</span>
      </label>
      <input
        type="range"
        min="80"
        max="120"
        value="100"
        class="range range-primary"
        id="base100-slider"
        oninput="adjustBase100(this.value)"
      />
    </div>

    <!-- Base-200 Adjustment -->
    <div class="form-control">
      <label class="label">
        <span class="label-text">Secondary Background</span>
        <span class="label-text-alt" id="base200-value">100%</span>
      </label>
      <input
        type="range"
        min="80"
        max="120"
        value="100"
        class="range range-secondary"
        id="base200-slider"
        oninput="adjustBase200(this.value)"
      />
    </div>

    <!-- Base-300 Adjustment -->
    <div class="form-control">
      <label class="label">
        <span class="label-text">Border Intensity</span>
        <span class="label-text-alt" id="base300-value">100%</span>
      </label>
      <input
        type="range"
        min="80"
        max="120"
        value="100"
        class="range range-accent"
        id="base300-slider"
        oninput="adjustBase300(this.value)"
      />
    </div>

    <!-- Reset Button -->
    <div class="card-actions justify-end">
      <button class="btn btn-ghost btn-sm" onclick="resetColors()">Reset to Defaults</button>
      <button class="btn btn-primary btn-sm" onclick="saveColors()">Save Changes</button>
    </div>
  </div>
</div>

<script>
function adjustBase100(value) {
  const percentage = value / 100;
  document.documentElement.style.setProperty('--base-100-adjust', percentage);
  document.getElementById('base100-value').textContent = `${value}%`;

  // Update CSS custom property
  const root = getComputedStyle(document.documentElement);
  const baseColor = root.getPropertyValue('--bc');
  document.documentElement.style.setProperty(
    '--bc',
    `oklch(${percentage * 100}% 0 0)`
  );
}

function adjustBase200(value) {
  const percentage = value / 100;
  document.documentElement.style.setProperty('--base-200-adjust', percentage);
  document.getElementById('base200-value').textContent = `${value}%`;
}

function adjustBase300(value) {
  const percentage = value / 100;
  document.documentElement.style.setProperty('--base-300-adjust', percentage);
  document.getElementById('base300-value').textContent = `${value}%`;
}

function resetColors() {
  // Reset all sliders
  ['base100', 'base200', 'base300'].forEach(base => {
    const slider = document.getElementById(`${base}-slider`);
    slider.value = 100;
    document.getElementById(`${base}-value`).textContent = '100%';
    document.documentElement.style.removeProperty(`--${base}-adjust`);
  });

  showToast('Colors reset to defaults', 'info');
}

function saveColors() {
  const settings = {
    base100: document.getElementById('base100-slider').value,
    base200: document.getElementById('base200-slider').value,
    base300: document.getElementById('base300-slider').value
  };

  localStorage.setItem('color-adjustments', JSON.stringify(settings));
  showToast('Color settings saved', 'success');
}

// Load saved colors on page load
document.addEventListener('DOMContentLoaded', () => {
  const saved = localStorage.getItem('color-adjustments');
  if (saved) {
    const settings = JSON.parse(saved);
    if (settings.base100) adjustBase100(settings.base100);
    if (settings.base200) adjustBase200(settings.base200);
    if (settings.base300) adjustBase300(settings.base300);
  }
});
</script>
```

---

### 12.3 Brightness Adjustment Controls

Users MUST be able to adjust brightness separately for light and dark themes to address accessibility needs.

**Brightness Control Requirements:**
- Separate sliders for light theme and dark theme
- Range: 50-150% (default: 100%)
- Real-time preview
- WCAG contrast validation warnings
- Reset to defaults option

**Implementation Example:**

```html
<!-- Brightness Control Panel -->
<div class="collapse collapse-arrow bg-base-200">
  <input type="checkbox" />
  <div class="collapse-title text-xl font-medium">
    Brightness Settings
  </div>
  <div class="collapse-content">
    <!-- Light Theme Brightness -->
    <div class="form-control">
      <label class="label">
        <span class="label-text">Light Theme Brightness</span>
        <span class="label-text-alt" id="light-brightness-value">100%</span>
      </label>
      <input
        type="range"
        min="50"
        max="150"
        value="100"
        class="range"
        step="5"
        id="light-brightness-slider"
        oninput="adjustLightBrightness(this.value)"
      />
      <div class="w-full flex justify-between text-xs px-2">
        <span>50%</span>
        <span>100%</span>
        <span>150%</span>
      </div>
    </div>

    <!-- Dark Theme Brightness -->
    <div class="form-control mt-4">
      <label class="label">
        <span class="label-text">Dark Theme Brightness</span>
        <span class="label-text-alt" id="dark-brightness-value">100%</span>
      </label>
      <input
        type="range"
        min="50"
        max="150"
        value="100"
        class="range range-primary"
        step="5"
        id="dark-brightness-slider"
        oninput="adjustDarkBrightness(this.value)"
      />
      <div class="w-full flex justify-between text-xs px-2">
        <span>50%</span>
        <span>100%</span>
        <span>150%</span>
      </div>
    </div>

    <!-- Contrast Warning -->
    <div id="brightness-warning" class="alert alert-warning mt-4 hidden">
      <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
      </svg>
      <span>Your brightness settings may reduce text readability. Consider adjusting for better contrast.</span>
    </div>

    <!-- Actions -->
    <div class="flex gap-2 mt-4">
      <button class="btn btn-ghost btn-sm flex-1" onclick="resetBrightness()">Reset</button>
      <button class="btn btn-primary btn-sm flex-1" onclick="saveBrightness()">Save</button>
    </div>
  </div>
</div>

<script>
function adjustLightBrightness(value) {
  const brightness = value / 100;
  document.getElementById('light-brightness-value').textContent = `${value}%`;

  // Apply CSS filter for light theme
  if (document.documentElement.getAttribute('data-theme') === 'light') {
    document.documentElement.style.filter = `brightness(${brightness})`;
  }

  // Store for later application
  localStorage.setItem('light-brightness', value);

  // Validate contrast
  validateBrightnessContrast(value);
}

function adjustDarkBrightness(value) {
  const brightness = value / 100;
  document.getElementById('dark-brightness-value').textContent = `${value}%`;

  // Apply CSS filter for dark theme
  if (document.documentElement.getAttribute('data-theme') === 'dark') {
    document.documentElement.style.filter = `brightness(${brightness})`;
  }

  // Store for later application
  localStorage.setItem('dark-brightness', value);

  // Validate contrast
  validateBrightnessContrast(value);
}

function validateBrightnessContrast(value) {
  const warning = document.getElementById('brightness-warning');

  // Show warning if brightness is too low or too high
  if (value < 70 || value > 130) {
    warning.classList.remove('hidden');
  } else {
    warning.classList.add('hidden');
  }
}

function resetBrightness() {
  document.getElementById('light-brightness-slider').value = 100;
  document.getElementById('dark-brightness-slider').value = 100;
  adjustLightBrightness(100);
  adjustDarkBrightness(100);

  showToast('Brightness reset to defaults', 'info');
}

function saveBrightness() {
  const lightValue = document.getElementById('light-brightness-slider').value;
  const darkValue = document.getElementById('dark-brightness-slider').value;

  localStorage.setItem('light-brightness', lightValue);
  localStorage.setItem('dark-brightness', darkValue);

  showToast('Brightness settings saved', 'success');
}

// Apply saved brightness on page load and theme change
function applyBrightness() {
  const currentTheme = document.documentElement.getAttribute('data-theme');
  const lightBrightness = localStorage.getItem('light-brightness') || 100;
  const darkBrightness = localStorage.getItem('dark-brightness') || 100;

  if (currentTheme === 'light') {
    document.documentElement.style.filter = `brightness(${lightBrightness / 100})`;
  } else if (currentTheme === 'dark') {
    document.documentElement.style.filter = `brightness(${darkBrightness / 100})`;
  }
}

// Apply on load
document.addEventListener('DOMContentLoaded', applyBrightness);

// Reapply when theme changes
const observer = new MutationObserver((mutations) => {
  mutations.forEach((mutation) => {
    if (mutation.attributeName === 'data-theme') {
      applyBrightness();
    }
  });
});

observer.observe(document.documentElement, { attributes: true });
</script>
```

---

### 12.4 Complete Customization Settings Page

**Full-featured Settings Component:**

```html
<!-- Complete User Customization Panel -->
<div class="container mx-auto p-4 max-w-4xl">
  <h1 class="text-3xl font-bold mb-6">Appearance Settings</h1>

  <div class="space-y-6">
    <!-- Theme Selection -->
    <div class="card bg-base-100 shadow-xl">
      <div class="card-body">
        <h2 class="card-title">Theme</h2>
        <div class="form-control">
          <label class="label">
            <span class="label-text">Select your preferred theme</span>
          </label>
          <select id="theme-selector" class="select select-bordered w-full max-w-xs">
            <option value="light">Light</option>
            <option value="dark">Dark</option>
            <option value="corporate">Corporate</option>
            <option value="cyberpunk">Cyberpunk</option>
            <option value="synthwave">Synthwave</option>
            <option value="retro">Retro</option>
            <option value="valentine">Valentine</option>
            <option value="aqua">Aqua</option>
          </select>
        </div>

        <!-- Theme Preview -->
        <div class="mockup-window border bg-base-300 mt-4">
          <div class="flex justify-center px-4 py-16 bg-base-200">
            <div class="space-x-2">
              <button class="btn btn-primary">Primary</button>
              <button class="btn btn-secondary">Secondary</button>
              <button class="btn btn-accent">Accent</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Brightness Controls -->
    <div class="card bg-base-100 shadow-xl">
      <div class="card-body">
        <h2 class="card-title">Brightness</h2>

        <!-- Light Theme -->
        <div class="form-control">
          <label class="label">
            <span class="label-text">Light Theme Brightness</span>
            <span class="label-text-alt badge badge-neutral" id="light-brightness-display">100%</span>
          </label>
          <input
            type="range"
            min="50"
            max="150"
            value="100"
            class="range range-primary"
            step="5"
            id="light-brightness"
          />
        </div>

        <!-- Dark Theme -->
        <div class="form-control mt-4">
          <label class="label">
            <span class="label-text">Dark Theme Brightness</span>
            <span class="label-text-alt badge badge-neutral" id="dark-brightness-display">100%</span>
          </label>
          <input
            type="range"
            min="50"
            max="150"
            value="100"
            class="range range-secondary"
            step="5"
            id="dark-brightness"
          />
        </div>
      </div>
    </div>

    <!-- Advanced Color Adjustments -->
    <div class="card bg-base-100 shadow-xl">
      <div class="card-body">
        <h2 class="card-title">Advanced Color Adjustments</h2>

        <div class="alert alert-info">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="stroke-current shrink-0 w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
          </svg>
          <span>These settings affect all themes. Adjust carefully to maintain readability.</span>
        </div>

        <!-- Color Adjustments (from 12.2) -->
        <div class="space-y-4 mt-4">
          <div class="form-control">
            <label class="label">
              <span class="label-text">Background Lightness</span>
              <span class="label-text-alt badge" id="base100-display">100%</span>
            </label>
            <input type="range" min="80" max="120" value="100" class="range" id="base100-adjust" />
          </div>

          <div class="form-control">
            <label class="label">
              <span class="label-text">Secondary Background</span>
              <span class="label-text-alt badge" id="base200-display">100%</span>
            </label>
            <input type="range" min="80" max="120" value="100" class="range" id="base200-adjust" />
          </div>

          <div class="form-control">
            <label class="label">
              <span class="label-text">Border Intensity</span>
              <span class="label-text-alt badge" id="base300-display">100%</span>
            </label>
            <input type="range" min="80" max="120" value="100" class="range" id="base300-adjust" />
          </div>
        </div>
      </div>
    </div>

    <!-- Actions -->
    <div class="card bg-base-100 shadow-xl">
      <div class="card-body">
        <div class="flex gap-2 justify-end">
          <button class="btn btn-ghost" onclick="resetAllSettings()">Reset All</button>
          <button class="btn btn-error" onclick="clearAllSettings()">Clear Saved Settings</button>
          <button class="btn btn-primary" onclick="saveAllSettings()">Save All Settings</button>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
// Comprehensive settings management
const SettingsManager = {
  init() {
    this.loadSettings();
    this.attachEventListeners();
  },

  attachEventListeners() {
    document.getElementById('theme-selector').addEventListener('change', (e) => {
      this.changeTheme(e.target.value);
    });

    ['light-brightness', 'dark-brightness', 'base100-adjust', 'base200-adjust', 'base300-adjust'].forEach(id => {
      document.getElementById(id).addEventListener('input', (e) => {
        this.updateDisplay(id, e.target.value);
      });
    });
  },

  loadSettings() {
    const theme = localStorage.getItem('user-theme') || 'light';
    const lightBright = localStorage.getItem('light-brightness') || 100;
    const darkBright = localStorage.getItem('dark-brightness') || 100;
    const colorSettings = JSON.parse(localStorage.getItem('color-adjustments') || '{}');

    document.getElementById('theme-selector').value = theme;
    document.getElementById('light-brightness').value = lightBright;
    document.getElementById('dark-brightness').value = darkBright;

    if (colorSettings.base100) document.getElementById('base100-adjust').value = colorSettings.base100;
    if (colorSettings.base200) document.getElementById('base200-adjust').value = colorSettings.base200;
    if (colorSettings.base300) document.getElementById('base300-adjust').value = colorSettings.base300;

    this.applySettings();
  },

  changeTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
  },

  updateDisplay(id, value) {
    const displayId = id.replace('-adjust', '').replace('-brightness', '-brightness') + '-display';
    document.getElementById(displayId).textContent = `${value}%`;
  },

  applySettings() {
    const theme = document.getElementById('theme-selector').value;
    this.changeTheme(theme);
    // Apply brightness and color adjustments...
  },

  saveAllSettings() {
    const settings = {
      theme: document.getElementById('theme-selector').value,
      lightBrightness: document.getElementById('light-brightness').value,
      darkBrightness: document.getElementById('dark-brightness').value,
      colorAdjustments: {
        base100: document.getElementById('base100-adjust').value,
        base200: document.getElementById('base200-adjust').value,
        base300: document.getElementById('base300-adjust').value
      }
    };

    localStorage.setItem('user-theme', settings.theme);
    localStorage.setItem('light-brightness', settings.lightBrightness);
    localStorage.setItem('dark-brightness', settings.darkBrightness);
    localStorage.setItem('color-adjustments', JSON.stringify(settings.colorAdjustments));

    showToast('All settings saved successfully', 'success');
  },

  resetAllSettings() {
    document.getElementById('theme-selector').value = 'light';
    document.getElementById('light-brightness').value = 100;
    document.getElementById('dark-brightness').value = 100;
    document.getElementById('base100-adjust').value = 100;
    document.getElementById('base200-adjust').value = 100;
    document.getElementById('base300-adjust').value = 100;

    this.applySettings();
    showToast('Settings reset to defaults', 'info');
  },

  clearAllSettings() {
    ['user-theme', 'light-brightness', 'dark-brightness', 'color-adjustments'].forEach(key => {
      localStorage.removeItem(key);
    });

    this.resetAllSettings();
    showToast('All saved settings cleared', 'warning');
  }
};

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
  SettingsManager.init();
});

// Toast helper
function showToast(message, type) {
  const alert = document.createElement('div');
  alert.className = `alert alert-${type} shadow-lg fixed bottom-4 right-4 w-96 z-50`;
  alert.innerHTML = `<span>${message}</span>`;
  document.body.appendChild(alert);
  setTimeout(() => alert.remove(), 3000);
}
</script>
```

---

### 12.5 Server Sync Implementation (Optional)

For cross-device preference synchronization:

```javascript
// Server API sync functions
async function syncThemeToServer(settings) {
  try {
    const response = await fetch('/api/user/preferences', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${getUserToken()}`
      },
      body: JSON.stringify({
        theme: settings.theme,
        brightness: {
          light: settings.lightBrightness,
          dark: settings.darkBrightness
        },
        colors: settings.colorAdjustments
      })
    });

    if (!response.ok) throw new Error('Sync failed');

    showToast('Settings synced to cloud', 'success');
  } catch (error) {
    console.error('Sync error:', error);
    showToast('Failed to sync settings', 'error');
  }
}

async function loadSettingsFromServer() {
  try {
    const response = await fetch('/api/user/preferences', {
      headers: {
        'Authorization': `Bearer ${getUserToken()}`
      }
    });

    if (!response.ok) throw new Error('Load failed');

    const settings = await response.json();

    // Apply server settings
    if (settings.theme) {
      localStorage.setItem('user-theme', settings.theme);
    }
    if (settings.brightness) {
      localStorage.setItem('light-brightness', settings.brightness.light);
      localStorage.setItem('dark-brightness', settings.brightness.dark);
    }
    if (settings.colors) {
      localStorage.setItem('color-adjustments', JSON.stringify(settings.colors));
    }

    SettingsManager.loadSettings();
    showToast('Settings loaded from cloud', 'success');
  } catch (error) {
    console.error('Load error:', error);
    // Fall back to localStorage
  }
}
```

---

### 12.6 Accessibility Requirements for Customization UI

All customization interfaces MUST meet these requirements:

1. **Keyboard Navigation:**
   - All controls accessible via Tab key
   - Enter/Space to activate buttons
   - Arrow keys for slider adjustment

2. **Screen Reader Support:**
   - ARIA labels on all inputs
   - Live region announcements for changes
   - Descriptive button text

3. **Visual Feedback:**
   - Real-time preview of changes
   - Clear focus indicators
   - Loading states for async operations

4. **Touch-Friendly:**
   - Minimum 44x44px touch targets
   - Adequate spacing between controls
   - Swipe gestures for theme switching

5. **Error Handling:**
   - Clear error messages
   - Recovery suggestions
   - Automatic fallback to defaults

**Example ARIA Implementation:**

```html
<div role="region" aria-labelledby="settings-heading">
  <h2 id="settings-heading">Appearance Settings</h2>

  <label for="theme-selector">
    <span class="label-text">Theme Selection</span>
  </label>
  <select
    id="theme-selector"
    aria-describedby="theme-help"
    class="select select-bordered"
  >
    <!-- options -->
  </select>
  <span id="theme-help" class="sr-only">
    Choose a visual theme for the application interface
  </span>

  <label for="brightness-slider">
    <span class="label-text">Brightness</span>
  </label>
  <input
    type="range"
    id="brightness-slider"
    aria-valuemin="50"
    aria-valuemax="150"
    aria-valuenow="100"
    aria-valuetext="100 percent brightness"
    class="range"
  />

  <!-- Live region for changes -->
  <div
    role="status"
    aria-live="polite"
    aria-atomic="true"
    class="sr-only"
    id="settings-status"
  >
    <!-- Dynamic announcements -->
  </div>
</div>
```

---

## 13. References

- DaisyUI Documentation: https://daisyui.com/docs/themes/
- DaisyUI Theme Generator: https://daisyui.com/theme-generator/
- Tailwind v4 Color System: https://tailwindcss.com/docs/customizing-colors
- WCAG Color Contrast: https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html
- CSS Filter Effects: https://developer.mozilla.org/en-US/docs/Web/CSS/filter
- Web Storage API: https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API
- ARIA Authoring Practices: https://www.w3.org/WAI/ARIA/apg/

---

**Last Updated:** 2025-12-01
**Version:** 1.2.0 (Added Comprehensive User Customization Implementation Guide)
**Status:** MANDATORY
