Quick Summary - ChatGPT UI Factory Session

  Context: You've been working with ChatGPT to build a comprehensive Web UI App Factory system. Here's what's been covered:

  Core Objectives

  Building a FastAPI-based application factory that:
  - Reads OpenAPI JSON specifications as input
  - Automatically generates complete web applications with pages, routes, and layouts
  - Produces both React components AND HTMX/Jinja2 templates from the same design system
  - Supports bidirectional conversion between React ↔ HTMX/Jinja2

  Design Foundations Established

  Three Core UI/UX Principles (extracted from YouTube video transcript):

  1. Shadows & Depth
    - Dual-shadow systems (light top, dark bottom)
    - Color layering with 3-4 tonal variations
    - Gradient enhancements for realism
  2. Responsive Layout
    - "Systems of boxes" with parent-child relationships
    - Rearranging with purpose (not just shrinking)
    - Container-query based (not just breakpoints)
    - Adaptive transformations: table → cards → list → accordion
  3. Color Systems
    - Primary (CTAs), Secondary (accents), Neutral (structure), Semantic (states)
    - Consistent hierarchy across all layouts

  Architecture Components (A-F)

  ✅ A - layout.tokens.json: Complete design token system
  - Spacing, breakpoints, elevation, radius, typography
  - Motion patterns (durations, easing, named transitions)
  - Behavior tokens (density thresholds, collapse rules)

  ⏭️ B - Component Specs: SKIPPED (as you requested)

  🔄 C - Motion & Transitions: In progress
  - Animation principles and timing
  - Layout transformation animations
  - Consistent visual feedback

  📋 D - Tailwind Generator: Upcoming
  - Auto-generates tailwind.config.js from tokens
  - Shared config for React + HTMX templates

  🔄 E - OpenAPI → UI Model Converter: Upcoming
  - Conversion rules from OpenAPI to intermediate UI Model JSON
  - Determines page layouts, component types, data density

  🏗️ F - MCP Protocol: Upcoming
  - Complete protocol for the UI Factory system
  - LLM prompt templates for generation and conversion

  Key Innovation

  Intelligent Layout Handler that automatically:
  - Evaluates data density → chooses optimal layout type
  - Responds to container width (not just screen size)
  - Transforms layouts: table → grid → cards → list → accordion
  - Maintains semantic consistency across all transformations

  Current Status

  ChatGPT has completed:
  - ✅ Design principles documentation
  - ✅ Responsive layout developer workflow
  - ✅ Figma design deck structure
  - ✅ layout.tokens.json (Component A)
  - 🔄 Working on Motion & Transitions System (Component C)

  Next: Continue through D, E, F to complete the full system specification.

  ---
  This is a sophisticated UI generation framework that will enable LLM-driven automatic web application creation from API specifications while maintaining professional design standards. 🎨⚡

● Ran 3 stop hooks

> C:\github_development\ai-agents\.mcp_prompts\implementation\instructions\web-ui\ ... now list all the files in this dir ... then review the first file only

● filesystem - list_directory (MCP)(path: "C:\\github_development\\ai-agents\\.mcp_prompts\\implementation\\instructions\\web-ui\\")
  ⎿  [FILE] ChatGPT_UI_Factory_Webui_Design_instructions_and_concepts_2025-12-01T05-59-56.html
     [FILE] ChatGPT_UI_Factory_Webui_Design_instructions_and_concepts_2025-12-01T05-59-56.json
     [FILE] ChatGPT_UI_Factory_Webui_Design_instructions_and_concepts_2025-12-01T05-59-56.md
     … +12 lines (ctrl+o to expand)

● Read(.mcp_prompts\implementation\instructions\web-ui\ChatGPT_UI_Factory_Webui_Design_instructions_and_concepts_2025-12-01T05-59-56.html)
  ⎿  Read 500 lines

● Files in Directory

  Here are all 15 files in C:\github_development\ai-agents\.mcp_prompts\implementation\instructions\web-ui\:

  1. ChatGPT_UI_Factory_Webui_Design_instructions_and_concepts_2025-12-01T05-59-56.html
  2. ChatGPT_UI_Factory_Webui_Design_instructions_and_concepts_2025-12-01T05-59-56.json
  3. ChatGPT_UI_Factory_Webui_Design_instructions_and_concepts_2025-12-01T05-59-56.md
  4. component_tokens.json
  5. design_system_foundations.md
  6. figma_guideline_deck.md
  7. layout_tokens.json
  8. mcp_ui_factory_protocol.md
  9. motion_transition_spec.md
  10. openapi_ui_model_conversion_rules.md
  11. renderer_mapping_spec.md
  12. responsive_layout_developer_workflow.md
  13. responsive_layout_principles.md
  14. tailwind_generator_template.js
  15. universal_component_mapping_protocol.md

  ---
  Review: First File (HTML Export)

  File: ChatGPT_UI_Factory_Webui_Design_instructions_and_concepts_2025-12-01T05-59-56.html

  Type: HTML document - styled ChatGPT conversation export

  Purpose: This is a browser-viewable export of the entire ChatGPT conversation about building the UI Factory system.

  Contents:
  - Styled Layout: Mimics ChatGPT's interface with proper CSS for messages, code blocks, tables, and formatting
  - Full Conversation: Contains the complete dialogue between user and ChatGPT
  - Design Principles: All three core principles (Shadows, Responsiveness, Color Systems) from the YouTube video transcript
  - Implementation Details: Includes color layering, dual-shadow systems, responsive layout rules, and color palette guidelines
  - Visual Elements: Tables showing neutral color hierarchies, blockquotes with design quotes

  Key Styling Features:
  - ChatGPT-like message bubbles (user vs assistant)
  - Syntax-highlighted code blocks with dark theme
  - Responsive max-width container (48rem)
  - Proper typography and spacing
  - Table formatting with borders and headers

  Assessment: This is a well-formatted, self-contained reference document that can be opened in any browser. It serves as a visual archive of the conversation that generated all the other specification
  files in this directory.

  Would you like me to review the next file, or would you prefer to examine specific files from the list?

● Ran 3 stop hooks

> ok.. now just focus on the .md files... then review the design_system_foundations.md

● Search(pattern: "*.md", path: ".mcp_prompts\implementation\instructions\web-ui")
  ⎿  Found 10 files (ctrl+o to expand)

● Read(.mcp_prompts\implementation\instructions\web-ui\design_system_foundations.md)
  ⎿  Read 113 lines

● Markdown Files in Directory (10 files)

  1. ChatGPT_UI_Factory_Webui_Design_instructions_and_concepts_2025-12-01T05-59-56.md - Full conversation export
  2. design_system_foundations.md ⭐ (reviewing this one)
  3. figma_guideline_deck.md - Visual presentation format
  4. mcp_ui_factory_protocol.md - MCP integration protocol
  5. motion_transition_spec.md - Animation specifications
  6. openapi_ui_model_conversion_rules.md - OpenAPI → UI Model conversion
  7. renderer_mapping_spec.md - Framework rendering mappings
  8. responsive_layout_developer_workflow.md - Developer workflow guide
  9. responsive_layout_principles.md - Responsive design principles
  10. universal_component_mapping_protocol.md - Component mapping system

  ---
  Review: design_system_foundations.md

  Structure & Purpose

  This is a concise, dual-mode reference document (113 lines) that serves as a high-level overview of the entire design system. It's structured for both designers (principles) and developers
  (implementation).

  Strengths

  ✅ Clarity: Clean, scannable format with clear section hierarchy
  ✅ Completeness: Covers all three core principles (Shadows, Responsiveness, Color)
  ✅ Practicality: Includes both "why" (philosophy) and "how" (implementation)
  ✅ AI-Ready: Contains explicit LLM prompt templates (Section 4)
  ✅ Enforceable: Has concrete enforcement rules (Section 5)

  Content Breakdown

  Section 1: Overview & Philosophy (6 lines)
  - Establishes timeless design principles approach
  - Sets scope: shadows, depth, responsiveness, color systems

  Section 2: Core Principles (47 lines)
  - 2.1 Shadows & Depth: Dual-shadow systems, color layering, gradients
  - 2.2 Responsiveness: Systems of boxes, purposeful rearrangement
  - 2.3 Color Systems: 4 palette roles (Primary, Secondary, Neutral, Semantic)

  Section 3: Developer Implementation (22 lines)
  - Token naming conventions for colors, shadows, spacing, typography
  - Uses code blocks for token structure examples
  - References 8pt spacing scale and modular typography

  Section 4: AI & Automation Prompts (9 lines)
  - Three ready-to-use prompt templates
  - Each maps to a core principle
  - Concise, actionable directives

  Section 5: Enforcement Rules (6 lines)
  - 5 mandatory requirements
  - Ensures consistency across implementations
  - Testing and validation criteria

  Section 6: Closing Principle (2 lines)
  - Philosophical anchor: "Design is communication"

  Gaps & Observations

  ⚠️ Missing Details:
  - No actual token values (references layout_tokens.json externally)
  - Shadow specifications lack concrete values (0 1px 2px rgba...)
  - No breakpoint definitions (sm/md/lg/xl values)
  - Typography scale not defined (just says "modular")
  - No examples or code snippets beyond token structure

  ⚠️ Developer Implementation Section:
  - Shows token naming structure but not actual values
  - Developers would need to reference layout_tokens.json for specifics

  ✅ By Design:
  - This appears intentional - it's a summary/overview document
  - Detailed specifications live in companion files (layout_tokens.json, motion_transition_spec.md, etc.)

  Role in the System

  This file serves as:
  1. Entry point - First document to read for understanding the system
  2. Quick reference - Fast lookup for core principles
  3. Prompt library - LLM instruction templates
  4. Compliance checklist - Enforcement rules for validation

  Relationship to Other Files

  design_system_foundations.md (YOU ARE HERE - Overview)
      ↓
  ├── layout_tokens.json (Concrete values)
  ├── responsive_layout_principles.md (Deep dive: responsiveness)
  ├── responsive_layout_developer_workflow.md (Implementation workflow)
  ├── motion_transition_spec.md (Animation details)
  ├── figma_guideline_deck.md (Visual presentation)
  └── mcp_ui_factory_protocol.md (System integration)

  Assessment

  Quality: ⭐⭐⭐⭐⭐ (Excellent)
  Completeness: ⭐⭐⭐⭐ (Intentionally high-level)
  Usability: ⭐⭐⭐⭐⭐ (Very accessible)
  AI-Readiness: ⭐⭐⭐⭐⭐ (Prompt templates included)

  Recommendation

  This document is production-ready as an overview. For the UI Factory system, it should be:
  - Index document - Link to all detailed specifications
  - Onboarding guide - First read for new developers/designers
  - LLM context - Loaded before generating UI components

  Next steps: Would you like me to review the companion specifications to see how they expand on these foundations?

● Ran 3 stop hooks

> review the next md files.. we are only reviewing 1 at a time

● Read(.mcp_prompts\implementation\instructions\web-ui\figma_guideline_deck.md)
  ⎿  Read 121 lines

● Review: figma_guideline_deck.md

  Structure & Purpose

  This is a presentation-ready slide deck (121 lines, 15 slides) formatted for easy import into Figma, PowerPoint, or Keynote. It's a visual communication tool for presenting the design system to
  stakeholders, designers, or developers.

  Format Analysis

  Slide Structure:
  - Each slide clearly marked with ## Slide N — Title
  - Horizontal rules (---) separate slides
  - Consistent formatting throughout
  - Bold headers for emphasis
  - Bullet points for scannable content

  Content Breakdown

  Slide 1-2: Introduction (7 lines)
  - Title slide establishes scope
  - Philosophy slide sets tone ("Tools Change. Principles Don't.")

  Slides 3-6: Shadows & Depth (31 lines)
  - Overview of 4 core principles
  - 3 slides dedicated to shadows (color layering, dual shadows, gradients)
  - Progressive disclosure of complexity

  Slides 7-8: Responsiveness (14 lines)
  - Systems of boxes concept
  - Purposeful rearrangement principle
  - Clear, non-technical language

  Slides 9-10: Color Systems (14 lines)
  - Palette role definitions
  - Usage pattern guidelines
  - Semantic meaning emphasis

  Slides 11-12: Typography & Spacing (14 lines)
  - 8pt grid system
  - Modular scale approach
  - Practical implementation hints

  Slide 13: Implementation Prompts (7 lines)
  - AI-assisted design guidance
  - Three core prompt templates
  - Bridges design → development

  Slide 14: Enforcement (7 lines)
  - Design governance rules
  - Quality assurance checklist
  - Mandatory requirements

  Slide 15: Closing (4 lines)
  - Philosophical anchor
  - Reinforces system value

  Strengths

  ✅ Presentation-Ready: Can be directly imported into Figma frames
  ✅ Progressive Disclosure: Complex topics broken into digestible slides
  ✅ Consistent Voice: Professional, authoritative tone throughout
  ✅ Visual Hierarchy: Bold headers + bullets create scannable structure
  ✅ Actionable: Includes implementation prompts (Slide 13)
  ✅ Complete Arc: Introduction → Principles → Implementation → Governance → Closing

  Comparison to design_system_foundations.md

  | Aspect   | design_system_foundations.md  | figma_guideline_deck.md |
  |----------|-------------------------------|-------------------------|
  | Format   | Reference document            | Presentation slides     |
  | Audience | Developers + Designers        | Stakeholders + Teams    |
  | Depth    | Moderate (with code examples) | High-level overview     |
  | Use Case | Day-to-day reference          | Training/Onboarding     |
  | Length   | 113 lines                     | 121 lines               |
  | Code     | Token structure examples      | No code blocks          |

  Gaps & Observations

  ⚠️ Visual Elements Missing:
  - No placeholder annotations for images/diagrams
  - Could benefit from "[IMAGE: dual shadow diagram]" placeholders
  - No color swatches or visual examples noted

  ⚠️ Slide Distribution:
  - Shadows get 3 slides (well-covered)
  - Responsiveness gets 2 slides (adequate)
  - Color gets 2 slides (adequate)
  - Typography/Spacing get 1 slide each (brief but sufficient for overview)

  ✅ By Design:
  - This is intentionally text-focused for Figma import
  - Designers would add visual elements in Figma after import
  - Text content provides the narrative structure

  Usability Assessment

  For Figma Import:
  - ⭐⭐⭐⭐⭐ Perfect - Clean markdown structure translates easily
  - Each H2 (##) becomes a frame title
  - Bullets map directly to text layers
  - Horizontal rules indicate slide breaks

  For Presentation Delivery:
  - ⭐⭐⭐⭐ Very Good - Clear progression, good pacing
  - 15 slides = 15-20 minute presentation at ~1 min/slide
  - Could use 2-3 visual example slides for impact

  For Documentation:
  - ⭐⭐⭐⭐ Good - Works as standalone quick reference
  - More accessible than full spec documents
  - Good for executive summaries

  Role in the System

  figma_guideline_deck.md (YOU ARE HERE - Presentation)
      ↑
  design_system_foundations.md (Source material)
      ↓
  Figma Design File (Visual implementation)
      ↓
  PDF Export / Team Presentation

  Recommendation for Enhancement

  Optional Additions:
  1. Slide 5.5 - Add visual diagram placeholder: "[IMAGE: Before/After shadow comparison]"
  2. Slide 8.5 - Add example: "[DEMO: Mobile vs Desktop layout transformation]"
  3. Slide 10.5 - Add color palette example: "[VISUAL: Primary/Secondary/Neutral swatches]"

  Current State: Production-ready as-is ✅

  Assessment

  Quality: ⭐⭐⭐⭐⭐ (Excellent)
  Clarity: ⭐⭐⭐⭐⭐ (Very clear, scannable)
  Completeness: ⭐⭐⭐⭐ (Covers essentials, could add visuals)
  Presentation Value: ⭐⭐⭐⭐⭐ (Ready for stakeholder presentation)

  Next File Preview

  Would you like me to review mcp_ui_factory_protocol.md next?

● Ran 3 stop hooks

> review the next one and halt

● Read(.mcp_prompts\implementation\instructions\web-ui\mcp_ui_factory_protocol.md)
  ⎿  Read 275 lines

● Review: mcp_ui_factory_protocol.md

  Structure & Purpose

  This is a comprehensive protocol specification (275 lines) that defines the complete orchestration system for the UI Factory. It's the operational blueprint for how LLMs, design tokens, and code
  generators work together to produce web applications from OpenAPI specifications.

  Architecture Overview

  Three-Role Model (lines 18-37):
  - Creator: Generates UI Model + code scaffolds
  - Validator: Verifies conformance to schemas and rules
  - Judge: Resolves conflicts and approves final output

  This is a sophisticated quality assurance pattern inspired by ensemble programming and multi-agent validation systems.

  Content Breakdown

  Section 1: Purpose (14 lines)
  - Clear scope definition
  - Four key properties: deterministic, auditable, repeatable, renderer-agnostic
  - Input sources clearly identified

  Section 2: Roles (19 lines)
  - Distinct separation of concerns
  - Prevents single-point-of-failure in generation
  - Each role has explicit responsibilities
  - Critical: "Each role must be implemented by a distinct model or tool"

  Section 3: Inputs (19 lines)
  - 5 required input types
  - References companion files (layout.tokens.json, conversion rules)
  - Supports dual rendering targets (React + HTMX/Jinja2)

  Section 4: Core Artefacts (21 lines)
  - 6 output types
  - Includes protocol logging for auditability
  - Project structure generation

  Section 5: High-Level Stages (31 lines)
  - 6-stage pipeline
  - Linear progression with validation gates
  - Clear handoffs between Creator/Validator/Judge

  Section 6: Stage Details (97 lines) ⭐ Most Important Section
  - Granular specifications for each stage
  - Concrete validation criteria
  - Error handling and retry logic
  - Specific file paths and naming conventions

  Section 7: Error Handling (13 lines)
  - Machine-readable status codes
  - Halt-on-error policy
  - Required fix proposals from LLMs

  Section 8: Outputs & Manifest (11 lines)
  - Complete artifact inventory
  - Includes protocol logging
  - Manifest for file tracking

  Section 9: Usage Notes (10 lines)
  - Extensibility guidance
  - Token-driven design enforcement
  - LLM consultation requirements

  Strengths

  ✅ Complete Pipeline Definition: Every stage from input to output clearly specified
  ✅ Quality Assurance Built-In: Three-role validation prevents hallucinations
  ✅ Deterministic: No room for ad-hoc decisions or creativity bypassing rules
  ✅ Auditable: Protocol log + manifest enable full traceability
  ✅ Error-Resistant: Explicit error handling at each stage
  ✅ Extensible: Renderer-agnostic design (can add Vue, Svelte, etc.)
  ✅ Reference Integration: Explicitly calls out companion files (layout.tokens.json, conversion rules)

  Key Implementation Details

  Stage 2 - UI Model Generation (lines 142-162):
  - Automatic CRUD page detection
  - Layout selection algorithm (table/grid/cards based on field count)
  - Three-tier visibility rules (mustShow/shouldShow/niceToShow)
  - Responsive behavior injection from tokens

  Stage 4 - Code Generation (lines 180-202):
  - Separate paths for React vs HTMX/Jinja2
  - Specific file naming conventions (src/pages/{pageId}.tsx)
  - Shared component library (Card, Table, List, Accordion)
  - Motion token integration for transitions

  Stage 6 - Judgment (lines 216-230):
  - Final validation of completeness
  - Flow coverage verification
  - Design system compliance check
  - Structured retry mechanism

  Critical Requirements

  LLM Obligations (lines 265-269):
  LLMs must always consult:
    - layout.tokens.json
    - motion transition spec
    - OpenAPI → UI Model conversion rules
  before generating or modifying UI code.

  This is THE GOLDEN RULE for the UI Factory system.

  Comparison to Other Files

  | File                                    | Role                 | Relationship to mcp_ui_factory_protocol.md |
  |-----------------------------------------|----------------------|--------------------------------------------|
  | design_system_foundations.md            | Design principles    | Referenced - Provides design rules         |
  | layout_tokens.json                      | Token definitions    | Input - Required at Stage 1                |
  | openapi_ui_model_conversion_rules.md    | Conversion logic     | Input - Used at Stage 2                    |
  | responsive_layout_developer_workflow.md | Implementation guide | Referenced - Informs Stage 4               |

  Gaps & Observations

  ⚠️ Missing Specifications:
  - No timeout values for LLM operations
  - No concurrency limits (how many pages generated in parallel?)
  - No versioning strategy for protocol evolution
  - No rollback/undo mechanism if Judge rejects

  ⚠️ Ambiguities:
  - "Distinct model or tool" for roles - can this be 3 instances of same model?
  - Stage 6 "requests specific re-runs" - but no maximum retry count specified
  - Protocol log format not specified (JSON structure undefined)

  ✅ Intentional Design:
  - High-level enough to allow multiple implementations
  - Implementation details delegated to companion specs
  - Focus on orchestration, not low-level code generation

  Integration Points

  OpenAPI Spec
      ↓
  Stage 1: Initialization → Validates layout.tokens.json
      ↓
  Stage 2: UI Model Generation (Creator)
      ↓
  Stage 3: UI Model Validation (Validator)
      ↓
  Stage 4: Code Generation (Creator) → Uses responsive_layout_developer_workflow.md
      ↓
  Stage 5: Code Validation (Validator)
      ↓
  Stage 6: Judgment (Judge)
      ↓
  Artefacts: ui-model.json + tailwind.config.js + React/HTMX code

  Production Readiness

  Completeness: ⭐⭐⭐⭐ (Missing retry limits, timeouts, versioning)
  Clarity: ⭐⭐⭐⭐⭐ (Exceptionally clear)
  Implementability: ⭐⭐⭐⭐⭐ (Ready to implement)
  Safety: ⭐⭐⭐⭐⭐ (Three-role validation is robust)
  Extensibility: ⭐⭐⭐⭐⭐ (Renderer-agnostic design)

  Assessment

  This is a production-grade orchestration protocol that demonstrates sophisticated understanding of:
  - Multi-agent LLM systems
  - Quality assurance through separation of concerns
  - Design system enforcement
  - Code generation pipelines

  Role in System: This is the master orchestration document that ties together all other specifications. It's the "operating system" of the UI Factory.

  Recommendation: Add minor enhancements (retry limits, timeout values, protocol log schema) but deploy as-is for MVP.

  ---
  Halting as requested.

● Ran 3 stop hooks

> review the next one

● Read(.mcp_prompts\implementation\instructions\web-ui\motion_transition_spec.md)
  ⎿  Read 167 lines

● Review: motion_transition_spec.md

  Structure & Purpose

  This is a comprehensive animation and motion specification (167 lines) that defines how all UI components should animate across React, HTMX, and Jinja2 implementations. It ensures consistent motion
  language regardless of rendering technology.

  Architecture Overview

  Token-Driven Design (lines 32-37):
  - All motion values reference layout.tokens.json
  - No hard-coded durations or easing values allowed
  - Creates single source of truth for motion

  Four Core Principles (lines 10-37):
  1. Motion communicates meaning (not decoration)
  2. Subtle and responsive (< 300ms default)
  3. Stateful and reversible (every transition has inverse)
  4. Token-based only (no ad-hoc values)

  Content Breakdown

  Section 2: Core Principles (27 lines)
  - 2.1 Meaning: Spatial relationships, hierarchy, state changes
  - 2.2 Responsiveness: 300ms limit, device scaling, reduced-motion support
  - 2.3 Reversibility: Bidirectional state transitions (expand ↔ collapse)
  - 2.4 Token-Based: Enforces layout.tokens.json as source of truth

  Section 3: Duration Tokens (8 lines)
  - 5 duration levels: Instant (50ms) → Long (400ms)
  - Written in readable format ("fifty milliseconds")
  - References external token file

  Section 4: Easing Tokens (6 lines)
  - 4 easing curves with bezier values
  - Standard, accelerate, decelerate, emphasised
  - Material Design-inspired naming

  Section 5: Motion Patterns (27 lines) ⭐ Core Animation Library
  - 5.1 Fade: Opacity transitions (in/out)
  - 5.2 Scale: Modal/card animations (0.9 ↔ 1.0)
  - 5.3 Slide: Directional movement (up/down/left/right)
  - 5.4 Collapse/Expand: Accordion/nav animations
  - 5.5 Shared Element: Layout mode transformations

  Section 6: Behavioural Rules (21 lines)
  - 6.1 Layout Transitions: Table → Grid → Cards → List → Accordion
  - 6.2 Micro-interactions: Hover lift, active press, focus ring
  - 6.3 Page-level Events: Page enter/exit, modal open/close

  Section 7: Device-Responsive Motion (9 lines)
  - Mobile: 50% distance reduction, 20% duration reduction
  - Desktop: Full transforms

  Section 8: Reduced Motion (6 lines)
  - Accessibility requirement
  - Disables transforms, uses instant opacity only
  - Critical for WCAG compliance

  Section 9: Implementation Requirements (13 lines)
  - React: Framer Motion or CSS transitions
  - HTMX/Alpine: CSS transitions only
  - Jinja2: Server-rendered CSS transitions

  Section 10: Validation Rules (6 lines)
  - 400ms maximum duration
  - Token easing only
  - Symmetrical transitions
  - Non-blocking motion

  Section 11: Notes (11 lines)
  - Brand/theme neutral
  - Universal across all renderers
  - Canonical protocol declaration

  Strengths

  ✅ Accessibility First: Reduced motion support built-in (Section 8)
  ✅ Performance Conscious: 300ms default limit prevents janky UX
  ✅ Framework Agnostic: Works across React, HTMX, Jinja2
  ✅ Reversible Design: Every animation has inverse state
  ✅ Token Enforcement: No ad-hoc values allowed
  ✅ Device Awareness: Mobile optimizations defined
  ✅ Comprehensive Coverage: Layout, component, and page-level motions
  ✅ Validation Rules: Clear quality gates

  Motion Pattern Library

  Fade (subtle):          opacity: 0 → 1 (150ms, decelerate)
  Scale (emphasis):       transform: scale(0.9 → 1.0) (200ms, standard)
  Slide (direction):      translateY: 1rem → 0 (150ms, decelerate)
  Collapse/Expand:        max-height: 0 → auto (200ms, standard)
  Shared Element:         Smooth container morphing

  Layout Transition Mapping

  Table → Grid      (medium, fade + reflow)
  Grid → Cards      (medium, scale + fade)
  Cards → List      (fast, collapse + fade)
  List → Accordion  (medium, expand)
  Any → Carousel    (medium, slide)

  Critical Implementation Details

  Micro-interactions (lines 100-103):
  Hover:  shadow elevation increase (subtle)
  Active: scale(0.95) (feedback)
  Focus:  ring fade-in (150ms, accessibility)

  Page-level Events (lines 105-109):
  Page enter:   fade + slideUp (200ms)
  Page exit:    fade out (150ms, faster exit)
  Modal open:   fade + scale (200ms)
  Modal close:  fade + scale down (150ms, faster dismiss)

  Device Optimization Strategy

  Mobile (lines 114-116):
  - Distance: 50% reduction (prevents excessive movement on small screens)
  - Duration: 20% faster (accounts for touch feedback expectations)
  - Example: slideUp from 1rem → 0.5rem, 200ms → 160ms

  Desktop (lines 118-120):
  - Full transforms (utilizes available screen space)
  - Standard durations (users expect richer animations)

  Accessibility Compliance

  Reduced Motion (lines 124-128):
  @media (prefers-reduced-motion: reduce) {
    * {
      animation-duration: 50ms !important;
      transition-duration: 50ms !important;
      transform: none !important;
    }
  }

  This ensures WCAG 2.1 Level AA compliance (Success Criterion 2.3.3).

  Integration with Other Specifications

  | File                                    | Relationship to motion_transition_spec.md                 |
  |-----------------------------------------|-----------------------------------------------------------|
  | layout_tokens.json                      | Source - Defines actual duration/easing values            |
  | mcp_ui_factory_protocol.md              | References - Stage 4 code generation uses motion tokens   |
  | responsive_layout_developer_workflow.md | Coordinates - Layout transformations use these animations |
  | design_system_foundations.md            | Complements - Motion enhances shadow/depth system         |

  Gaps & Observations

  ⚠️ Missing Specifications:
  - No loading state animations (spinners, skeletons)
  - No error state animations (shake, pulse)
  - No success state animations (checkmark, pulse)
  - No animation chaining/sequencing rules (when multiple animations occur)
  - No z-index management during transitions

  ⚠️ Token Values as Text:
  - Durations written as "fifty milliseconds" instead of 50
  - Easing written as "two five zero" instead of 0.25
  - Intentional: References external token file, avoids duplication

  ✅ Smart Design Decisions:
  - Faster exit than entry (150ms vs 200ms) = perceived responsiveness
  - Mobile optimization prevents motion sickness on small screens
  - Symmetrical transitions ensure predictable UX

  Validation Against Best Practices

  Material Design Alignment: ✅
  - Duration ranges match Material guidelines (100-300ms)
  - Easing curves mirror Material's standard/emphasized/accelerated

  Apple HIG Alignment: ✅
  - Reduced motion support mandatory
  - Subtle, purposeful animations
  - Performance-first approach

  WCAG 2.1 Compliance: ✅
  - Reduced motion support (2.3.3)
  - Non-blocking animations
  - User control respected

  Implementation Example

  React (Framer Motion):
  <motion.div
    initial={{ opacity: 0, y: '1rem' }}
    animate={{ opacity: 1, y: 0 }}
    transition={{
      duration: tokens.motion.durations.medium / 1000,
      ease: tokens.motion.easing.standard
    }}
  />

  HTMX (CSS Transitions):
  <div class="transition-all duration-[200ms] ease-standard
              opacity-0 translate-y-4 htmx-swapping:opacity-100
              htmx-swapping:translate-y-0">

  Production Readiness

  Completeness: ⭐⭐⭐⭐ (Missing loading/error/success states)
  Clarity: ⭐⭐⭐⭐⭐ (Exceptionally clear)
  Accessibility: ⭐⭐⭐⭐⭐ (Reduced motion built-in)
  Performance: ⭐⭐⭐⭐⭐ (300ms limit enforced)
  Framework Support: ⭐⭐⭐⭐⭐ (React, HTMX, Jinja2 covered)

  Assessment

  This is a production-grade motion system specification that demonstrates:
  - Deep understanding of animation best practices
  - Accessibility awareness (reduced motion)
  - Performance consciousness (duration limits)
  - Framework-agnostic design
  - Token-driven consistency

  Role in System: This is the animation governance layer that ensures all UI Factory outputs have consistent, professional motion regardless of rendering technology.

  Recommendation:
  - Deploy as-is for core animations ✅
  - Enhancement: Add loading/error/success state animations
  - Enhancement: Add animation chaining rules
  - Enhancement: Add z-index management during shared element transitions

  Critical Success: The reduced motion support (Section 8) makes this WCAG-compliant out of the box, which is often overlooked in design systems.

● Ran 3 stop hooks

> next one.. then stop

● Read(.mcp_prompts\implementation\instructions\web-ui\openapi_ui_model_conversion_rules.md)
  ⎿  Read 234 lines

● Review: openapi_ui_model_conversion_rules.md

  Structure & Purpose

  This is a deterministic conversion specification (234 lines) that defines the exact rules for transforming OpenAPI specifications into UI Model JSON. This is the brain of the UI Factory - the
  intelligence layer that interprets API contracts and generates appropriate user interfaces.

  Architecture Overview

  Three-Phase Pipeline (lines 8-38):
  1. Extract: Parse OpenAPI structure
  2. Interpret: Apply UI heuristics
  3. Generate: Output UI Model JSON

  This is a classic ETL pattern (Extract-Transform-Load) adapted for UI generation.

  Content Breakdown

  Section 1: High-Level Overview (30 lines)
  - Clear phase separation
  - Defines inputs (OpenAPI) and outputs (UI Model)
  - Establishes deterministic transformation requirement

  Section 2: Tag → Page Mapping (13 lines)
  - Tags become logical modules
  - Automatic CRUD page generation
  - Fallback strategy (use path segments if no tags)
  - Smart: Creates index/create/details/edit automatically

  Section 3: Operation → Page Type Rules (28 lines) ⭐ Core Mapping Logic
  - GET collection → List Page (table/cards/list)
  - GET single → Detail Page (key/value blocks)
  - POST → Create Form
  - PUT/PATCH → Edit Form
  - DELETE → Delete Action with confirmation

  Section 4: Schema → UI Component Rules (23 lines)
  - Primitive mapping table (critical reference)
  - Enum handling (dropdown/radio based on length)
  - Array handling (tags vs nested tables)
  - Object handling (accordions/tabs)

  Section 5: Layout Mapping Rules (17 lines)
  - Page-type-specific layout assignments
  - Responsive breakdowns per page type
  - Auto-generated metadata grids for detail pages

  Section 6: Action Mapping Rules (18 lines)
  - HTTP method → UI action mapping
  - Primary/secondary action patterns
  - DELETE requires confirmation modal
  - Semantic color injection (red for destructive)

  Section 7: Routing Rules (13 lines)
  - RESTful routing convention
  - ID inference logic
  - Consistent URL patterns

  Section 8: Responsive Rules (15 lines)
  - Layout transformation breakpoints
  - Table → Cards → List cascade
  - Form column collapsing strategy
  - Detail page accordion stacking

  Section 9: Behaviour Rules (13 lines)
  - Pagination auto-detection
  - Search field inference
  - Filter generation from query params
  - Sorting enablement

  Section 10: Security Rules (5 lines)
  - Protected route flagging
  - Login-required wrapper generation

  Section 11: Final Output Shape (16 lines)
  - JSON structure example
  - Shows actual UI Model format

  Strengths

  ✅ Deterministic: Every OpenAPI pattern maps to exactly one UI pattern
  ✅ Complete CRUD Coverage: Automatically generates all standard pages
  ✅ Smart Defaults: Responsive breakdowns built-in
  ✅ RESTful Alignment: Follows REST conventions
  ✅ Behavior Inference: Auto-detects pagination, search, filtering
  ✅ Security Aware: Handles authentication requirements
  ✅ Primitive Type Coverage: All OpenAPI types mapped

  Critical Mapping Tables

  Schema → Component Mapping (lines 89-97):
  string              → text field
  string (email)      → email field
  string (date)       → date picker
  string (uri)        → link field
  number/integer      → number field
  boolean             → toggle switch

  Operation → Page Type (lines 58-85):
  GET /pets           → List Page (table/cards/list)
  GET /pets/{id}      → Detail Page (key/value)
  POST /pets          → Create Form
  PUT /pets/{id}      → Edit Form (prefilled)
  DELETE /pets/{id}   → Delete Action (with modal)

  Layout Cascading (lines 172-174):
  viewport ≥ md       → table
  viewport < md       → cards
  viewport < sm       → list

  Smart Heuristics

  Pagination Auto-Detection (lines 188-190):
  Response contains: {
    "page": 1,
    "limit": 20,
    "offset": 0,
    "total": 100
  }
  → Pagination UI auto-enabled

  Search Auto-Detection (lines 192-194):
  Query params contain: q, search, keyword
  → Search bar auto-generated

  Enum Component Selection (lines 99-100):
  enum.length <= 3   → radio group
  enum.length <= 8   → segmented control
  enum.length > 8    → dropdown

  CRUD Pattern Recognition

  Tag: "pets" generates:
  /pets              → index (list all)
  /pets/create       → create form
  /pets/{id}         → detail view
  /pets/{id}/edit    → edit form
  + DELETE action on list rows

  This is automatic scaffolding from OpenAPI spec.

  Responsive Strategy

  List Pages (lines 117-120):
  - Desktop: Full table with all columns
  - Tablet: Card grid (2-3 columns)
  - Mobile: Vertical list (1 column)

  Form Pages (lines 177-179):
  - Desktop: 2-3 column layout
  - Tablet: 2 column layout
  - Mobile: Single column stack

  Detail Pages (lines 181-183):
  - Desktop: Multi-column summary grids
  - Mobile: Stacked accordions

  Security Integration

  Protected Routes (lines 204-208):
  /api/admin/users:
    security:
      - bearerAuth: []

  → UI Model Output:
  {
    "route": "/admin/users",
    "protected": true,
    "authRequired": "bearerAuth"
  }

  Integration with MCP Protocol

  This file is referenced in mcp_ui_factory_protocol.md Stage 2:
  Stage 2 – UI Model Generation (Creator)
    Uses: openapi_ui_model_conversion_rules.md
    Produces: ui-model.json

  Gaps & Observations

  ⚠️ Missing Rules:
  - No file upload field mapping (multipart/form-data)
  - No rich text editor mapping (text with format: markdown/html)
  - No image/media field handling
  - No validation rule mapping (min/max/pattern)
  - No relationship visualization (foreign keys, references)
  - No bulk action generation (select all, bulk delete)
  - No export functionality (CSV, PDF downloads)

  ⚠️ Ambiguities:
  - "Enum length" decision thresholds (lines 99-100) - exact numbers could be specified
  - "Long or complex objects" for tabs (line 110) - needs concrete threshold
  - Array handling (line 104) - when to choose nested table vs cards?

  ✅ By Design:
  - High-level rules allow implementation flexibility
  - Edge cases handled by validator/judge in MCP protocol
  - Focus on common 80% use cases

  Real-World Example

  Input OpenAPI:
  paths:
    /api/users:
      get:
        tags: [users]
        responses:
          200:
            content:
              application/json:
                schema:
                  type: array
                  items:
                    properties:
                      id: {type: integer}
                      name: {type: string}
                      email: {type: string, format: email}
                      role: {type: string, enum: [admin, user, guest]}
                      active: {type: boolean}

  Output UI Model:
  {
    "pages": [{
      "route": "/users",
      "type": "list",
      "layout": "table",
      "responsive": {
        "md": "cards",
        "sm": "list"
      },
      "fields": [
        {"name": "id", "component": "number"},
        {"name": "name", "component": "text"},
        {"name": "email", "component": "email"},
        {"name": "role", "component": "segmented-control", "options": ["admin","user","guest"]},
        {"name": "active", "component": "toggle"}
      ],
      "actions": [],
      "behavior": {
        "sorting": true,
        "pagination": true
      }
    }]
  }

  Production Readiness

  Completeness: ⭐⭐⭐⭐ (Missing file upload, validation rules, bulk actions)
  Clarity: ⭐⭐⭐⭐⭐ (Exceptionally clear)
  Determinism: ⭐⭐⭐⭐⭐ (Fully deterministic)
  Coverage: ⭐⭐⭐⭐ (Covers 80% of common use cases)
  REST Alignment: ⭐⭐⭐⭐⭐ (Perfect REST conventions)

  Assessment

  This is a production-grade conversion specification that provides:
  - Deterministic mapping from API to UI
  - Smart defaults for common patterns
  - Automatic CRUD scaffolding
  - Responsive behavior built-in
  - Security awareness

  Role in System: This is the intelligence layer that transforms API contracts into complete UI specifications. It's what makes the UI Factory "smart" rather than just a template engine.

  Recommendation:
  - Deploy as-is for MVP ✅
  - Enhancement: Add file upload field handling
  - Enhancement: Add validation rule mapping (min/max/pattern → UI hints)
  - Enhancement: Add bulk action generation rules
  - Enhancement: Specify exact enum thresholds (radio vs dropdown)

  Critical Success: The automatic CRUD page generation (Section 2) is the killer feature. From a single OpenAPI spec with proper tags, this generates complete admin panels automatically.

  ---
  Stopping as requested.

● Ran 3 stop hooks

> next md file then halt

● Read(.mcp_prompts\implementation\instructions\web-ui\renderer_mapping_spec.md)
  ⎿  Read 299 lines

● Review: renderer_mapping_spec.md

  Structure & Purpose

  This is a cross-framework component mapping specification (299 lines) that defines how logical UI components (UCMP - Universal Component Mapping Protocol) translate into concrete React and HTMX/Jinja2
  implementations. This is the translation layer between abstract UI definitions and actual code.

  Architecture Overview

  UCMP Pattern (Universal Component Mapping Protocol):
  Logical Component → [Renderer] → React TSX | HTMX/Jinja2
                           ↓
                    layout.tokens.json

  Dual Token System (lines 36-40):
  - Primary Token: Desktop/tablet (elevated, standard density)
  - Secondary Token: Mobile/compact (flat, reduced density)

  This ensures responsive component variants without layout shifts.

  Content Breakdown

  Section 1: Core Principles (31 lines)
  - 1.1 Logical Components First: UCMP as source of truth
  - 1.2 Renderer-Agnostic Flow: 5-step transformation pipeline
  - 1.3 Dual Token Enforcement: Primary/secondary for different contexts
  - 1.4 Naming Consistency: Predictable name transformations

  Section 2: Directory Structure (29 lines)
  - React structure: Component categorization (forms/display/layout)
  - Jinja2 structure: Templates + macros separation
  - Clear separation of concerns

  Section 3: Logical → React Mapping (82 lines) ⭐ React Implementation
  - 5 core components with primary/secondary variants
  - 3.1 Text Field: Standard vs compact
  - 3.2 Select: Dropdown vs searchable
  - 3.3 Boolean: Toggle vs checkbox
  - 3.4 Table: Full table vs mobile list
  - 3.5 Cardlist: Elevated vs bordered

  Section 4: Logical → HTMX/Jinja2 Mapping (64 lines) ⭐ Jinja2 Implementation
  - Parallel structure to React mappings
  - Jinja macro syntax
  - Same component set with equivalent variants

  Section 5: HTMX Interaction Rules (25 lines)
  - Submit-on-change pattern
  - Live search with debouncing
  - Table pagination with hx-get
  - Key Feature: Progressive enhancement

  Section 6: Responsive Token Behaviour (12 lines)
  - Breakpoint-based token selection
  - Hook-based (React) vs macro-based (Jinja2)
  - Width-dependent component variant switching

  Section 7: Motion Mapping (9 lines)
  - Transition assignments per component type
  - Tailwind token usage
  - Cross-renderer consistency

  Section 8: Error Handling (6 lines)
  - Fallback strategy for unmapped components
  - Build artifact warnings

  Strengths

  ✅ Framework Parity: React and Jinja2 get equivalent implementations
  ✅ Dual Token System: Responsive variants built-in
  ✅ HTMX Integration: Progressive enhancement patterns included
  ✅ Naming Consistency: Predictable transformations (snake_case ↔ PascalCase)
  ✅ Directory Standards: Clear project structure conventions
  ✅ Error Resilience: Fallback strategy prevents build failures
  ✅ Motion Integration: Animation patterns specified

  Key Mapping Examples

  Text Field Dual Token:
  Primary (Desktop):
    className="w-full px-3 py-2 rounded-md shadow-sm bg-white border border-gray-200"

  Secondary (Mobile):
    className="w-full px-2 py-1 rounded border bg-gray-50"

  Visual Difference:
  - Primary: More padding (py-2 vs py-1), elevation (shadow-sm), distinct border
  - Secondary: Compact spacing, flat appearance, lighter background

  Boolean Component Variants:
  Primary:   Toggle (modern, space-efficient)
  Secondary: Checkbox (compact, traditional)

  Strategic: Toggle for important settings, checkbox for bulk selections.

  Table Responsive Strategy:
  Desktop:  <Table columns={columns} data={data} />
  Mobile:   <MobileList data={data} />

  Transformation: Full table → collapsible list items (completely different component).

  HTMX Progressive Enhancement

  Live Search Pattern (lines 244-250):
  hx-get="/api/search"
  hx-trigger="input changed delay:300ms"
  hx-target="#results"
  hx-swap="outerHTML"

  Features:
  - 300ms debounce prevents excessive requests
  - Target-specific updates (partial page replacement)
  - Works without JavaScript (degrades to form submission)

  Table Pagination (lines 253-257):
  hx-get="/api/list?page={{ page }}"
  hx-trigger="click"
  hx-target="#table"

  Benefits:
  - No page reload
  - Preserves scroll position
  - SEO-friendly (server-rendered)

  Responsive Token Selection Logic

  Algorithm (lines 263-268):
  if width < sm:
      use secondary (all components)
  elif width < md:
      use secondary for heavy components (table, cardlist)
  else:
      use primary

  Implementation Hooks:
  // React
  const variant = useResponsiveTokens()

  // Jinja2
  {{ apply_responsive(component, context) }}

  Component Coverage

  Forms (3 components):
  - Text Field (with validation)
  - Select Dropdown (with search variant)
  - Boolean (toggle/checkbox)

  Display (2 components):
  - Table (with mobile list fallback)
  - Cardlist (elevated/bordered variants)

  Missing Components ⚠️:
  - Date Picker
  - File Upload
  - Multi-Select
  - Rich Text Editor
  - Image Display
  - Progress Indicators
  - Tabs/Accordions
  - Modal/Dialog
  - Toast/Alert

  Integration with Other Specs

  | File                                    | Relationship to renderer_mapping_spec.md |
  |-----------------------------------------|------------------------------------------|
  | universal_component_mapping_protocol.md | Source - Defines UCMP logical components |
  | layout_tokens.json                      | Input - Token values for styling         |
  | motion_transition_spec.md               | Referenced - Animation patterns          |
  | mcp_ui_factory_protocol.md              | Consumed by - Stage 4 code generation    |

  Directory Structure Comparison

  React (lines 54-63):
  src/
    components/
      forms/      ← TextField, Select, Toggle
      display/    ← Table, CardList
      layout/     ← Shell, Container
    pages/        ← Generated page components
    hooks/        ← useResponsiveTokens()
    utils/        ← Helper functions

  HTMX/Jinja2 (lines 66-80):
  templates/
    pages/        ← Page templates
    components/   ← Component includes
  macros/
    forms.jinja   ← text_field(), select()
    display.jinja ← table(), cardlist()
    layout.jinja  ← container(), shell()
  static/
    js/           ← HTMX enhancements
    css/          ← Tailwind output

  Symmetry: Both follow same categorization (forms/display/layout).

  Code Generation Examples

  React Component Generation:
  // From UI Model:
  { component: "text_field", props: { name: "email", label: "Email" } }

  // Generates:
  <TextField
    label="Email"
    name="email"
    className="w-full px-3 py-2 rounded-md shadow-sm bg-white border"
  />

  Jinja2 Macro Generation:
  {# From same UI Model #}
  {{ text_field(
      label="Email",
      name="email",
      class="w-full px-3 py-2 rounded-md shadow-sm bg-white border"
  ) }}

  Gaps & Observations

  ⚠️ Missing Specifications:
  - No validation error display mapping
  - No loading state variants
  - No disabled state handling
  - No aria-label/accessibility attribute mapping
  - No form submission patterns (React onSubmit vs HTMX hx-post)
  - Limited component library (only 5 components)

  ⚠️ Incomplete Patterns:
  - Section 7 mentions motion mapping but lacks specific examples
  - No color token mapping (uses hardcoded classes like bg-white)
  - No dark mode variants specified

  ✅ Smart Design:
  - Dual token system solves responsive density problem elegantly
  - HTMX debouncing (delay:300ms) shows production awareness
  - Fallback to text_field_secondary prevents catastrophic failures

  Naming Convention Verification

  Rule (lines 42-47):
  Logical          React       Jinja2
  text_field   →   TextField   text_field()
  select       →   Select      select()
  cardlist     →   CardList    cardlist()

  Pattern:
  - Logical: snake_case (data format)
  - React: PascalCase (component standard)
  - Jinja2: snake_case (Python convention)

  Consistency: ✅ Follows language/framework conventions.

  Production Readiness

  Completeness: ⭐⭐⭐ (Only 5 components, missing common patterns)
  Clarity: ⭐⭐⭐⭐⭐ (Exceptionally clear examples)
  Framework Parity: ⭐⭐⭐⭐⭐ (React ≈ Jinja2 feature parity)
  Responsiveness: ⭐⭐⭐⭐⭐ (Dual token system is brilliant)
  HTMX Integration: ⭐⭐⭐⭐⭐ (Progressive enhancement done right)

  Assessment

  This is a production-grade renderer specification that demonstrates:
  - Cross-framework consistency (React/HTMX parity)
  - Responsive design via dual token system
  - Progressive enhancement through HTMX patterns
  - Naming conventions that respect framework idioms

  Role in System: This is the code generation bridge between abstract UI Model JSON and concrete React/Jinja2 implementations. It ensures both renderers produce functionally equivalent UIs.

  Critical Innovation: The dual token system (primary/secondary) solves the responsive component density problem without requiring media query duplication in every component.

  Recommendation:
  - Expand component library to 20+ components (date picker, file upload, modal, etc.)
  - Add validation error mapping (crucial for forms)
  - Specify dark mode variants
  - Add accessibility attribute mapping (aria-label, role, etc.)
  - Deploy current 5 components as MVP ✅

  Unique Strength: HTMX integration with debouncing, targeting, and swap strategies shows this isn't just a React-first system with Jinja2 bolted on - it's truly dual-renderer from the ground up.

  ---
  Halting as requested.

● Ran 3 stop hooks

> review the next md file then halt

● Read(.mcp_prompts\implementation\instructions\web-ui\responsive_layout_developer_workflow.md)
  ⎿  Read 216 lines

● Review: responsive_layout_developer_workflow.md

  Structure & Purpose

  This is a technical implementation guide (216 lines) for developers building adaptive multi-format UI layouts. It defines the engineering architecture, code patterns, and decision logic needed to make
  layouts transform intelligently between tables, grids, cards, lists, accordions, and carousels.

  Architecture Overview

  Layout Manager Pattern (lines 17-24):
  - Central orchestrator that evaluates multiple factors
  - Container dimensions (not viewport)
  - Data density analysis
  - Component constraints
  - Interaction mode (touch vs desktop)
  - Visibility priorities

  Module Structure (lines 25-38):
  /layout
    ├─ useContainerQuery.ts       (measures container width)
    ├─ useDensityEvaluator.ts     (analyzes data complexity)
    ├─ responsiveLayoutHandler.ts (central decision engine)
    ├─ layoutTypes.ts             (type definitions)
    ├─ componentRegistry.ts       (component specs)
    └─ transformers/              (layout conversion functions)

  This is a well-architected module system with clear separation of concerns.

  Content Breakdown

  Section 2: Architecture Overview (23 lines)
  - Layout Manager as single decision point
  - 5 input factors for layout decisions
  - Module structure with functional organization

  Section 3: Component Contract (18 lines) ⭐ Critical Pattern
  - Every component must export constraints
  - Defines minimum widths, optimal widths, collapse thresholds
  - Declares supported layout types
  - Smart: Self-documenting component capabilities

  Section 4: Container Query Logic (15 lines)
  - Hook-based width measurement
  - Threshold-based layout selection
  - Waterfall logic (most constrained first)

  Section 5: Density Evaluation (21 lines)
  - Algorithm for analyzing data complexity
  - Considers columns, media, semantic indicators
  - Density-driven layout selection

  Section 6: Responsive Layout Handler (17 lines)
  - Central orchestration flow
  - 5-level priority resolution
  - Combines container + density + interaction mode

  Section 7: Layout Transformations (28 lines)
  - Pure functions for each transformation
  - Specific operations per transformation type
  - Clear semantic naming

  Section 8: Tailwind Implementation (17 lines)
  - Container query plugin usage
  - CSS utility examples
  - Adaptive grid patterns

  Section 9: Interaction Mode Recognition (11 lines)
  - Desktop vs mobile differences
  - Input to layout resolution

  Section 10: Declarative Layout API (9 lines)
  - Component interface example
  - Props-based configuration

  Section 11: Accessibility Workflow (6 lines)
  - Reading order preservation
  - ARIA attributes
  - Semantic structure maintenance

  Section 12: Final Principle (3 lines)
  - Philosophical anchor
  - Container-aware responsiveness emphasis

  Strengths

  ✅ Container Queries: Modern approach (not viewport-based)
  ✅ Pure Functions: Transformations are predictable and testable
  ✅ Component Contracts: Self-documenting constraints
  ✅ Density Analysis: Smart layout selection beyond just screen size
  ✅ Declarative API: Simple component interface
  ✅ Accessibility Built-In: ARIA and semantic structure preserved
  ✅ Tailwind Integration: Practical CSS implementation patterns

  Key Algorithms

  Threshold Logic (lines 70-76):
  if (width < ComponentSpec.minWidth) return "list";         // < 240px
  if (width < ComponentSpec.collapseThreshold) return "accordion";  // < 280px
  if (width < ComponentSpec.optimalWidth) return "cards";    // < 320px
  return "grid";                                             // >= 320px

  Cascade Pattern: Most constrained layout first, progressively more spacious.

  Density Evaluation (lines 88-98):
  function evaluateDensity(data) {
    const columns = estimateColumns(data);
    const hasImages = detectMedia(data);
    const hasStatuses = detectSemantic(data);

    if (columns > 5) return "table";    // High info density
    if (columns >= 3) return "grid";    // Medium density
    if (hasImages) return "cards";      // Visual content
    return "list";                      // Low density
  }

  Smart: Analyzes data structure, not just dimensions.

  Resolution Priority (lines 114-119):
  1. Must-fit constraints       (physical impossibility)
  2. Component minimum thresholds  (component-defined)
  3. Density requirements       (data-driven)
  4. Interaction mode          (touch vs mouse)
  5. Developer override        (explicit preference)

  This is a well-thought-out conflict resolution hierarchy.

  Layout Transformations

  Table → Cards (lines 126-131):
  flattenColumns();                  // Convert table rows to objects
  wrapIntoCard();                    // Apply card component wrapper
  ensurePrimaryContentVisible();     // Prioritize key fields

  Cards → List (lines 133-138):
  reduceVisualNoise();     // Remove decorative elements
  stackVertically();       // Change flex direction
  adjustImageSize();       // Reduce image prominence

  List → Accordion (lines 140-145):
  wrapContentInPanels();           // Create collapsible sections
  addExpandCollapse();             // Add toggle interaction
  promotePrimaryFieldAsHeader();   // Make primary field the summary

  Grid → Carousel (lines 147-151):
  convertColumnsToScrollRow();  // Horizontal overflow scroll
  maintainCardSpacing();        // Preserve card gaps

  Each transformation has semantic clarity - the function names describe what happens.

  Tailwind Container Query Pattern

  Structural Example (lines 159-166):
  @container card (min-width: 320px) {
    .card-grid { @apply grid grid-cols-2; }
  }

  @container card (max-width: 319px) {
    .card-grid { @apply flex flex-col; }
  }

  Modern CSS: Uses @container instead of @media, enabling component-level responsiveness.

  Utility Rules (lines 169-172):
  min-w-[240px]                              /* Card minimums */
  grid-cols-[auto-fit,_minmax(240px,_1fr)]  /* Adaptive grids */
  flex-col md:flex-row                       /* Orientation shift */

  Component Contract Example

  Specification Object (lines 44-57):
  export const ComponentSpec = {
    minWidth: 240,              // Absolute minimum
    optimalWidth: 320,          // Ideal size
    maxColumns: 4,              // Grid constraint
    collapseThreshold: 280,     // Accordion trigger
    preferredLayout: "cards",   // Default choice
    supports: {                 // Capability flags
      table: true,
      grid: true,
      cards: true,
      list: true,
      accordion: true,
    }
  };

  Benefits:
  - Self-documenting capabilities
  - Enables runtime validation
  - Layout manager can query support before transformation

  Declarative API Design

  Component Interface (lines 192-199):
  <ResponsiveLayout
    data={items}
    preferred="cards"      // Developer preference
    fallback="list"        // Safety net
    enableTransitions      // Motion system
  />

  Developer Experience:
  - Simple props-based API
  - No complex configuration
  - Framework handles complexity

  Accessibility Workflow

  Requirements (lines 204-208):
  - Reading order: Transformations preserve logical flow
  - ARIA attributes: aria-expanded for accordions
  - Semantic structure: Heading levels maintained
  - Status colors: Consistent across layouts

  Critical: Layout changes don't break screen readers.

  Integration with Other Specs

  | File                            | Relationship to responsive_layout_developer_workflow.md |
  |---------------------------------|---------------------------------------------------------|
  | responsive_layout_principles.md | Source - Design philosophy backing this workflow        |
  | renderer_mapping_spec.md        | Implements - Uses layout transformations                |
  | layout_tokens.json              | Input - Width thresholds, breakpoints                   |
  | motion_transition_spec.md       | Consumes - enableTransitions uses motion tokens         |
  | mcp_ui_factory_protocol.md      | Referenced - Stage 4 code generation                    |

  Gaps & Observations

  ⚠️ Missing Implementations:
  - No actual code for estimateColumns(), detectMedia(), detectSemantic()
  - No type definitions shown (only references layoutTypes.ts)
  - No error handling patterns
  - No loading state management during transformations
  - No caching strategy for density evaluation

  ⚠️ Incomplete Patterns:
  - Section 9 (Interaction Mode) mentions it contributes to layout but doesn't show how
  - No example of resolveFinalLayout() conflict resolution
  - No explanation of what "developer override" means in practice

  ✅ Intentional Abstraction:
  - This is a workflow guide, not implementation code
  - Shows patterns developers should follow
  - Detailed implementation left to framework-specific code

  Real-World Usage Example

  Scenario: Product listing page

  // 1. Component defines constraints
  export const ProductCardSpec = {
    minWidth: 280,
    optimalWidth: 340,
    maxColumns: 3,
    collapseThreshold: 300,
    preferredLayout: "cards",
    supports: { table: true, grid: true, cards: true, list: true }
  };

  // 2. Hook measures container
  const { width } = useContainerQuery(containerRef);

  // 3. Density evaluation
  const density = evaluateDensity(products);
  // products has 6 fields + images → density = "grid"

  // 4. Layout handler resolves
  const layout = responsiveLayoutHandler(width, density, "desktop");
  // width = 800px, density = "grid", mode = "desktop"
  // → final layout = "grid"

  // 5. Render appropriate component
  {layout === "grid" && <ProductGrid items={products} />}
  {layout === "cards" && <ProductCards items={products} />}
  {layout === "list" && <ProductList items={products} />}

  Production Readiness

  Completeness: ⭐⭐⭐⭐ (Missing actual implementations, but patterns clear)
  Clarity: ⭐⭐⭐⭐⭐ (Exceptionally clear workflow)
  Modern Patterns: ⭐⭐⭐⭐⭐ (Container queries, hooks, pure functions)
  Accessibility: ⭐⭐⭐⭐⭐ (Built into workflow)
  Developer Experience: ⭐⭐⭐⭐⭐ (Declarative API)

  Assessment

  This is a production-grade developer workflow specification that demonstrates:
  - Modern CSS patterns (container queries)
  - Functional programming (pure transformation functions)
  - Component-driven architecture (contracts, constraints)
  - Data-driven decisions (density evaluation)
  - Accessibility-first (semantic structure preservation)

  Role in System: This is the implementation blueprint for developers building the responsive layout engine. It bridges design principles and actual code.

  Critical Innovation: The Component Contract pattern (Section 3) is brilliant - components self-declare their capabilities and constraints, enabling the layout manager to make intelligent decisions
  without hard-coding knowledge about every component type.

  Recommendation:
  - Use as developer guide ✅
  - Add code examples for estimateColumns(), detectMedia(), density caching
  - Add TypeScript interfaces for ComponentSpec, LayoutTypes
  - Add error handling patterns (what happens when no layout fits?)
  - Add performance guidelines (when to memoize density evaluation)

  Unique Strength: This workflow emphasizes container queries over media queries, which is the modern approach to component-level responsiveness. Most design systems still use viewport-based breakpoints
  exclusively.

  ---
  Halting as requested.

● Ran 3 stop hooks

> review the next the halt

● Read(.mcp_prompts\implementation\instructions\web-ui\responsive_layout_principles.md)
  ⎿  Read 153 lines

● Review: responsive_layout_principles.md

  Structure & Purpose

  This is a design philosophy and principles document (153 lines) that establishes the conceptual foundation for responsive layout systems. It's the "why" before the "how" - defining philosophical
  principles before implementation details. This pairs with responsive_layout_developer_workflow.md (which provides the technical "how").

  Architecture Overview

  Living Structure Philosophy (lines 3-10):
  - Not static breakpoints, but dynamic adaptation
  - Responds to: data density, container integrity, user intent, interaction models
  - Four core characteristics: rearranges purposefully, preserves hierarchy, adapts intelligently, maintains consistency

  Content Breakdown

  Section 1: Overarching Philosophy (11 lines)
  - Establishes "living structure" metaphor
  - Context-aware, information-driven design
  - Sets philosophical tone for entire system

  Section 2: Core Principles (56 lines) ⭐ Heart of Document
  - 15 principles covering all aspects of responsive design
  - Ranges from high-level philosophy to specific patterns
  - Each principle is concise (1-3 lines)

  Section 3: Developer Workflow Methodologies (78 lines)
  - 10 workflow patterns for implementation
  - Bridges philosophy → practice
  - Includes code examples and API designs

  Section 4: Closing Principle (3 lines)
  - Philosophical anchor
  - Reinforces core message

  The 15 Core Principles

  2.1 Information Hierarchy First (line 16-17)
  - Content priority drives structure
  - Philosophy: "What matters most" precedes "what fits"

  2.2 Density Dictates Format (lines 19-23)
  - Layout selection based on information density
  - Clear mapping: high→table, medium→grid, low→cards, extreme→accordion

  2.3 Semantic Consistency (lines 25-26)
  - Meaning preserved across layout transformations
  - Critical: CTA remains primary regardless of layout type

  2.4 Readability Before Composition (lines 28-29)
  - Change layout rather than compress
  - Anti-pattern: Squeezing elements to maintain visual structure

  2.5 Layout Transformation Rules (lines 31-37)
  - Five predictable transformations
  - Forms the transformation graph

  2.6 Minimum Viable Dimensions (lines 39-40)
  - Component-level constraints
  - Prevents layout degradation

  2.7 Container Queries Over Breakpoints (lines 42-43)
  - Modern approach: Component-aware, not viewport-aware
  - Key innovation of this system

  2.8 Interaction-Based Adaptation (lines 45-47)
  - Desktop vs mobile input models
  - Hover vs tap-first design

  2.9 Context-Specific Views (lines 49-50)
  - Simplified summaries for small screens
  - Drill-down details when needed

  2.10 Smooth Transitional Behaviour (lines 52-53)
  - Visual consistency during transformations
  - Non-jarring motion

  2.11 Layout Manager Architecture (lines 55-56)
  - Centralized decision engine
  - Multiple input factors

  2.12 Declarative Responsive Logic (lines 58-59)
  - Describe "what" not "how"
  - Configuration over code

  2.13 Content Visibility Priorities (lines 61-62)
  - Three-tier hierarchy: Must/Should/Nice
  - Progressive disclosure pattern

  2.14 Transformation Mapping (lines 64-65)
  - Bidirectional transformations
  - Predictable behavior

  2.15 Systemic Design Approach (lines 67-68)
  - System of relationships, not collection of screens
  - Core philosophy: Responsive as a system

  Developer Workflow Methodologies (10 Patterns)

  3.1 Responsive Layout Handler (lines 74-78)
  - Central manager pattern
  - Three responsibilities: measure, evaluate, select

  3.2 Define Component Minimums (lines 80-87)
  minWidth             (absolute minimum)
  maxColumns           (grid constraint)
  collapseThreshold    (accordion trigger)
  truncateRules        (text overflow handling)

  3.3 Layout Priority Logic (lines 89-94)
  - Waterfall decision tree
  - Progressive degradation pattern

  3.4 Tailwind Utility Strategy (lines 96-100)
  - Container query plugin dependency
  - Specific utility patterns for adaptive grids

  3.5 Data Density Heuristics (lines 102-110)
  - Five evaluation criteria
  - Input to layout selection algorithm

  3.6 Decoupled View Components (lines 112-119)
  - Multiple representations per content type
  - Layout handler as renderer selector

  3.7 Smooth Transitions (lines 121-122)
  - Opacity + size transitions
  - Visual reinforcement of transformations

  3.8 Interaction Modes (lines 124-132)
  - Desktop: hover, inline menus, wider actions
  - Mobile: tap, sticky footers, collapsible sections

  3.9 Accessibility in Responsive Systems (lines 134-137)
  - Large tap areas
  - Reading order preservation
  - ARIA attributes for interactive elements

  3.10 Declarative API (lines 139-146)
  <ResponsiveLayout
    data={items}
    density="auto"      // Automatic density evaluation
    fallback="list"     // Safety layout
  />

  Strengths

  ✅ Philosophical Foundation: Establishes "why" before "what"
  ✅ Comprehensive Coverage: 15 principles cover all aspects
  ✅ Bridges Theory → Practice: Section 3 connects philosophy to code
  ✅ Container Query Focus: Modern CSS approach emphasized
  ✅ Accessibility Included: Not an afterthought
  ✅ Declarative API Design: Simple developer interface
  ✅ Semantic Consistency: Meaning preserved across transformations

  Transformation Graph

  From principles 2.2, 2.5, and 3.3:

  Table (high density, >5 columns)
    ↓ (container shrinks)
  Cards (medium density, 3-5 columns)
    ↓ (container shrinks further)
  List (low density, vertical stack)
    ↓ (extreme constraint)
  Accordion (collapsible panels)

  Grid (spatial arrangement)
    → Carousel (horizontal scroll)

  Reversible: Each transformation can reverse when constraints relax.

  Density Heuristics

  Five Factors (lines 103-108):
  1. numColumns: Number of data fields
  2. cellContentLength: Text length per field
  3. hasImages: Visual content presence
  4. needsStatuses: Semantic indicators (success/error/warning)
  5. interactionType: Touch vs mouse input

  Algorithm:
  if (numColumns > 5) → table
  if (numColumns >= 3 && !hasImages) → grid
  if (hasImages || cellContentLength > 50) → cards
  else → list

  Comparison to responsive_layout_developer_workflow.md

  | Aspect       | responsive_layout_principles.md | responsive_layout_developer_workflow.md |
  |--------------|---------------------------------|-----------------------------------------|
  | Focus        | Philosophy & "Why"              | Implementation & "How"                  |
  | Audience     | Designers + Architects          | Developers                              |
  | Code Level   | Pseudo-code examples            | Module structure + hooks                |
  | Length       | 153 lines                       | 216 lines                               |
  | Principles   | 15 design principles            | Component contracts + algorithms        |
  | Relationship | Foundation                      | Implementation guide                    |

  Together they form: Design Philosophy → Technical Specification

  Container Queries Emphasis

  Principle 2.7 (lines 42-43):
  Layout responds to its container, not global screen width.

  Why Critical:
  - Same component can have different layouts in different containers
  - Sidebar: table → list (narrow container)
  - Main content: table → cards (wide container)
  - Modern CSS (@container) support required

  Contrast with Traditional:
  /* Old way - viewport-based */
  @media (max-width: 768px) {
    .product-grid { /* changes everywhere */ }
  }

  /* New way - container-based */
  @container (max-width: 768px) {
    .product-grid { /* changes only in this container */ }
  }

  Content Visibility Hierarchy

  Principle 2.13 (lines 61-62):
  Must Show    → id, title, primary CTA (always visible)
  Should Show  → description, status, secondary actions (desktop+)
  Nice to Show → metadata, tags, timestamps (desktop only)

  Implementation:
  // Desktop
  <Card>
    {mustShow}
    {shouldShow}
    {niceToShow}
  </Card>

  // Mobile
  <ListItem>
    {mustShow}
    {shouldShow}  // conditionally
    {/* niceToShow hidden */}
  </ListItem>

  Interaction Mode Adaptation

  Principle 2.8 (lines 45-47):

  Desktop Characteristics:
  - Hover states reveal actions
  - Inline editing controls
  - Wide information scans (multi-column)

  Mobile Characteristics:
  - Tap-first (no hover states)
  - Stacked layouts (single column)
  - Thumb zone optimization (actions at bottom)

  Design Implication: Can't just "shrink" desktop UI - must redesign for touch.

  Integration with Other Specs

  | File                                    | Relationship to responsive_layout_principles.md |
  |-----------------------------------------|-------------------------------------------------|
  | responsive_layout_developer_workflow.md | Implements - Translates principles to code      |
  | design_system_foundations.md            | Extends - Adds responsive depth to foundations  |
  | renderer_mapping_spec.md                | Guided by - Uses density heuristics             |
  | openapi_ui_model_conversion_rules.md    | Applies - Layout selection uses these rules     |

  Gaps & Observations

  ⚠️ Missing Principles:
  - No principle for loading states during transformations
  - No principle for print layouts
  - No principle for right-to-left (RTL) language support
  - No principle for high-contrast/accessibility modes beyond reading order

  ⚠️ Incomplete Coverage:
  - Section 3.5 lists heuristics but doesn't provide weighting algorithm
  - Section 3.7 mentions transitions but doesn't specify which motion tokens to use
  - Section 3.9 accessibility is brief (only 3 points)

  ✅ By Design:
  - This is a principles document, not implementation
  - Detailed patterns live in companion workflow document
  - Focuses on "what to think about" not "exactly how to code it"

  Real-World Application Example

  Scenario: E-commerce product listing

  Data Analysis:
  numColumns: 6 (image, title, price, rating, stock, actions)
  cellContentLength: 40 (title average)
  hasImages: true
  needsStatuses: true (stock status)
  interactionType: varies

  Layout Selection:
  Desktop (1200px):
    density = high, hasImages = true
    → grid (3-4 columns with cards)

  Tablet (768px):
    density = medium, container narrower
    → cards (2 columns)

  Mobile (375px):
    density = low, container narrow
    → list (1 column, vertical stack)

  Visibility Priorities:
  Must Show:    image, title, price, "Add to Cart"
  Should Show:  rating, stock status
  Nice to Show: brand, category, SKU

  Production Readiness

  Completeness: ⭐⭐⭐⭐ (Covers core principles, minor gaps)
  Clarity: ⭐⭐⭐⭐⭐ (Exceptionally clear)
  Actionability: ⭐⭐⭐⭐⭐ (Principles → practice via Section 3)
  Modern Approach: ⭐⭐⭐⭐⭐ (Container queries, declarative API)
  Comprehensiveness: ⭐⭐⭐⭐ (15 principles cover most scenarios)

  Assessment

  This is a production-grade design principles document that:
  - Establishes philosophy before implementation
  - Provides 15 actionable principles covering responsive design holistically
  - Bridges theory and practice with developer workflow section
  - Emphasizes modern patterns (container queries, declarative APIs)
  - Includes accessibility from the start

  Role in System: This is the philosophical foundation that informs all responsive layout decisions. It's what designers reference when making layout choices and what developers implement in code.

  Critical Innovation: The emphasis on container queries over breakpoints (Principle 2.7) positions this system as modern and component-centric rather than page-centric.

  Recommendation:
  - Use as design reference ✅
  - Pair with responsive_layout_developer_workflow.md for complete guidance
  - Enhancement: Add principle for loading state transformations
  - Enhancement: Expand accessibility section (add contrast modes, RTL)
  - Enhancement: Add weighting algorithm for density heuristics (Section 3.5)

  Unique Strength: The three-tier visibility hierarchy (Must/Should/Nice - Principle 2.13) is a simple yet powerful pattern for progressive disclosure that most design systems overlook.

  ---
  Halting as requested.

---

## File 9: universal_component_mapping_protocol.md (263 lines)

### Structure Breakdown

**Sections:**
- Title & Philosophy (lines 1-15)
- Core Principles (lines 16-30)
- 6-Step Workflow (lines 31-100)
- Base Type Mapping Table (lines 101-140)
- Semantic Override Rules (lines 141-180)
- Secondary Token Logic (lines 181-210)
- Component Descriptor Output (lines 211-250)
- Implementation Examples (lines 251-263)

### Content Assessment

**Purpose:**
Universal Component Mapping Protocol (UCMP) - The component intelligence layer that transforms raw OpenAPI schema metadata into smart, responsive UI component selections.

**Architecture:**

This specification defines a deterministic, rule-based workflow for:
1. Analyzing field metadata from OpenAPI schemas
2. Selecting appropriate UI components based on type, semantics, and constraints
3. Generating component descriptors with dual tokens (primary/secondary)
4. Applying responsive behavior based on device context

**Key Innovation:**
The semantic override system that uses field names to influence component selection (e.g., "email" field gets email_primary component with built-in validation, not generic text_field).

### Detailed Content Breakdown

#### 1. Philosophy & Core Principles (lines 1-30)

**Core Assertion:**
"Component selection is NOT arbitrary guesswork—it is a deterministic process driven by metadata."

**Three Pillars:**
1. **Determinism:** Same input → same output, always
2. **Semantics First:** Field names carry meaning that influences component choice
3. **Dual-Token Architecture:** Every component has primary (desktop) and secondary (mobile) variants

#### 2. Six-Step Workflow (lines 31-100)

**Step 1: Extract Raw Metadata**
```
Input: OpenAPI schema field definition
Extract:
  - name (e.g., "email", "password", "avatar_url")
  - type (string, number, boolean, array, object)
  - format (date-time, email, uri, uuid)
  - constraints (minLength, maxLength, pattern, enum)
  - required (true/false)
  - description
```

**Step 2: Identify Structural Context**
```
Determine if field is:
  - Form field (in request body schema)
  - Display field (in response schema)
  - Filter parameter (in query parameters)
  - Navigation element (in path parameters)
```

**Step 3: Apply Base Type Mapping**
```
Using the Base Type Mapping Table:
  string              → text_field
  string (email)      → email_field
  string (date)       → date_picker
  number/integer      → number_field
  boolean             → toggle_switch
  enum                → select_dropdown
  array (of strings)  → multi_select
```

**Step 4: Apply Semantic Overrides**
```
Check field name against Semantic Override Table:
  If name contains "email"       → email_primary
  If name contains "password"    → password_primary
  If name contains "avatar"      → image_upload_primary
  If name contains "description" → textarea_primary
  If name contains "status"      → badge_primary
```

**Step 5: Apply Secondary Token Logic**
```
Based on device context:
  Mobile/Narrow    → use secondary token (compact variant)
  Tablet/Medium    → use primary or secondary based on density
  Desktop/Wide     → use primary token (full-featured variant)
```

**Step 6: Apply Behavior from Constraints**
```
Translate OpenAPI constraints to component props:
  maxLength      → maxLength prop + character counter
  pattern        → regex validation + error message
  enum           → options array for dropdown
  required: true → required prop + asterisk indicator
  minimum/maximum → min/max props for number field
```

#### 3. Base Type Mapping Table (lines 101-140)

**Complete Mapping Matrix:**

| OpenAPI Type | Format | Component | Primary Token | Secondary Token |
|--------------|--------|-----------|---------------|-----------------|
| string | - | text_field | text_field_primary | text_field_secondary |
| string | email | email_field | email_primary | email_secondary |
| string | password | password_field | password_primary | password_secondary |
| string | date | date_picker | date_picker_primary | date_picker_secondary |
| string | date-time | datetime_picker | datetime_primary | datetime_secondary |
| string | uri/url | url_field | url_primary | url_secondary |
| string (long) | - | textarea | textarea_primary | textarea_secondary |
| number | - | number_field | number_primary | number_secondary |
| integer | - | number_field | number_primary | number_secondary |
| boolean | - | toggle_switch | toggle_primary | toggle_secondary |
| enum | - | select_dropdown | select_primary | select_secondary |
| array | primitives | multi_select | multi_select_primary | multi_select_secondary |
| array | objects | table/cardlist | table_primary | cardlist_secondary |
| object | - | nested_form | form_section_primary | accordion_secondary |

**Heuristic for string → textarea:**
```
If maxLength > 200 OR description contains "description"/"bio"/"notes"
  → Use textarea instead of text_field
```

#### 4. Semantic Override Rules (lines 141-180)

**Override Priority:**
Semantic overrides take precedence over base type mapping.

**Complete Semantic Override Table:**

| Field Name Pattern | Override Component | Tokens |
|--------------------|-------------------|--------|
| email, user_email, contact_email | email_field | email_primary / email_secondary |
| password, pwd, pass | password_field | password_primary / password_secondary |
| avatar, profile_pic, image_url, photo | image_upload | image_upload_primary / image_upload_secondary |
| description, bio, notes, comments | textarea | textarea_primary / textarea_secondary |
| status, state, type, category | badge | badge_primary / badge_secondary |
| tags, labels, categories | tag_input | tag_input_primary / tag_input_secondary |
| color, colour | color_picker | color_primary / color_secondary |
| rating, score | rating | rating_primary / rating_secondary |
| search, query | search_field | search_primary / search_secondary |

**Matching Logic:**
- Case-insensitive
- Partial match (e.g., "user_email" matches "email")
- First match wins (process table top-to-bottom)

#### 5. Secondary Token Logic (lines 181-210)

**Decision Tree for Token Selection:**

```
function selectToken(component, containerWidth, density) {
  if (containerWidth < 480) {
    return component.secondaryToken;
  }

  if (containerWidth >= 768) {
    return component.primaryToken;
  }

  // 480-767px: tablet range
  if (density === "high") {
    return component.secondaryToken; // Compact to fit more
  } else {
    return component.primaryToken; // Standard for readability
  }
}
```

**Token Variant Differences:**

**Primary (Desktop/Standard):**
- Full labels above field
- Larger padding (px-3 py-2)
- Helper text below field
- Character counters visible
- Error messages inline
- Icons and adornments visible

**Secondary (Mobile/Compact):**
- Labels may be floating or placeholder
- Smaller padding (px-2 py-1)
- Helper text hidden or tooltip
- Character counters hidden until near limit
- Error messages toast/bottom sheet
- Icons minimal or hidden

#### 6. Component Descriptor Output (lines 211-250)

**Output Schema:**

```json
{
  "component": "text_field",
  "primaryToken": "text_field_primary",
  "secondaryToken": "text_field_secondary",
  "props": {
    "label": "Email Address",
    "name": "email",
    "type": "email",
    "required": true,
    "maxLength": 120,
    "placeholder": "you@example.com",
    "autocomplete": "email",
    "validation": {
      "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
      "message": "Please enter a valid email address"
    }
  },
  "responsive": {
    "mobile": "secondary",
    "tablet": "primary",
    "desktop": "primary"
  },
  "accessibility": {
    "ariaLabel": "Email Address",
    "ariaRequired": true,
    "ariaDescribedBy": "email-helper-text"
  }
}
```

**Descriptor Fields Explained:**

- **component:** Base component type (used for logic branching)
- **primaryToken:** Desktop/full-featured variant token name
- **secondaryToken:** Mobile/compact variant token name
- **props:** All component properties derived from OpenAPI constraints
- **responsive:** Device-specific token selection rules
- **accessibility:** ARIA attributes for screen readers

#### 7. Implementation Examples (lines 251-263)

**Example 1: Email Field**

```
OpenAPI Schema:
{
  "email": {
    "type": "string",
    "format": "email",
    "maxLength": 120,
    "description": "User's email address"
  }
}

UCMP Processing:
Step 1: Extract → name="email", type="string", format="email", maxLength=120
Step 2: Context → Form field (in request body)
Step 3: Base mapping → string + email format → email_field
Step 4: Semantic override → "email" in name → email_primary (already matched)
Step 5: Token logic → Desktop: primary, Mobile: secondary
Step 6: Constraints → maxLength → maxLength prop + counter

Output: email_field with email_primary/email_secondary tokens
```

**Example 2: Status Field**

```
OpenAPI Schema:
{
  "status": {
    "type": "string",
    "enum": ["active", "pending", "inactive"],
    "description": "Account status"
  }
}

UCMP Processing:
Step 1: Extract → name="status", type="string", enum=[...], required=true
Step 2: Context → Display field (in response schema)
Step 3: Base mapping → enum → select_dropdown
Step 4: Semantic override → "status" in name → badge_primary (OVERRIDE!)
Step 5: Token logic → Desktop: primary, Mobile: secondary
Step 6: Constraints → enum → options for badge variants

Output: badge with badge_primary/badge_secondary tokens
```

### Integration with Other Specifications

**Dependencies:**
- **component_tokens.json:** Provides actual CSS/token values for primary/secondary variants
- **renderer_mapping_spec.md:** Uses UCMP output to generate React/HTMX code
- **openapi_ui_model_conversion_rules.md:** Invokes UCMP during Phase 2 (Interpretation)
- **layout_tokens.json:** Referenced for responsive breakpoint thresholds

**UCMP Position in Pipeline:**
```
OpenAPI Schema → UCMP → Component Descriptors → Renderer → React/HTMX Code
```

**Workflow Integration:**
1. `openapi_ui_model_conversion_rules.md` extracts schema fields (Phase 1)
2. **UCMP processes each field** (Phase 2) ← THIS SPEC
3. `renderer_mapping_spec.md` generates code from descriptors (Phase 3)

### Gaps and Observations

**Missing Component Mappings:**

1. **File Upload:** No mapping for binary/file types
   - `type: string, format: binary` → Should map to `file_upload_primary`

2. **Rich Text Editor:** No mapping for HTML/markdown content
   - Long strings with "html"/"markdown" in description → Should map to `rich_text_editor`

3. **Autocomplete/Typeahead:** No mapping for searchable selects
   - Large enums (>20 options) → Should use `autocomplete_primary` not `select_dropdown`

4. **Slider:** No mapping for ranged numbers with step values
   - `type: number` with `minimum`, `maximum`, `multipleOf` → Could map to `slider_primary`

5. **Date Range:** No mapping for paired date fields
   - Fields like "start_date"/"end_date" → Should detect pairs and map to `date_range_picker`

**Ambiguities:**

1. **Semantic Override Conflicts:** What if field name contains both "email" and "search"? (e.g., "search_by_email")
   - Needs explicit precedence rules or multi-pattern matching

2. **Threshold for Textarea:** "maxLength > 200" is mentioned but not formalized
   - Should be in Step 3 as explicit rule

3. **Badge vs Select for Enums:** Status example shows override to badge, but when should it stay a select?
   - Needs rule: "If in response schema → badge, if in request schema → select"

4. **Array of Objects Detection:** How does UCMP know when to use table vs cardlist for array fields?
   - Missing rule: Check object complexity and field count

5. **Nested Object Depth:** At what nesting level should nested_form become accordion_secondary?
   - Missing rule: Depth threshold or field count threshold

**Enhancement Opportunities:**

1. **Validation Rule Extraction:** Expand Step 6 to include:
   - `minLength` → "Must be at least X characters"
   - `pattern` → Custom regex error messages
   - Cross-field validation (e.g., password confirmation)

2. **Internationalization (i18n):** Add step for label generation
   - Convert "user_email" → "User Email" (display label)
   - Support for multiple languages

3. **Conditional Logic:** Support for dependent fields
   - If "country" = "US" → show "state" field
   - OpenAPI may use `dependencies` or `allOf`/`oneOf`

4. **Custom Component Registry:** Allow projects to register custom components
   - e.g., "credit_card" → custom `credit_card_input` component

5. **Machine Learning Enhancement:** Suggest using ML for ambiguous cases
   - Train on labeled examples to improve semantic override matching
   - Confidence scores for component suggestions

### Production Readiness

**Completeness:** ⭐⭐⭐⭐ (4/5)
- Covers 80% of common UI components
- Missing file upload, rich text, autocomplete, sliders
- Semantic override table needs 10-15 more patterns

**Clarity:** ⭐⭐⭐⭐⭐ (5/5)
- Six-step workflow is exceptionally clear
- Examples demonstrate theory → practice
- Terminology is consistent and well-defined

**Determinism:** ⭐⭐⭐⭐⭐ (5/5)
- Rule-based approach ensures repeatability
- No ambiguous "AI decides" handwaving
- Clear precedence: Semantic overrides > Base type mapping

**Extensibility:** ⭐⭐⭐⭐ (4/5)
- Easy to add new semantic overrides
- Base mapping table is straightforward to extend
- Missing: Plugin/extension mechanism for custom components

**Integration:** ⭐⭐⭐⭐⭐ (5/5)
- Perfectly positioned between OpenAPI conversion and renderer
- Clear inputs (OpenAPI schema) and outputs (Component Descriptor)
- References component_tokens.json and layout_tokens.json appropriately

### Assessment

This is a production-grade MVP specification that:
- Defines the intelligence layer for component selection
- Uses deterministic, rule-based approach (no ML black box)
- Implements semantic understanding through field name analysis
- Supports responsive design through dual-token architecture
- Provides clear, actionable 6-step workflow

**Role in System:**
UCMP is the "brain" of the UI Factory system. It's what makes the system intelligent—transforming dumb API schemas into smart UI component selections that respect semantics, accessibility, and responsive design.

**Critical Innovation:**
The semantic override system (Step 4) is brilliant. Instead of treating all strings as generic text fields, it recognizes that "email" fields need email validation, "password" fields need masking, and "description" fields need multi-line input. This is what separates a naive code generator from an intelligent UI factory.

**Recommendation:**
- **Use as-is for MVP** ✅ (covers 80% of use cases)
- **Priority enhancements:**
  1. Add file upload component mapping
  2. Add autocomplete for large enums (>20 options)
  3. Formalize textarea threshold rule (currently informal)
  4. Add semantic override conflict resolution rules
  5. Expand semantic override table to 20+ patterns
- **Future enhancements:**
  - Rich text editor support
  - Date range picker detection
  - Conditional field logic
  - Custom component registry
  - i18n label generation

**Unique Strength:**
The combination of determinism (rule-based) and intelligence (semantic overrides) makes this system predictable yet smart. It won't surprise developers with random component choices, but it also won't give you a generic text field when you clearly meant an email input.

**Integration Dependencies:**
- Requires `component_tokens.json` to exist with matching token names
- Requires `renderer_mapping_spec.md` to consume Component Descriptor format
- Should be invoked by `openapi_ui_model_conversion_rules.md` during Phase 2

---

## Summary Completion

All 10 markdown documentation files have been comprehensively reviewed. The universal_component_mapping_protocol.md specification represents the intelligence layer of the UI Factory system, providing deterministic yet semantic-aware component selection from OpenAPI schemas.

**Archive Status:** Complete
**Files Reviewed:** 10/10
**Assessment Date:** 2025-12-01
**Final Review Added:** universal_component_mapping_protocol.md