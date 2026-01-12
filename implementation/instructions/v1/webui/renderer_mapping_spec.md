# Renderer Mapping Specification (React & HTMX/Jinja2)

## Purpose
This specification defines how **logical UCMP components** map to concrete implementations in:
- **React + Tailwind (TSX)**
- **HTMX + Jinja2 + Tailwind**

This ensures:
- deterministic cross-renderer behaviour
- interchangeable UI generation
- consistent responsive behaviour
- dual-token primary/secondary rendering
- unified naming + directory conventions

---

# 1. Core Principles

### 1.1 Logical Components First
Mapping always begins with a UCMP logical component:
```
component: "text_field"
primaryToken: "text_field_primary"
secondaryToken: "text_field_secondary"
props: {...}
```

### 1.2 Renderer-Agnostic → Renderer-Specific
The mapping layer must:
1. **read logical component**
2. determine renderer target
3. select React or Jinja2/HTMX implementation
4. apply Tailwind classes from tokens
5. inject motion tokens when applicable

### 1.3 Dual Token Enforcement
Each mapping must use:
- **primary token** for desktop/tablet
- **secondary token** for mobile/compact modes

### 1.4 Naming Consistency
Logical → React → Jinja2 naming must follow:
```
text_field → TextField → text_field()
select → Select → select()
cardlist → CardList → cardlist()
```

---

# 2. Directory Structure

## 2.1 React Structure
```
src/
  components/
    forms/
    display/
    layout/
  pages/
  hooks/
  utils/
```

## 2.2 HTMX + Jinja2 Structure
```
templates/
  pages/
  components/
    forms.html
    display.html
    layout.html
macros/
  forms.jinja
  display.jinja
  layout.jinja
static/
  js/
  css/
```

---

# 3. Logical → React Mapping
Each component maps to a TSX implementation with Tailwind styling.

## 3.1 Text Field
### Primary Token → Elevated/standard density
```tsx
<TextField
  label={label}
  name={name}
  required={required}
  maxLength={maxLength}
  className="input input-bordered w-full"
/>
```

### Secondary Token → Compact/flat
```tsx
<TextField
  label={label}
  name={name}
  className="input input-sm input-bordered w-full bg-base-200"
/>
```

---

## 3.2 Select Dropdown
### Primary
```tsx
<Select
  name={name}
  options={options}
  className="select select-bordered w-full"
/>
```

### Secondary (searchable)
```tsx
<SearchableSelect
  name={name}
  options={options}
  className="select select-sm select-bordered w-full bg-base-200"
/>
```

---

## 3.3 Boolean
Primary = toggle
```tsx
<Toggle name={name} />
```
Secondary = checkbox
```tsx
<Checkbox name={name} />
```

---

## 3.4 Table
Primary
```tsx
<Table columns={columns} data={data} />
```

Secondary (mobile collapsible rows)
```tsx
<MobileList data={data} />
```

---

## 3.5 Cardlist
Primary
```tsx
<CardList items={items} variant="elevated" />
```
Secondary
```tsx
<CardList items={items} variant="bordered" />
```

---

# 4. Logical → HTMX + Jinja2 Mapping
Mapping rules transform logical components into Jinja macros + HTMX interactions.

## 4.1 Text Field
### Primary
```jinja
{{ text_field(label, name, required=required, maxlength=maxLength, class="input input-bordered w-full") }}
```

### Secondary
```jinja
{{ text_field(label, name, class="input input-sm input-bordered w-full bg-base-200") }}
```

---

## 4.2 Select Dropdown
### Primary
```jinja
{{ select(name, options, class="select select-bordered w-full") }}
```

### Secondary
```jinja
{{ searchable_select(name, options, class="select select-sm select-bordered w-full bg-base-200") }}
```

---

## 4.3 Boolean
Primary (toggle)
```jinja
{{ toggle(name) }}
```
Secondary (checkbox)
```jinja
{{ checkbox(name) }}
```

---

## 4.4 Table
Primary
```jinja
{{ table(columns, data) }}
```

Secondary (collapsible mobile list)
```jinja
{{ mobile_list(data) }}
```

---

## 4.5 Cardlist
Primary
```jinja
{{ cardlist(items, variant="elevated") }}
```
Secondary
```jinja
{{ cardlist(items, variant="bordered") }}
```

---

# 5. HTMX Interaction Rules
Each logical component can extend via HTMX:

## 5.1 Submit-on-change
```html
hx-post="/api/update"
hx-trigger="change"
hx-target="#container"
```

## 5.2 Live Search for Select
```html
hx-get="/api/search"
hx-trigger="input changed delay:300ms"
hx-target="#results"
hx-swap="outerHTML"
```

## 5.3 Table Pagination
```html
hx-get="/api/list?page={{ page }}"
hx-trigger="click"
hx-target="#table"
```

---

# 6. Responsive Token Behaviour

Primary vs Secondary selection depends on screen size:
```
if width < sm → use secondary
if width < md → use secondary for heavy components (table/cardlist)
else → primary
```

This logic must be embedded inside:
- React hooks (`useResponsiveTokens()`)
- Jinja wrapper macros (`apply_responsive()`)

---

# 7. Motion Mapping
Each renderer must apply:
- fade transitions for form fields
- slide transitions for accordions
- opacity + translate transitions for cards
- table row expansion animations

Tailwind motion tokens map to:
- `transition-all duration-{token} ease-{token}` in React
- same classes in Jinja2 templates

---

# 8. Error Handling
If a logical component has no renderer mapping:
1. log error
2. fallback to `text_field_secondary`
3. attach warning to build artefacts

---

# End of Specification
