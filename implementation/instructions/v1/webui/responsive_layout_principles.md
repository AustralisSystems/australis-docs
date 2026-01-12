# Responsive Layout Design Principles

## 1. Overarching Philosophy
Modern UI/UX must be adaptive, context-aware, and information-driven. Layouts should never be static breakpoints—they must respond to data density, container integrity, user intent, and interaction models.

A layout system is a *living structure* that:
- rearranges based on purpose
- preserves hierarchy across formats
- adapts intelligently to constraints
- maintains semantic consistency

---

## 2. Core Principles

### 2.1 Information Hierarchy First
Decide what content matters most before choosing layout. Structure flows from information priority.

### 2.2 Density Dictates Format
High density → tables
Medium density → grids
Low density → cards/lists
Extreme constraint → accordions

### 2.3 Semantic Consistency
Regardless of layout, titles stay primary, CTAs stay primary, statuses stay semantic.

### 2.4 Readability Before Composition
If text, controls, or interactions become cramped, change layout entirely rather than squeezing elements.

### 2.5 Layout Transformation Rules
Define predictable transformations:
- Table → Cards
- Cards → List
- List → Accordion
- Grid → Carousel
- Grid → Cards

### 2.6 Minimum Viable Dimensions
Each component defines minimum width, height, and readable thresholds.

### 2.7 Container Queries Over Breakpoints
Layout responds to **its container**, not global screen width.

### 2.8 Interaction-Based Adaptation
Desktop: hover, inline actions, wide scan.  
Mobile: tap-first, stacked, thumb zones.

### 2.9 Context-Specific Views
Complex data presents simplified summary views on small screens.

### 2.10 Smooth Transitional Behaviour
Transformations must be visually consistent and non-jarring.

### 2.11 Layout Manager Architecture
Centralised handler manages layout logic based on density + container width + interaction mode.

### 2.12 Declarative Responsive Logic
Rules describe *what* should happen, not *how* it’s calculated.

### 2.13 Content Visibility Priorities
Must Show → Should Show → Nice to Show hierarchy.

### 2.14 Transformation Mapping
Defined routes ensure predictable, reversible behaviour.

### 2.15 Systemic Design Approach
Design UI as an adaptive system of relationships, not fixed screens.

---

## 3. Developer Workflow Methodologies

### 3.1 Use a Responsive Layout Handler
Implement a layout manager (hook/module/service) that:
- measures container width
- checks density rules
- selects appropriate layout type

### 3.2 Define Component Minimums
Each component exports:
```
minWidth
maxColumns
collapseThreshold
truncateRules
```

### 3.3 Layout Priority Logic
```
if (containerWidth < minCardWidth) → list
if (listTooDense) → accordion
if (tableCannotFit) → cards
```

### 3.4 Tailwind Utility Strategy
- use `grid-cols-auto` and `minmax()`
- prefer `flex-col` fallback layouts
- use `md:` `lg:` `xl:` for coarse tuning
- rely heavily on container query plugins

### 3.5 Data Density Heuristics
```
numColumns
cellContentLength
hasImages
needsStatuses
interactionType
```
These determine whether table/grid/card/list is best.

### 3.6 Decoupled View Components
Each content type has multiple representations:
- TableRow
- CardItem
- ListItem
- AccordionItem

Layout handler swaps them.

### 3.7 Smooth Transitions
Use small opacity + size transitions to visually reinforce the transformation.

### 3.8 Interaction Modes
Desktop:
- hover
- inline menus
- wider actions
Mobile:
- tap
- sticky footer buttons
- collapsible sections

### 3.9 Accessibility in Responsive Systems
- maintain large tap areas
- preserve reading order
- ensure aria-expanded for accordions

### 3.10 Declarative API
```
<ResponsiveLayout
  data={items}
  density="auto"
  fallback="list"
/>
```

---

## 4. Closing Principle
Responsive design is not about breakpoints; it is about dynamic interpretation of space, density, and intent.

