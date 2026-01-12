# OpenAPI → UI Model Conversion Rules

## Purpose
These rules define how the UI Factory interprets an OpenAPI spec and produces a complete UI schema describing pages, routes, sections, components, layouts, responsive behaviour, and data interactions. This is the canonical mapping logic the LLMs and generator engine must follow.

---

# 1. High‑Level Overview
An OpenAPI document is transformed through three deterministic phases:

### Phase 1 — **Extract**
Parse OpenAPI and extract:
- Endpoints (grouped by tags)
- Operations (GET/POST/PUT/PATCH/DELETE)
- Request schemas
- Response schemas
- Parameters (query, path, header)
- Security requirements

### Phase 2 — **Interpret**
Apply UI heuristics to determine:
- Page types (index, list, detail, form, dashboard)
- Primary + secondary user actions
- Data relationships
- Required UI components

### Phase 3 — **Generate UI Model**
Output a fully structured UI definition describing:
- Pages
- Routes
- Layout containers (grid, table, cards, list, accordion)
- Sections
- Component blueprints
- Bindings
- Responsive rules
- Behaviour rules

This model is then used by the **React generator** *or* **HTMX/Jinja generator**.

---

# 2. Tag → Page Mapping Rules
Tags are treated as **logical modules**.

### If no tag exists:
- Group endpoints by **first path segment**.

### For each tag/module:
Create:
- `{tag}/index` page → listing
- `{tag}/create` page → form (if POST exists)
- `{tag}/details` page → detail view (if GET by ID exists)
- `{tag}/edit` page → form (if PUT/PATCH exists)

---

# 3. Operation → Page Type Rules
### GET collection → **List Page**
Used when response schema contains:
- `type: array`
- or `results/items` fields

Default component:
- `table` (desktop)
- auto‑convert to `cards` (tablet)
- auto‑convert to `list` (mobile)

### GET single → **Detail Page**
Response object fields become:
- key/value blocks
- accordions for nested objects
- tabs for long or complex objects

### POST → **Create Form**
Request body schema → input components.

### PUT/PATCH → **Edit Form**
Same rules as create, but prefilled.

### DELETE → **Delete Action**
Attached to:
- table row
- card
- detail header

---

# 4. Schema → UI Component Rules
### Primitive Fields
| OpenAPI Type | UI Component |
|--------------|--------------|
| string | text field |
| string (format: email) | email field |
| string (format: date) | date picker |
| string (format: uri) | link field |
| number / integer | number field |
| boolean | toggle switch |

### Enums
→ dropdown, segmented control, or radio group depending on `enum.length`.

### Arrays
- Arrays of primitives → tag list input
- Arrays of objects → nested table or repeated card component

### Objects
Nested object →
- Accordion
- or collapsible section
- or tab group if top‑level nested objects > 3

---

# 5. Layout Mapping Rules
Each page gets a layout container depending on content.

### List Page
- desktop: `table`
- tablet: `cards`
- mobile: `list`

### Detail Page
- top summary block
- 1–4 metadata grids (auto‑generated)
- accordions for nested structures

### Form Page
- one or more `formSections`
- responsive 1–3 column layout based on screen size

---

# 6. Action Mapping Rules
Each operation generates UI actions.

### GET
No action; fetch and display.

### POST
- primary action: `Create`
- optional secondary: `Cancel`

### PUT/PATCH
- primary: `Save`
- secondary: `Cancel`

### DELETE
- destructive button
- requires confirmation modal
- auto‑generates semantic red UI tokens

---

# 7. Routing Rules
Routes follow consistent patterns:
```
/{tag} → list
/{tag}/create → create form
/{tag}/{id} → detail page
/{tag}/{id}/edit → edit form
```

ID field is inferred as:
- `id`
- or first required path parameter

---

# 8. Responsive Rules
Use layout tokens and rules from the global design system.

### Table → Cards → List
If viewport < `md` → convert table to cards.
If viewport < `sm` → convert cards to list.

### Form
- desktop: two/three columns
- tablet: two columns
- mobile: single column

### Detail
- desktop: multi‑column summary grids
- mobile: stacked accordions

---

# 9. Behaviour Rules
### Pagination
Auto‑enabled if GET response contains:
- `page`, `limit`, `offset`, `total`

### Searching
Auto‑enabled if query parameters contain fields:
- `q`, `search`, `keyword`

### Filtering
Generated from query parameters with enums.

### Sorting
Enabled for numeric or string fields in tables.

---

# 10. Security Rules
If operation lists `security` requirements:
- add protected route flag
- generate login-required wrapper

---

# 11. Final Output Shape
The UI model is exported as structured JSON:
```json
{
  "pages": [
    {
      "route": "/pets",
      "type": "list",
      "layout": "table",
      "components": [...],
      "actions": [...],
      "responsive": {...},
      "data": {...}
    }
  ]
}
```
This is consumed by the generators (React or HTMX/Jinja2).

---

# End of Document

