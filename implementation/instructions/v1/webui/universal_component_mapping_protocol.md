# Universal Component Mapping Protocol (UCMP)

## Purpose
The Universal Component Mapping Protocol (UCMP) defines how the UI Factory deterministically selects UI components based on data supplied through an OpenAPI specification. The protocol ensures:
- Predictable and repeatable component selection
- Stable rendering across React and HTMX/Jinja2 output targets
- Semantic awareness
- Responsive suitability
- Dual-token component strategies for variation and adaptability

This document governs *how* the mapping logic behaves, *what rules* it must follow, and *how workflows* progress during mapping.

---

# 1. Core Principles

### 1.1 Deterministic Behaviour
Any given OpenAPI property must always map to the same component type under the same conditions.

### 1.2 Dual-Token Component Architecture
Each component mapping must reference **two tokens**:
- A **primary component token** (base type)
- A **secondary component token** (variant or fallback)

This allows:
- flexible rendering across screen sizes
- theme overrides
- alternative render modes for React vs HTMX/Jinja2

### 1.3 Semantic Precedence
Semantics override raw type when deciding which component to use.
Example: A field named `email` should map to an email field even if its raw type is `string`.

### 1.4 Constraint-Aware Behaviour
Constraints such as `required`, `pattern`, `enum`, `minLength`, etc. directly influence component configuration.

### 1.5 Renderer-Agnostic Mapping
All mapping results must be expressed as **logical components**, not framework-specific code.

---

# 2. Inputs to the Mapping Engine

The mapping engine processes the following:

1. **OpenAPI Property**
2. **Inferred Type + Format**
3. **Semantic Keywords** (names, descriptions)
4. **Constraints** (limits, patterns, enum)
5. **Layout Context** (page type, container type)
6. **Component Token Registry** (dual-token definitions)
7. **Renderer Target** (React, HTMX, Jinja2)

---

# 3. The Mapping Workflow

## 3.1 Overview
The mapping workflow follows six deterministic steps:

### Step 1 — Extract Raw Metadata
Read:
- type
- format
- enum values
- constraints
- description

### Step 2 — Identify Structural Context
Determine if property is:
- primitive
- object
- array of primitives
- array of objects

### Step 3 — Apply Base Type Mapping
Map property to a **primary component token**.
Examples:
- string → text_field_primary
- boolean → toggle_primary
- integer → number_field_primary

### Step 4 — Apply Semantic Overrides
Keywords modify the mapping.
Examples:
- `email` → email_field_primary
- `password` → password_primary
- `image`, `avatar`, `photoUrl` → image_upload_primary

### Step 5 — Apply Secondary Token Logic
Each mapping must pick a **secondary token**:
- for variant components
- for mobile fallback
- for theme/density variants

Examples:
- text_field_secondary (compact)
- select_dropdown_secondary (searchable)
- card_secondary (bordered vs elevated)

### Step 6 — Apply Behaviour from Constraints
Constraints set component configuration:
- required: true
- maxLength: X
- minLength: X
- pattern: regex
- enum: list of allowed values

---

# 4. Component Token Types

Each logical component in the system must define two tokens:

## 4.1 Primary Token
The base representation of the component.
Used for: Desktop, defaults, standard density.

Examples:
- text_field_primary
- select_primary
- table_primary
- card_primary

## 4.2 Secondary Token
A variant or fallback.
Used for: Mobile, compact mode, alternative theme, simplified rendering.

Examples:
- text_field_secondary (compact)
- select_secondary (searchable)
- list_secondary (collapsible)
- accordion_secondary (bordered)

This ensures **every mapping is stable even when switching formats**.

---

# 5. Deterministic Component Selection Rules

## 5.1 Primitive Rules
| OpenAPI Type | Primary Token | Secondary Token |
|--------------|---------------|-----------------|
| string | text_field_primary | text_field_secondary |
| string + enum | select_primary | select_secondary |
| boolean | toggle_primary | checkbox_secondary |
| integer/number | number_primary | number_secondary |
| string + date | date_primary | date_secondary |
| string + datetime | datetime_primary | datetime_secondary |

---

## 5.2 Semantic Rules
These override primitive rules.

| Keyword | Primary Token | Secondary Token |
|---------|----------------|-----------------|
| email | email_primary | email_secondary |
| password | password_primary | password_secondary |
| avatar/image/photo | image_upload_primary | image_upload_secondary |
| description/notes | textarea_primary | textarea_secondary |
| status/type/state | badge_primary | badge_secondary |
| url/link | link_primary | link_secondary |

---

## 5.3 Object Mapping
Objects always map to containers first:

Primary token: `object_group_primary`
Secondary token: `object_group_secondary`

Children are then mapped recursively.

---

## 5.4 Array Mapping
### Arrays of primitives
- Primary: `taglist_primary`
- Secondary: `taglist_secondary`

### Arrays of objects
- If item contains identifiable primary key → table_primary / table_secondary
- Else → cardlist_primary / cardlist_secondary

---

# 6. Layout Context Overrides

### In List Pages
- prefer table_primary
- fallback to card_secondary on mobile

### In Detail Pages
- prefer object_group_primary
- fallback to accordion_secondary

### In Form Pages
- prefer text_field_primary
- use text_field_secondary in compact mode

---

# 7. Mapping Output Schema

Every mapping must produce a **component descriptor**:
```
{
  "component": "text_field",
  "primaryToken": "text_field_primary",
  "secondaryToken": "text_field_secondary",
  "props": {
      "label": "Email",
      "name": "email",
      "required": true,
      "maxLength": 120
  },
  "responsive": {
      "mobile": "secondary",
      "tablet": "primary",
      "desktop": "primary"
  }
}
```

This ensures stable rendering across frameworks.

---

# 8. Execution Workflow

### 8.1 Creator Role
- Applies UCMP to all properties.
- Produces component descriptors.
- Builds page definitions using these descriptors.

### 8.2 Validator Role
- Ensures rules were applied correctly.
- Confirms primary and secondary tokens are present.
- Checks semantics are respected.

### 8.3 Judge Role
- Resolves conflicts.
- Approves or requests a rerun.

---

# 9. Error Handling
Mapping errors occur if:
- no primary token can be assigned
- no secondary token exists
- mismatched schema types

The protocol requires:
- structured error messages
- clear resolution instructions
- non-silent failure modes

---

# End of Protocol

