/**
 * Tailwind Generator Template
 *
 * This file shows how the UI Factory should generate a Tailwind config
 * from layout.tokens.json, so that React and HTMX/Jinja2 share the same
 * spacing, breakpoints, elevation, radius, typography, and motion tokens.
 */

const fs = require('fs');
const path = require('path');

// Load tokens (generated or maintained separately)
const tokensPath = path.resolve(__dirname, 'layout.tokens.json');
const layoutTokens = JSON.parse(fs.readFileSync(tokensPath, 'utf8'));

// Helper: convert a numeric array into Tailwind spacing map
function spacingFromScale(scaleArray) {
  const spacing = {};
  scaleArray.forEach((value, index) => {
    spacing[index] = `${value}px`;
  });
  return spacing;
}

// Helper: passthrough for breakpoints (Tailwind expects strings with px)
function screensFromBreakpoints(breakpoints) {
  const screens = {};
  Object.entries(breakpoints).forEach(([key, value]) => {
    screens[key] = `${value}px`;
  });
  return screens;
}

// Helper: elevation to boxShadow map
function boxShadowFromElevation(elevationTokens) {
  const boxShadow = {};
  Object.entries(elevationTokens).forEach(([key, value]) => {
    boxShadow[key] = value.shadow;
  });
  return boxShadow;
}

// Helper: radius tokens (assume raw pixel numbers)
function borderRadiusFromTokens(radiusTokens) {
  const radius = {};
  Object.entries(radiusTokens).forEach(([key, value]) => {
    radius[key] = `${value}px`;
  });
  return radius;
}

// Helper: typography scale → fontSize map
function fontSizeFromTypographyScale(scale) {
  const fontSize = {};
  Object.entries(scale).forEach(([key, value]) => {
    fontSize[key] = [`${value.fontSize / 16}rem`, `${value.lineHeight / 16}rem`];
  });
  return fontSize;
}

/**
 * Generated Tailwind Config
 * This can be written out to tailwind.config.js by the factory, or
 * imported directly into a monorepo configuration.
 */

/** @type {import('tailwindcss').Config} */
const config = {
  content: [
    './src/**/*.{js,ts,jsx,tsx}',
    './templates/**/*.html', // Jinja2 + HTMX templates
  ],
  theme: {
    container: {
      center: true,
      padding: {
        DEFAULT: `${layoutTokens.layout.container.paddingX}px`,
        sm: `${layoutTokens.layout.container.paddingX}px`,
        md: `${layoutTokens.layout.container.paddingX}px`,
      },
    },
    extend: {
      screens: screensFromBreakpoints(layoutTokens.breakpoints),
      spacing: spacingFromScale(layoutTokens.spacing.scale),
      boxShadow: boxShadowFromElevation(layoutTokens.elevation),
      borderRadius: borderRadiusFromTokens(layoutTokens.radius),
      fontSize: fontSizeFromTypographyScale(layoutTokens.typography.scale),
      // Colour roles are mapped in brand-specific configs; here we only
      // declare the structure, not the concrete hex values.
      colors: {
        primary: {
          DEFAULT: 'var(--color-primary)',
          hover: 'var(--color-primary-hover)',
          soft: 'var(--color-primary-soft)',
        },
        secondary: {
          DEFAULT: 'var(--color-secondary)',
          hover: 'var(--color-secondary-hover)',
        },
        neutral: {
          50: 'var(--color-neutral-50)',
          100: 'var(--color-neutral-100)',
          200: 'var(--color-neutral-200)',
          300: 'var(--color-neutral-300)',
          400: 'var(--color-neutral-400)',
          500: 'var(--color-neutral-500)',
          600: 'var(--color-neutral-600)',
          700: 'var(--color-neutral-700)',
          800: 'var(--color-neutral-800)',
          900: 'var(--color-neutral-900)',
        },
        success: 'var(--color-success)',
        warning: 'var(--color-warning)',
        info: 'var(--color-info)',
        error: 'var(--color-error)',
      },
      transitionTimingFunction: {
        standard: layoutTokens.motion.easing.standard,
        inOut: layoutTokens.motion.easing.inOut,
        snappy: layoutTokens.motion.easing.snappy,
      },
      transitionDuration: {
        fast: `${layoutTokens.motion.durations.fast}ms`,
        normal: `${layoutTokens.motion.durations.normal}ms`,
        slow: `${layoutTokens.motion.durations.slow}ms`,
      },
    },
  },
  plugins: [
    require('@tailwindcss/container-queries'),
  ],
};

module.exports = config;

/**
 * Factory Usage
 * 1. Read layout.tokens.json
 * 2. Build this config object
 * 3. Write to tailwind.config.js in the generated project
 * 4. Use same tokens across React + HTMX + Jinja2
 */
