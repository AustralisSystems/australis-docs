# Design System Foundations

*(Full dual-mode: Designer principles + Developer implementation)*

## 1. Overview & Philosophy
Design evolves, tools change, but foundational principles remain constant. This system defines universal rules for shadows, depth, responsiveness, colour systems, layout structure, and semantic meaning.

### Purpose
This document serves as:
- **Entry point** - First document to read for understanding the system
- **Quick reference** - Fast lookup for core principles
- **Prompt library** - LLM instruction templates
- **Compliance checklist** - Enforcement rules for validation
- **Index document** - Links to all detailed specifications

### Related Specifications
For detailed implementation guidance, refer to these companion documents:

- **[layout_tokens.json](layout_tokens.json)** - Concrete token values (spacing, colors, shadows, typography, motion)
- **[component_tokens.json](component_tokens.json)** - Component-specific design tokens
- **[responsive_layout_principles.md](responsive_layout_principles.md)** - Deep dive into responsive design (15 core principles)
- **[responsive_layout_developer_workflow.md](responsive_layout_developer_workflow.md)** - Step-by-step implementation workflow
- **[motion_transition_spec.md](motion_transition_spec.md)** - Animation timing, easing, and transition patterns
- **[figma_guideline_deck.md](figma_guideline_deck.md)** - Visual presentation for stakeholder communication
- **[mcp_ui_factory_protocol.md](mcp_ui_factory_protocol.md)** - System integration and orchestration protocol
- **[openapi_ui_model_conversion_rules.md](openapi_ui_model_conversion_rules.md)** - OpenAPI to UI Model transformation rules
- **[universal_component_mapping_protocol.md](universal_component_mapping_protocol.md)** - Component selection and mapping logic
- **[renderer_mapping_spec.md](renderer_mapping_spec.md)** - React and HTMX/Jinja2 rendering specifications
- **[tailwind_generator_template.js](tailwind_generator_template.js)** - Tailwind configuration generator

---

## 2. Core Principles

### 2.1 Shadows & Depth
Shadows define hierarchy, realism, and structure. Use colour layering and dual-shadow systems.

#### Colour Layering
- Create 3–4 tonal variations of each base colour.
- Darker shades in the background; lighter shades at the front.
- Avoid borders by relying on tonal contrast.

#### Dual-Shadow System
- Combine light top shadow with darker bottom shadow.
- Three elevation levels: small, medium, large.
- Maintain consistent top-down lighting.

#### Gradients
- Use subtle linear gradients with soft inner shadows.
- Effective especially in dark mode.

---

### 2.2 Responsiveness & Layout
Responsive design is about rearrangement, not shrinking.

#### Systems of Boxes
- All layouts are structured using nested boxes.
- Maintain parent–child relationships.
- Use grids or flex systems.

#### Purposeful Rearrangement
- Prioritise elements based on importance.
- Avoid squished components; allow reflow.
- Use carousels or stacked layouts where needed.

---

### 2.3 Colour Systems
Colours communicate hierarchy, focus, emotion, and state.

#### Palette Roles
- **Primary**: CTAs, action anchors.
- **Secondary**: Supporting actions.
- **Neutral**: Backgrounds, surfaces, typography.
- **Semantic**: Success, warning, info, error.

#### Usage Guidelines
- Use neutrals for structure.
- Use saturated colours sparingly.
- Semantic colours must match meaning.

---

## 3. Developer Implementation

### 3.1 Colour Tokens
Define colour palettes as structured tokens:
```
colors.primary.DEFAULT
colors.secondary.DEFAULT
colors.neutral.100–900
colors.semantic.success
colors.semantic.error
```

### 3.2 Shadow Tokens
```
shadow.sm
shadow.md
shadow.lg
```

### 3.3 Spacing System
Use an 8pt scale mapped to utility classes.

### 3.4 Typography
Use modular scales with 400–700 weights.

---

## 4. AI & Automation Prompts
### Shadows Prompt
"Apply dual shadows, tonal layering, and subtle gradients. Avoid borders. Maintain top-down lighting."

### Responsive Prompt
"Rearrange elements by priority at breakpoints. Preserve hierarchy. Avoid shrinking components."

### Colour System Prompt
"Use primary for CTAs, secondary for accents, neutral for structure, semantic for state. Maintain contrast."

---

## 5. Enforcement Rules
- All components must use design tokens.
- Semantic colours must align to meaning.
- Shadows must use the defined dual-shadow system.
- Responsive layouts must be tested at three breakpoints.
- Typography must follow the modular scale.

---

## 6. Closing Principle
Design is communication through hierarchy, rhythm, and clarity. Consistency creates craftsmanship.
