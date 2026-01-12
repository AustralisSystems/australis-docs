# Web UI Scaffolding Libraries Overview

**Version:** 1.0.0
**Date:** 2025-12-01
**Purpose:** Documentation of template and component libraries used for web UI implementation

---

## Overview

The web UI scaffolding system consists of two primary libraries that LLMs use when implementing web interfaces:

1. **`src_templates/`** - HTMX/Jinja2 server-side rendered templates
2. **`react_component_libs/`** - React/Next.js client-side components

These libraries provide production-ready, reusable building blocks that align with the design system foundations and component mapping protocols documented in this directory.

---

## 1. HTMX/Jinja2 Templates (`src_templates/`)

**Location:** `C:\github_development\projects\fastapi-fastmcp-htmx-jit-generator\src_templates`

### Purpose

Production-ready HTMX + DaisyUI + Tailwind v4 template library for server-side rendered FastAPI applications.

### Structure

```
src_templates/
├── base.html                      # Minimal base layout
├── base_dashboard.html            # Dashboard layout with navbar/sections
├── base_hub.html                  # Hub layout for dynamic content
├── README.md                      # Library usage guide
├── components/                    # Reusable HTMX components
│   ├── README.md
│   ├── alerts/                   # Alert components (success, error, warning, info)
│   │   ├── alert_base.html
│   │   ├── success.html
│   │   ├── error.html
│   │   ├── warning.html
│   │   └── info.html
│   ├── api_management/           # Domain-specific components
│   │   ├── batch_result.html
│   │   ├── connection_test_result.html
│   │   ├── endpoint_details.html
│   │   ├── endpoint_list.html
│   │   └── ... (50+ API management components)
│   ├── account_details/          # User account components
│   ├── actions_cards/            # Action card components
│   ├── anchored_actions_bar.html # Fixed action bar
│   ├── data_table_elements.html  # Table building blocks
│   ├── empty_state.html          # Empty state UI
│   ├── form_elements.html        # Form controls
│   ├── interactive_button.html   # HTMX-enabled buttons
│   ├── interactive_button_group.html
│   ├── interactive_card.html     # Metric/summary cards
│   ├── interactive_card_group.html
│   ├── interactive_data_table.html # Sortable/filterable tables
│   ├── interactive_form.html     # HTMX forms
│   ├── interactive_forms_elements.html
│   ├── interactive_form_wizard.html # Multi-step forms
│   ├── interactive_modal.html    # Modal dialogs
│   ├── interactive_panel.html    # Collapsible panels
│   ├── interactive_panel_group.html
│   ├── interactive_tabs.html     # Tab navigation
│   ├── interactive_tabs_group.html
│   ├── log_viewer.html           # Log display component
│   ├── page_header.html          # Page title/breadcrumbs
│   ├── progress_bar.html         # Progress indicators
│   ├── sidebar_navigation.html   # Sidebar nav
│   ├── sorting_grouping_controls.html
│   ├── table_row.html
│   └── tabs_elements.html
├── macros/                        # DaisyUI/Tailwind helper macros
├── pages/                         # Example page implementations
├── partials/                      # Response fragments
├── errors/                        # Error views (404, 500, etc.)
└── services/                      # Service-specific templates

```

### Key Features

**✅ Production Ready:**
- Zero TODOs, placeholders, or mock data
- Fully tested with FastAPI + HTMX
- DaisyUI component library integration
- Tailwind v4 utility classes

**✅ HTMX Progressive Enhancement:**
- All interactive components use HTMX attributes
- Server-side rendering with client-side updates
- No JavaScript frameworks required
- Graceful degradation for non-JS environments

**✅ Component Architecture:**
- Reusable macros via Jinja2 imports
- Consistent prop patterns across components
- DaisyUI variant system (primary, secondary, success, error, etc.)
- ARIA labels and accessibility built-in

**✅ Layout System:**
- Three base layouts: minimal, dashboard, hub
- Responsive grid system
- Sidebar navigation support
- Header/footer sections

### Usage Pattern

```jinja2
{# Import base layout #}
{% extends "base_dashboard.html" %}

{# Import components #}
{% from "components/interactive_card.html" import interactive_card %}
{% from "components/interactive_data_table.html" import interactive_data_table %}

{# Use in template #}
{% block content %}
  {{ interactive_card(
    title="Users",
    value="1,234",
    trend="+12%",
    hx_get="/api/stats/users",
    hx_trigger="every 30s"
  ) }}

  {{ interactive_data_table(
    columns=[
      {"key": "name", "title": "Name", "type": "text"},
      {"key": "email", "title": "Email", "type": "email"},
      {"key": "status", "title": "Status", "type": "badge"}
    ],
    hx_get="/api/users",
    hx_target="#user-table",
    hx_swap="innerHTML"
  ) }}
{% endblock %}
```

### Key Components Reference

| Component | Purpose | HTMX Enabled | DaisyUI Styled |
|-----------|---------|--------------|----------------|
| `interactive_card.html` | Metric/summary cards with live updates | ✅ | ✅ |
| `interactive_data_table.html` | Sortable, filterable tables | ✅ | ✅ |
| `interactive_form.html` | Forms with inline validation | ✅ | ✅ |
| `interactive_modal.html` | Modal dialogs with HTMX content | ✅ | ✅ |
| `interactive_tabs.html` | Tab navigation with lazy loading | ✅ | ✅ |
| `alerts/` | Success, error, warning, info alerts | ✅ | ✅ |
| `page_header.html` | Page title with breadcrumbs | ❌ | ✅ |
| `sidebar_navigation.html` | Collapsible sidebar menu | ✅ | ✅ |
| `progress_bar.html` | Progress indicators | ❌ | ✅ |
| `empty_state.html` | Empty state UI with CTA | ❌ | ✅ |

### Integration with FastAPI

```python
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Point Jinja2 loader at src_templates
templates = Jinja2Templates(directory="src_templates")

router = APIRouter(prefix="/dashboard", tags=["UI"])

@router.get("/", response_class=HTMLResponse)
async def dashboard_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="pages/dashboard/index.html",
        context={"user": current_user, "stats": get_stats()}
    )
```

### Design System Compliance

**Shadows & Depth:**
- Uses DaisyUI shadow utilities: `shadow-sm`, `shadow-md`, `shadow-lg`
- Dual-shadow system via custom Tailwind classes
- Color layering with neutral palette

**Responsive Layout:**
- Container queries via custom CSS
- Three-tier visibility (Must/Should/Nice to Show)
- Mobile-first breakpoints

**Color System:**
- DaisyUI semantic colors: `primary`, `secondary`, `accent`, `neutral`
- Semantic state colors: `success`, `warning`, `info`, `error`
- Neutral dominance (backgrounds, text)

**Typography:**
- Tailwind typography plugin integration
- Modular scale: `text-xs` through `text-3xl`
- Line heights: `leading-tight`, `leading-normal`, `leading-relaxed`

**Spacing:**
- 8pt grid via Tailwind spacing scale
- Consistent padding/margin: `p-2`, `p-4`, `p-6`, etc.

---

## 2. React/Next.js Components (`react_component_libs/`)

**Location:** `C:\github_development\projects\fastapi-fastmcp-htmx-jit-generator\react_component_libs`

### Purpose

React/TypeScript component library based on HeroUI (Next.js UI component library) for client-side rendered applications.

### Structure

```
react_component_libs/
└── heroui/                        # HeroUI component library
    ├── downloaded/                # Original HeroUI components (150+ .zip files)
    │   ├── account-details.zip
    │   ├── actions-cards.zip
    │   ├── assistant-message-with-feedback.zip
    │   ├── basic-navbar.zip
    │   ├── basic-sidebar.zip
    │   ├── basic-product-list.zip
    │   ├── calendar-booking-form.zip
    │   ├── chat-list.zip
    │   ├── dashboard-analytics.zip
    │   ├── form-with-validation.zip
    │   ├── pricing-tables.zip
    │   ├── settings-layout.zip
    │   ├── table-with-filters.zip
    │   ├── user-profile.zip
    │   └── ... (100+ more components)
    ├── converted/                 # Converted/adapted components (7 .zip files)
    │   ├── account-details.zip
    │   ├── assistant-message-with-feedback.zip
    │   ├── security-settings.zip
    │   ├── settings-layout.zip
    │   ├── settings-tabs.zip
    │   ├── table-with-filters.zip
    │   └── user-profile.zip
    ├── templates/                 # Working component templates (organized .tsx files)
    │   ├── auth/                 # Authentication components
    │   ├── auth-alt/             # Alternative auth layouts
    │   ├── buttons/              # Button variants and groups
    │   ├── cards/                # Card components with various layouts
    │   ├── chat/                 # Chat/messaging components
    │   ├── content/              # Content renderers and dynamic components
    │   ├── dropdowns/            # Dropdown menus
    │   ├── grids/                # Grid layout components
    │   ├── hero-section-basic/   # Hero sections
    │   ├── icons/                # Icon components
    │   ├── messaging/            # Message components
    │   ├── modals/               # Modal dialogs
    │   ├── popovers/             # Popover components
    │   ├── sidebar/              # Sidebar navigation
    │   ├── tabs/                 # Tab components
    │   ├── user-account/         # User account UI
    │   └── prompt-container-with-sidebar/  # Prompt UI layouts
    └── to convert/                # Components queued for conversion
```

### Key Features

**✅ HeroUI Component Library:**
- Built on Next.js + React + TypeScript
- Production-grade components from https://heroui.com/
- Tailwind CSS styling
- shadcn/ui component patterns
- Dark mode support

**✅ Component Categories:**
- **Authentication:** Login, signup, password reset
- **Navigation:** Navbars, sidebars, breadcrumbs, tabs
- **Data Display:** Tables, cards, lists, stats
- **Forms:** Input fields, validation, wizards, file uploads
- **Feedback:** Alerts, toasts, modals, progress bars
- **Layout:** Dashboard layouts, settings pages, profile pages
- **Chat/Messages:** Assistant messages, chat lists, feedback UI
- **E-commerce:** Product lists, pricing tables, checkout flows
- **Calendar/Booking:** Calendar components, booking forms

**✅ Conversion Pipeline:**
1. **Downloaded:** Original .zip files from HeroUI
2. **To Convert:** Components queued for adaptation to project standards
3. **Converted:** Components adapted with:
   - FastAPI backend integration patterns
   - Relative imports/URLs
   - Design system token alignment
   - TypeScript strict mode compliance

### Component Structure (Typical .zip contents)

```
component-name.zip
├── component-name.tsx         # Main component file
├── types.ts                   # TypeScript type definitions
├── hooks.ts                   # Custom React hooks (if applicable)
├── utils.ts                   # Helper functions
├── styles.css                 # Component-specific styles
└── README.md                  # Component documentation
```

### Usage Pattern

```tsx
// Import converted component
import { AccountDetails } from '@/components/heroui/converted/account-details';
import type { AccountDetailsProps } from '@/components/heroui/converted/account-details/types';

// Use in Next.js page
export default function ProfilePage() {
  const userData: AccountDetailsProps = {
    name: "John Doe",
    email: "john@example.com",
    avatar: "/api/users/123/avatar",
    onUpdate: async (data) => {
      // Call FastAPI backend
      await fetch('/api/users/123', {
        method: 'PUT',
        body: JSON.stringify(data)
      });
    }
  };

  return (
    <div className="container mx-auto p-6">
      <AccountDetails {...userData} />
    </div>
  );
}
```

### Integration with FastAPI Backend

React components should use **relative URLs** when calling FastAPI endpoints:

```tsx
// ✅ CORRECT: Relative URL
const response = await fetch('/api/users');

// ❌ INCORRECT: Absolute URL
const response = await fetch('http://localhost:8080/api/users');
```

### Design System Compliance

**Component Tokens:**
- Each component should reference `component_tokens.json`
- Use primary/secondary token variants
- Responsive behavior based on container width

**Responsive Layout:**
- Use CSS container queries (not viewport queries)
- Implement three-tier visibility (Must/Should/Nice)
- Mobile-first responsive design

**Accessibility:**
- ARIA labels on all interactive elements
- Keyboard navigation support
- Focus states visible
- Screen reader compatible

---

## 3. Technology Stack Hierarchy (MANDATORY)

### Priority Order

When implementing web UIs, LLMs **MUST** follow this technology hierarchy from highest to lowest priority:

#### 1. HTMX Primitives (HIGHEST PRIORITY)

**Rule:** ALWAYS use HTMX primitives FIRST before considering any JavaScript.

**Core Attributes:**
- `hx-get`, `hx-post`, `hx-put`, `hx-delete`, `hx-patch` - HTTP requests
- `hx-target` - Where to place response
- `hx-swap` - How to swap content (innerHTML, outerHTML, beforebegin, etc.)
- `hx-trigger` - What triggers request (click, load, every 30s, etc.)
- `hx-include` - Include additional form data
- `hx-indicator` - Loading indicators
- `hx-push-url`, `hx-replace-url` - History management

**Example:**
```html
<!-- ✅ CORRECT: Pure HTMX for server interaction -->
<button hx-delete="/api/users/123"
        hx-confirm="Delete this user?"
        hx-target="#user-list"
        hx-swap="outerHTML"
        class="btn btn-error">
  Delete User
</button>

<form hx-post="/api/users"
      hx-target="#user-list"
      hx-swap="beforeend">
  <input name="name" required>
  <button type="submit">Add User</button>
</form>
```

#### 2. HTMX Extensions (HIGH PRIORITY)

**Rule:** Use HTMX extensions from public repos before Alpine.js or custom JS.

**Official Extensions:**
- `loading-states` - Loading indicators and disabled states
- `multi-swap` - Swap multiple elements in one response
- `response-targets` - Conditional targeting based on status codes
- `class-tools` - Toggle/add/remove classes
- `debug` - Debug HTMX requests
- `sse` - Server-Sent Events support

**Source:** https://htmx.org/extensions/ or https://unpkg.com/htmx.org@*/dist/ext/

**Requirements:**
- Must be from official HTMX GitHub or well-maintained public repos
- Document extension source URL and version

**Example:**
```html
<!-- ✅ CORRECT: HTMX extension for loading states -->
<div hx-ext="loading-states">
  <button hx-get="/api/data"
          data-loading-disable
          data-loading-class="loading"
          data-loading="Fetching...">
    Load Data
  </button>
</div>

<script src="https://unpkg.com/htmx.org@1.9.10/dist/ext/loading-states.js"></script>
```

#### 3. Alpine.js (MEDIUM PRIORITY)

**Rule:** Use Alpine.js ONLY when HTMX primitives + extensions cannot achieve the functionality.

**Valid Use Cases:**
- Client-side state management (dropdowns, toggles, accordions)
- Form validation before submission
- Interactive UI without server round-trip
- Local data manipulation (filtering, sorting client-side arrays)

**Core Directives:**
- `x-data` - Component state
- `x-show`, `x-if` - Conditional rendering
- `x-for` - List rendering
- `x-on` (or `@`) - Event handlers
- `x-bind` (or `:`) - Attribute binding
- `x-model` - Two-way data binding

**Source:** https://cdn.jsdelivr.net/npm/alpinejs@3.x.x

**Requirements:**
- Must use CDN or npm package (no custom builds)
- Document Alpine.js version

**Example:**
```html
<!-- ✅ CORRECT: Alpine.js for client-side dropdown (no server call) -->
<div x-data="{ open: false }" class="dropdown">
  <button @click="open = !open" class="btn">
    Menu
  </button>
  <div x-show="open"
       @click.outside="open = false"
       class="menu">
    <a href="/profile">Profile</a>
    <a href="/settings">Settings</a>
  </div>
</div>

<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.13.3/dist/cdn.min.js"></script>
```

**❌ INCORRECT:** Using Alpine.js when HTMX can handle it:
```html
<!-- ❌ WRONG: Alpine.js for server interaction -->
<button @click="deleteUser(123)">Delete</button>

<!-- ✅ CORRECT: HTMX for server interaction -->
<button hx-delete="/api/users/123">Delete</button>
```

#### 4. Public JavaScript Libraries (MEDIUM-LOW PRIORITY)

**Rule:** Use public, maintained libraries from npm/CDN before writing custom JS.

**Common Libraries:**
- **Charts:** Chart.js, D3.js, ApexCharts
- **Drag & Drop:** Sortable.js, dragula
- **Enhanced Selects:** Choices.js, Tom Select, Select2
- **Date Pickers:** Flatpickr, Pikaday, Tempus Dominus
- **File Uploads:** Uppy, FilePond
- **Rich Text:** Quill, TinyMCE, Trix
- **Data Tables:** DataTables, Tabulator
- **Notifications:** Toastify, Notyf
- **Modals:** Micromodal, tingle.js

**Requirements:**
- ✅ **Active maintenance:** Commits within last 6 months
- ✅ **Popular OR standard:** >1000 GitHub stars OR industry standard
- ✅ **Public source:** npm, CDN (unpkg, jsdelivr, cdnjs)
- ✅ **Documented:** Library name, version, CDN URL in code comments

**Example:**
```html
<!-- ✅ CORRECT: Public, maintained library from CDN -->
<!-- Chart.js v4.4.0 - https://www.chartjs.org/ -->
<canvas id="myChart"></canvas>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.js"></script>
<script>
  // Chart.js initialization
  const ctx = document.getElementById('myChart');
  new Chart(ctx, {
    type: 'bar',
    data: { /* ... */ }
  });
</script>
```

**❌ INCORRECT:**
```html
<!-- ❌ Unmaintained library (last commit 3+ years ago) -->
<script src="https://cdn.example.com/dead-library-v0.1.js"></script>

<!-- ❌ Private/custom library -->
<script src="https://my-private-cdn.com/custom-framework.js"></script>

<!-- ❌ No version documentation -->
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
```

#### 5. Custom JavaScript (LOWEST PRIORITY - LAST RESORT)

**Rule:** ONLY write custom JavaScript when ALL above options are exhausted.

**Justification Required:**
Before writing ANY custom JavaScript, you MUST document:
1. ❌ **Why HTMX primitives cannot work**
2. ❌ **Why HTMX extensions cannot work**
3. ❌ **Why Alpine.js cannot work**
4. ❌ **Why no public library exists**

**Constraints:**
- ✅ Keep minimal: <50 lines per file
- ✅ Use vanilla JS (no jQuery or custom frameworks)
- ✅ Add comprehensive comments explaining necessity
- ✅ Prefer event delegation over direct event listeners
- ✅ Extract to separate `.js` files (no inline `<script>` tags)

**Justification Template:**
```markdown
# Custom JavaScript Justification

**File:** static/js/custom-chart-websocket.js

**Functionality Required:** Real-time WebSocket chart updates with custom zoom/pan

**Why HTMX Cannot Work:**
- WebSocket updates require persistent bidirectional connection
- HTMX is request/response model, not persistent connection

**Why HTMX Extensions Cannot Work:**
- SSE extension is unidirectional (server → client only)
- No HTMX WebSocket extension exists

**Why Alpine.js Cannot Work:**
- Chart.js requires imperative API: `new Chart()`, `chart.update(data)`
- Alpine.js is declarative and cannot wrap Chart.js initialization

**Why No Public Library Exists:**
- Chart.js itself is the public library (used)
- No public HTMX + Chart.js + WebSocket integration library found
- Searched npm, GitHub (0 results for "htmx chart.js websocket")

**Custom Code:** 47 lines
- WebSocket connection management
- Chart.js initialization and data updates
- Error handling and reconnection logic

**Approved by:** [Engineering Lead] on [Date]
```

**Example (when justified):**
```javascript
// static/js/custom-chart-websocket.js
// Custom WebSocket + Chart.js integration (justified - see docs/CUSTOM_JS_JUSTIFICATION.md)

const socket = new WebSocket('ws://localhost:8080/ws/chart-data');
let chart = null;

socket.onopen = () => {
  console.log('WebSocket connected');
};

socket.onmessage = (event) => {
  const data = JSON.parse(event.data);
  if (chart) {
    chart.data.datasets[0].data = data.values;
    chart.update();
  } else {
    // Initialize chart on first data
    const ctx = document.getElementById('wsChart');
    chart = new Chart(ctx, {
      type: 'line',
      data: { datasets: [{ data: data.values }] }
    });
  }
};

socket.onerror = (error) => {
  console.error('WebSocket error:', error);
  // Reconnection logic...
};
```

---

### Styling Stack Hierarchy

#### Mandatory for HTMX/Jinja2:

1. **DaisyUI** (component library) - https://daisyui.com/
2. **Tailwind CSS v4** (utility classes)

**Rule:** ALWAYS use DaisyUI + Tailwind for HTMX/Jinja2 templates.

**DaisyUI Components:**
- `btn`, `btn-primary`, `btn-error`, `btn-ghost`
- `card`, `card-body`, `card-title`
- `alert`, `alert-success`, `alert-error`
- `badge`, `badge-primary`, `badge-secondary`
- `modal`, `drawer`, `dropdown`, `tabs`
- `form-control`, `input`, `textarea`, `select`

**Example:**
```html
<!-- ✅ CORRECT: DaisyUI + Tailwind -->
<div class="card bg-base-100 shadow-md">
  <div class="card-body">
    <h2 class="card-title text-2xl">User Profile</h2>
    <p class="text-sm text-gray-600">Edit your details</p>
    <div class="card-actions justify-end">
      <button class="btn btn-primary">Save</button>
    </div>
  </div>
</div>
```

#### Custom CSS (Last Resort):

**Rule:** ONLY write custom CSS when DaisyUI + Tailwind cannot achieve the design.

**Valid use cases:**
- Complex animations not supported by Tailwind
- Highly specific brand requirements
- Custom shadow systems (dual-shadow from design foundations)

**Constraints:**
- Keep minimal: <100 lines per file
- Use CSS custom properties (variables) for values
- Document why DaisyUI/Tailwind insufficient
- Follow BEM naming convention for custom classes

---

### Technology Decision Flowchart

```
User interaction needed?
│
├─ Server interaction (GET/POST/DELETE/etc.)?
│  ├─ YES → Use HTMX primitives (hx-get, hx-post, etc.) ✅
│  └─ NO → Continue to next check
│
├─ Advanced HTMX behavior needed (loading states, multi-swap)?
│  ├─ YES → Use HTMX extensions ✅
│  └─ NO → Continue to next check
│
├─ Client-side state/interactivity (dropdown, toggle, accordion)?
│  ├─ YES → Use Alpine.js ✅
│  └─ NO → Continue to next check
│
├─ Complex functionality (charts, rich text, drag-drop)?
│  ├─ Public library exists?
│  │  ├─ YES → Use public library (Chart.js, Quill, etc.) ✅
│  │  └─ NO → Continue to next check
│  └─ NO → Continue to next check
│
└─ ALL above options exhausted?
   ├─ YES → Document justification + write custom JS ⚠️
   └─ NO → Re-evaluate (you likely missed a solution)
```

---

## 4. LLM Implementation Workflow

When implementing web UIs, LLMs should follow this workflow:

### Phase 1: Choose Stack

**Decision criteria:**
- **HTMX/Jinja2** if:
  - Server-side rendering preferred
  - Simple page updates
  - Progressive enhancement approach
  - No complex client-side state management

- **React/Next.js** if:
  - Complex client-side interactions
  - Real-time updates (WebSocket-heavy)
  - Rich data visualization
  - SPA (Single Page Application) architecture

### Phase 2: Component Selection

**HTMX/Jinja2:**
1. Browse `src_templates/components/` directory
2. Select components matching UI requirements
3. Check component README for props/usage
4. Import via Jinja2 `{% from ... import ... %}`

**React/Next.js:**
1. Browse `react_component_libs/heroui/downloaded/` or `converted/`
2. Extract .zip file to project components directory
3. Adapt imports to use relative paths
4. Update API calls to use relative URLs
5. Apply design tokens from `component_tokens.json`

### Phase 3: Implementation

**HTMX/Jinja2:**
```jinja2
{# 1. Extend base layout #}
{% extends "base_dashboard.html" %}

{# 2. Import components #}
{% from "components/interactive_card.html" import interactive_card %}

{# 3. Use components with HTMX attributes #}
{% block content %}
  {{ interactive_card(
    hx_get="/api/stats",
    hx_trigger="load, every 30s"
  ) }}
{% endblock %}
```

**React/Next.js:**
```tsx
// 1. Import component
import { DataTable } from '@/components/heroui/converted/table-with-filters';

// 2. Fetch data from FastAPI
const [data, setData] = useState([]);
useEffect(() => {
  fetch('/api/users').then(r => r.json()).then(setData);
}, []);

// 3. Render with props
return <DataTable data={data} onSort={handleSort} />;
```

### Phase 4: Validation

**All implementations must validate:**
- ✅ Relative URLs (no `http://localhost:8080`)
- ✅ Relative imports (no `from src.services...`)
- ✅ HTMX endpoints reference existing routers
- ✅ Design tokens used (no hardcoded colors/sizes)
- ✅ Container queries (no viewport `@media`)
- ✅ WCAG AA contrast ratios
- ✅ Keyboard navigation functional

---

## 4. Directory References

**When LLMs receive instructions, they should have access to:**

```
src_templates/                     # Copy to project templates directory
react_component_libs/heroui/       # Extract .zip files as needed
component_tokens.json              # Design tokens
design_system_foundations.md       # Design principles
universal_component_mapping_protocol.md  # Component selection rules
```

**Typical project structure:**
```
my-fastapi-project/
├── src/
│   ├── services/
│   │   └── ui/
│   │       ├── routers/         # FastAPI routers
│   │       ├── services/        # Business logic
│   │       └── templates/       # ← Copy src_templates/ here
│   │           ├── base.html
│   │           ├── components/
│   │           ├── pages/
│   │           └── ...
│   └── frontend/                # Next.js app (if using React)
│       ├── components/          # ← Extract heroui .zip files here
│       ├── app/
│       └── public/
└── ...
```

---

## 5. Conversion Guidelines

When converting HeroUI React components for project use:

**1. Update Imports:**
```tsx
// Before (absolute)
import { Button } from '@heroui/react';
import { api } from '@/lib/api';

// After (relative)
import { Button } from '../../ui/button';
import { api } from '../../../lib/api';
```

**2. Update API Calls:**
```tsx
// Before (absolute URL)
fetch('http://localhost:8080/api/users')

// After (relative URL)
fetch('/api/users')
```

**3. Apply Design Tokens:**
```tsx
// Before (hardcoded)
<div className="bg-blue-500 shadow-lg p-6">

// After (tokens)
<div className="bg-primary shadow-md p-6">
```

**4. Add TypeScript Types:**
```tsx
// Define prop types
interface UserCardProps {
  userId: string;
  name: string;
  email: string;
  onUpdate: (data: UserData) => Promise<void>;
}

// Use in component
export const UserCard: React.FC<UserCardProps> = ({ ... }) => {
  // ...
};
```

---

## 6. Summary

**HTMX/Jinja2 (`src_templates/`):**
- 🎯 **Purpose:** Server-side rendered FastAPI UIs
- 📦 **Components:** 50+ production-ready templates
- 🎨 **Styling:** DaisyUI + Tailwind v4
- ⚡ **Enhancement:** HTMX progressive enhancement
- ✅ **Status:** Production ready, zero TODOs

**React/Next.js (`react_component_libs/heroui/`):**
- 🎯 **Purpose:** Client-side rendered React UIs
- 📦 **Components:** 150+ HeroUI components (zipped)
- 🎨 **Styling:** Tailwind CSS + shadcn/ui patterns
- 🔄 **Status:** Downloaded originals + 7 converted examples
- ⚠️ **Requires:** Conversion to project standards (relative imports/URLs, design tokens)

**Both libraries:**
- Align with `design_system_foundations.md` principles
- Support component_tokens.json token system
- Enforce relative imports and relative URLs
- Provide production-grade scaffolding for LLM implementation

---

**Last Updated:** 2025-12-01
**Maintained By:** Shadow Team AI
**Reference:** UI Factory Documentation Suite
