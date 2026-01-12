# Motion & Transitions System Specification

## 1. Purpose
This specification defines the motion, animation, and interaction behaviour for all UI components produced by the UI Factory (React, HTMX, Jinja2). It provides a unified language and rule set so that all generated pages feel coherent and consistent.

It builds directly on top of layout.tokens.json and uses only values and patterns declared in the token set.

---

## 2. Core Principles

### 2.1 Motion must communicate meaning
Animations must:
- Clarify spatial relationships.
- Show hierarchy (parent → child → detail).
- Reinforce state changes (open, close, load, reorder).
- Reduce cognitive load.

### 2.2 Motion should be subtle and responsive
Use motion to enhance, never distract. All motion must:
- Stay under three hundred milliseconds unless explicitly marked as long-form.
- Adjust for device scale (mobile reduces distances and duration).
- Respect user reduced-motion preferences.

### 2.3 All transitions are stateful and reversible
Every animated state must have a matching reverse state:
- expand ↔ collapse
- enter ↔ exit
- focus ↔ blur
- active ↔ idle

### 2.4 All interactions use token-based durations and easing
All implementations (React, Alpine/HTMX, plain CSS, Jinja2 templates) must use token values:
- durations.xxx
- easing.xxx
- motion.xxx patterns

---

## 3. Duration Tokens (reference only)
Key durations to be used in components:
- Instant: fifty milliseconds
- Fast: one hundred and fifty milliseconds
- Medium: two hundred milliseconds
- Slow: three hundred milliseconds
- Long: four hundred milliseconds (avoid unless required)

---

## 4. Easing Tokens (reference only)
- ease.standard (two five zero, zero, two zero five, one)
- ease.accelerate (three three oh, zero, one, one)
- ease.decelerate (zero, zero, zero, one)
- ease.emphasised (four five oh, zero five, two oh five, one)

---

## 5. Motion Patterns
### 5.1 Fade
Used for subtle appearance or disappearance:
- Fade in: opacity zero → one using durations.fast and ease.decelerate.
- Fade out: opacity one → zero using durations.fast and ease.accelerate.

### 5.2 Scale
Used for modals, cards, tiles:
- scale.zero point nine → one for emphasised entry.
- scale.one → zero point nine for exit.

### 5.3 Slide
Directional context change:
- slideUp: translateY one rem → zero.
- slideDown: translateY minus one rem → zero.
- slideLeft/slideRight: translateX one rem → zero.

### 5.4 Collapse / Expand
Accordion, nav groups, tables switching to card mode:
- max-height: zero → auto, duration medium, easing standard.
- opacity: zero point five → one.

### 5.5 Shared Element Transitions
When switching between layout modes:
- Containers morph by resizing smoothly.
- Content fades between views.
- Primary element maintains origin when possible.

### 5.6 Loading State Animations
Indicating asynchronous operations:
- **Spinner:** Continuous rotate (360deg, duration 800ms, linear)
- **Skeleton:** Pulse opacity 0.5 ↔ 1.0 (duration 1500ms, ease-in-out)
- **Progress Bar:** Width 0% → 100% (duration variable, ease-standard)
- **Dots Loader:** Sequential fade + scale (stagger 150ms per dot)

### 5.7 Error State Animations
Drawing attention to validation failures:
- **Shake:** TranslateX oscillation: 0 → -10px → 10px → -5px → 5px → 0 (duration 400ms)
- **Pulse Border:** Border color flash red with opacity pulse (2 cycles, 300ms each)
- **Icon Entry:** Error icon scales in with bounce (scale 0 → 1.2 → 1, duration 350ms)

### 5.8 Success State Animations
Confirming completed actions:
- **Checkmark Draw:** SVG path stroke-dashoffset animation (duration 400ms, ease-decelerate)
- **Pulse Success:** Scale 1 → 1.1 → 1 with green glow (duration 500ms, ease-emphasised)
- **Toast Slide-In:** SlideDown + Fade (from top, duration 250ms, ease-decelerate)
- **Confetti Burst:** (Optional, for critical success) Particles with gravity physics

---

## 6. Behavioural Motion Rules
### 6.1 Layout Transitions
The UI factory will generate transitions for:
- Table → Grid
- Grid → Cards
- Cards → List
- List → Accordion
- Any → Carousel

Transitions use the official motion patterns defined in the token file.

### 6.2 Component Micro-interactions
Every interactive element must include:
- Hover lift (shadow elevation increase).
- Active press (scale zero point nine five).
- Focus ring fade-in (duration fast).

### 6.3 Page-level Motion Events
- Page enter: fade + slideUp (duration medium).
- Page exit: fade out (duration fast).
- Modal open: fade + scale (duration medium).
- Modal close: fade + scale down (duration fast).

### 6.4 Animation Chaining & Sequencing
When multiple animations occur simultaneously or sequentially:

**Parallel Animations (Same Element):**
- Combine compatible properties: opacity + transform (allowed)
- Avoid conflicting transforms: scale + rotate + translate (use single transform property)
- Maximum 3 simultaneous animations per element

**Sequential Animations (Staggered Elements):**
- **List Items:** Stagger by 50ms per item (max 10 items, then instant)
- **Card Grid:** Stagger by row (100ms delay per row)
- **Form Fields:** Validate sequentially with 80ms stagger
- **Navigation Items:** Cascade from top (60ms per item)

**Timing Priority:**
1. User interaction feedback (immediate)
2. Layout shifts (within 100ms)
3. Content loading (background)
4. Decorative animations (lowest priority, can be skipped)

**Interruption Rules:**
- User interactions interrupt decorative animations immediately
- Cancel pending animations in queue if new interaction detected
- Critical state changes (error/success) interrupt non-critical animations

### 6.5 Z-Index Management During Transitions
Prevents visual glitches during animated state changes:

**Z-Index Layers (Ascending Order):**
```
0   - Base content layer
10  - Elevated cards/buttons (hover state)
100 - Dropdown menus, popovers
500 - Modal backdrop
501 - Modal content
1000 - Toasts, notifications
9999 - Critical alerts, force-foreground elements
```

**Transition-Specific Rules:**
- **During Shared Element Transitions:** Transitioning element gets z-index: 999 (temporary)
- **Modal Opening:** Backdrop fades in first (z-500), then modal content (z-501)
- **Accordion Expand:** Expanding panel gets z-index: 11 during animation, returns to 1 on complete
- **Dropdown Menus:** Set z-index: 100 before animation starts, maintain during slide-in

**Cleanup:**
- Remove temporary z-index values on animation complete
- Use CSS animation event listeners: `animationend`, `transitionend`
- Restore to base z-index or remove inline style after 50ms grace period

---

## 7. Device-Responsive Motion
### 7.1 Mobile
- Reduce movement distances by fifty percent.
- Reduce duration by twenty percent.

### 7.2 Desktop
- Use full transforms.
- Keep durations standard.

---

## 8. Reduced Motion Mode
If user prefers reduced motion:
- Disable all transforms.
- Replace transitions with instant opacity changes.
- Use no more than fifty milliseconds for state change.

---

## 9. Implementation Requirements
### 9.1 React
- Use Framer Motion or CSS transitions based on build profile.
- All components generated by the factory must reference tokens via motion maps.

### 9.2 HTMX / Alpine
- Use CSS transitions only.
- Tokens are compiled into the Tailwind config via token importer.

### 9.3 Jinja2
- Server-rendered views rely entirely on CSS transitions.
- Motion classes provided by the Tailwind token expansion.

---

## 10. Validation Rules
- No animation exceeds four hundred milliseconds.
- All animation curves must use token easing.
- State transitions must be symmetrical.
- Motion must not obstruct or delay input.

---

## 11. Notes
This spec is intentionally neutral to brand colour, theme, or specific component definitions. Those details live inside layout.tokens.json and theme definitions.

The motion system defined here is universal across:
- React
- HTMX
- Jinja2
- mobile/desktop
- light/dark themes

It is safe to use as the canonical motion protocol for the UI factory.
