# State Capacity AI

## Overview
A static website for the State Capacity AI project — focused on AI governance, decision transparency, and public accountability. The site publishes field guides, tools, and strategies that make the AI decision layer visible and contestable.

## Project Architecture
- **Type**: Static HTML/CSS/JS website (no build system)
- **Design**: Dark-first editorial aesthetic inspired by Forensic Architecture. High contrast, sans-serif typography (Inter), minimal ornamentation.
- **Structure**:
  - `index.html` — Landing page with hero, 2-column guide grid, search filter
  - `about/` — About page
  - `guide/`, `guides/`, `experiments/`, `framework/` — Content pages
  - `css/sovereign.css` — Main stylesheet (design tokens, dark/light themes, card grid, sidebar, responsive)
  - `js/nav.js` — Navigation, theme toggle (dark default), sidebar/mobile menu coordination, search/filter
  - `img/` — SVG logo, PNG social card
  - `repo-content/` — Source markdown/HTML content for various sub-projects

## Design System
- **Colors**: Dark-first (`#0a0a0a` bg, `#ffffff` headings, `#d4d4d4` body, `#737373` muted). Light mode via `[data-theme="light"]`.
- **Typography**: Inter (300-700 weights). Bold headings with tight letter-spacing. Uppercase section labels.
- **Cards**: 2-column editorial grid with 1px gap borders. Hover reveals elevated background.
- **Navigation**: Uppercase site title, minimal header nav, hamburger on mobile with organized dropdown.
- **Theme toggle**: Dark is default. Light mode available via toggle button. Preference stored in localStorage.

## Recent Changes
- Redesigned entire site with dark-first editorial aesthetic (Forensic Architecture-inspired)
- Replaced light color scheme with high-contrast dark theme as default
- Updated typography to Inter sans-serif with bold headings and tight letter-spacing
- Redesigned landing page with dramatic hero and 2-column editorial card grid
- Removed PureCSS dependency
- Updated footer from badge-only to minimal footer bar
- All 22+ pages updated with consistent dark theme

## User Preferences
- User mentioned adding custom font later
- Editorial/investigative aesthetic preferred

## Running Locally
The site is served using `npx serve` on port 5000.

## Deployment
Configured as a static site deployment with the root directory (`.`) as the public directory.
