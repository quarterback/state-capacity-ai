# State Capacity AI

## Overview
A static website for the State Capacity AI project — focused on AI governance, decision transparency, and public accountability. The site publishes field guides, tools, and strategies that make the AI decision layer visible and contestable.

## Project Architecture
- **Type**: Static HTML/CSS/JS website
- **Structure**:
  - `index.html` — Landing page with guide cards and search filter
  - `about/` — About page
  - `guide/`, `guides/`, `experiments/`, `framework/` — Content pages
  - `css/sovereign.css` — Main stylesheet (design tokens, card styles, accessibility)
  - `js/nav.js` — Navigation, theme toggle, and search/filter script
  - `img/` — SVG logo, PNG social card
  - `repo-content/` — Source markdown/HTML content for various sub-projects

## Recent Changes
- Restyled guide list into visual card layout with SVG icons, borders, shadows, and hover effects
- Added search/filter input for guides on landing page (filters by title, description, and tags)
- Improved accessibility: skip-to-content links, focus-visible states, ARIA roles/labels, sr-only class
- Updated OG metadata across all pages: PNG card image, og:url, og:site_name, apple-touch-icon, theme-color

## Running Locally
The site is served using `npx serve` on port 5000.

## Deployment
Configured as a static site deployment with the root directory (`.`) as the public directory.
