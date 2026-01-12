# Responsive Layout Developer Workflow & Methodology
*(Technical implementation standards for adaptive multi-format UI layouts)*

## 1. Purpose
This document defines the engineering workflow, logic structures, and component architecture needed to build multi-dimensional responsive layouts that adapt intelligently between:
- tables
- grids
- cards
- lists
- accordions
- carousels

This workflow is declarative, data-driven, and container-aware.

---

## 2. Architecture Overview
Responsive layouts must be handled by a dedicated **Layout Manager** that operates on:
- container dimensions
- data density
- component constraints
- interaction mode (touch/desktop)
- visibility priorities

### 2.1 Core Modules
```
/layout
  ├─ useContainerQuery.ts
  ├─ useDensityEvaluator.ts
  ├─ responsiveLayoutHandler.ts
  ├─ layoutTypes.ts
  ├─ componentRegistry.ts
  └─ transformers/
        tableToCards.ts
        cardsToList.ts
        listToAccordion.ts
        gridToCarousel.ts
```

---

## 3. Component Contract
Each component variant (table row, card, list item, accordion item) must export constraints:
```
export const ComponentSpec = {
  minWidth: 240,
  optimalWidth: 320,
  maxColumns: 4,
  collapseThreshold: 280,
  preferredLayout: "cards",
  supports:
    table: true,
    grid: true,
    cards: true,
    list: true,
    accordion: true,
};
```

---

## 4. Container Query Logic
Use container queries to determine when a layout can no longer maintain structural integrity.

### 4.1 Hook
```
const { width } = useContainerQuery(ref);
```

### 4.2 Threshold Logic
```
if (width < ComponentSpec.minWidth) return "list";
if (width < ComponentSpec.collapseThreshold) return "accordion";
if (width < ComponentSpec.optimalWidth) return "cards";
return "grid";
```

---

## 5. Density Evaluation
Layouts must adapt to data density:
- number of columns
- text length
- presence of media
- semantic status indicators

### 5.1 Algorithm
```
function evaluateDensity(data) {
  const columns = estimateColumns(data);
  const hasImages = detectMedia(data);
  const hasStatuses = detectSemantic(data);

  if (columns > 5) return "table";
  if (columns >= 3) return "grid";
  if (hasImages) return "cards";
  return "list";
}
```

---

## 6. Responsive Layout Handler
Central orchestrator combining container width + density + interaction mode.

### 6.1 Flow
```
const containerLayout = getLayoutFromContainer(width);
const densityLayout = evaluateDensity(data);

return resolveFinalLayout(containerLayout, densityLayout, interactionMode);
```

### 6.2 Resolution Priority
1. Must-fit constraints
2. Component minimum thresholds
3. Density requirements
4. Interaction mode
5. Developer override

---

## 7. Layout Transformations
Each transformation is implemented as a pure function.

### 7.1 Table → Cards
```
flattenColumns();
wrapIntoCard();
ensurePrimaryContentVisible();
```

### 7.2 Cards → List
```
reduceVisualNoise();
stackVertically();
adjustImageSize();
```

### 7.3 List → Accordion
```
wrapContentInPanels();
addExpandCollapse();
promotePrimaryFieldAsHeader();
```

### 7.4 Grid → Carousel
```
convertColumnsToScrollRow();
maintainCardSpacing();
```

---

## 8. Tailwind Implementation Strategy
Use Tailwind utilities + container query plugins.

### 8.1 Structural
```
@container card (min-width: 320px) {
  .card-grid { @apply grid grid-cols-2; }
}

@container card (max-width: 319px) {
  .card-grid { @apply flex flex-col; }
}
```

### 8.2 Utility Rules
- `min-w-[240px]` for card minimums
- `grid-cols-[auto-fit,_minmax(240px,_1fr)]` for adaptive grids
- `flex-col md:flex-row` for adaptive orientation

---

## 9. Interaction Mode Recognition
### 9.1 Desktop
- hover interactions
- inline actions
- larger density views

### 9.2 Mobile
- tap-first
- thumb zone alignment
- collapsed views

Interaction mode directly contributes to layout resolution.

---

## 10. Declarative Layout API
Example component:
```
<ResponsiveLayout
  data={items}
  preferred="cards"
  fallback="list"
  enableTransitions
/>
```

---

## 11. Accessibility Workflow
- maintain reading order in transformations
- use aria-expanded for accordions
- preserve headings and semantic structure
- ensure consistent status colour usage

---

## 12. Final Engineering Principle
Responsive behaviour must be *logical*, *predictable*, and *declarative*.  
Breakpoints alone are insufficient—true responsiveness adapts to container size, content density, and user interaction mode.

