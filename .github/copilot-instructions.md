# Copilot Instructions — ramdesh.github.io

## Project Overview

Personal portfolio and creative writing site for Ramindu Deshapriya, hosted on **GitHub Pages** at `https://ramdesh.github.io`. The site showcases open-source projects, tech stats, skills, and Sinhala science fiction short stories.

## Hosting & Deployment

- **Platform**: GitHub Pages (static hosting, no build step)
- **Repository**: `ramdesh/ramdesh.github.io` (deploys from `main` branch root)
- **Constraints**: No server-side code, no build tools (no Jekyll, Hugo, Webpack, etc.). All pages are pure static HTML/CSS/JS served directly.

## Architecture

```
ramdesh.github.io/
├── index.html                    # Main portfolio page (single-file, embedded CSS/JS)
├── sinhala-stories/
│   ├── index.html                # Story listing page
│   ├── hirano-35.html            # හිරානෝ-35 story
│   └── minimuthu.html            # මිණිමුතු story
├── hirano_35.txt                 # Raw story text (source, not served directly)
├── minimuthu.txt                 # Raw story text (source, not served directly)
└── LICENSE                       # MIT
```

- **No external CSS/JS frameworks** — all styling is embedded in `<style>` tags within each HTML file
- **No shared CSS file** — styles are duplicated per page (keep them in sync manually)
- Story pages under `sinhala-stories/` use a slightly different CSS set (includes `Noto Sans Sinhala` font, narrower `max-width: 900px` container, story-specific classes)

## Design System

### Color Palette (Blue-themed dark mode)

| Token              | Hex                           | Usage                              |
|--------------------|-------------------------------|------------------------------------|
| Background         | `#1C1B1F`                     | Page background                    |
| Surface            | `#2B2930`                     | Cards, header, footer              |
| Surface hover      | `#322F37`                     | Card hover state                   |
| Border             | `#49454F`                     | Card borders, dividers             |
| Primary accent     | `#82B1FF`                     | Headings, links, buttons, stats    |
| Primary hover      | `#B3D4FC`                     | Button/link hover state            |
| Button text (dark) | `#0D2B6B`                     | Text on primary-colored buttons    |
| Body text          | `#E6E1E5`                     | Main body text                     |
| Secondary text     | `#CAC4D0`                     | Descriptions, subtitles, footer    |
| Subtle accent bg   | `rgba(130, 177, 255, 0.08)`   | Pill buttons, skill tags (rest)    |
| Subtle accent hover| `rgba(130, 177, 255, 0.16)`   | Pill buttons, skill tags (hover)   |
| Badge blue         | `#8AB4F8` / `rgba(138,180,248,0.12)` | Language badges            |
| Badge gold         | `#FDD663` / `rgba(253,214,99,0.12)`  | Star count badges          |
| Badge green        | `#81C995` / `rgba(129,201,149,0.12)` | Contributor badges         |

### Typography

- **Primary font**: `Roboto` (Google Fonts) — weights 300, 400, 500, 700
- **Sinhala font**: `Noto Sans Sinhala` (Google Fonts) — used on story pages for proper rendering; weights 300, 400, 500, 700
- **Line height**: 1.6 (body), 2.0 (story content)

### Component Patterns

- **Cards**: `border-radius: 16px`, `1px solid #49454F` border, subtle box-shadow, `-2px translateY` on hover
- **Pill buttons**: `border-radius: 20px`, `padding: 10px 24px`
- **Badges**: `border-radius: 8px`, `padding: 6px 16px`
- **Transitions**: `all 0.2s ease` for hover effects
- **Responsive**: Single breakpoint at `768px` (grid collapses to single column)

## Sinhala Stories Section

- Stories are written in **Sinhala Unicode** — always use `<html lang="si">` and `<meta charset="UTF-8">`
- Each line in the `.txt` source files is a separate paragraph (`<p>` tag) — do NOT join lines
- `---` lines in source text become `<hr class="story-divider">`
- Navigation: portfolio `index.html` → `sinhala-stories/index.html` → individual story pages
- All internal links use **relative paths** (e.g., `../` for parent, `./` for same directory)
- Story pages use `font-family: 'Noto Sans Sinhala', 'Roboto', sans-serif` for Sinhala text elements

## Adding a New Story

1. Add the raw `.txt` file to the repo root (Sinhala Unicode, one paragraph per line)
2. Create a new HTML page in `sinhala-stories/` following the existing story page template
3. Convert text: each non-empty line → `<p>`, `---` → `<hr class="story-divider">`, HTML-escape content
4. Add a link to `sinhala-stories/index.html` story list
5. Keep all styles in sync with existing story pages

## Guidelines

- **Keep it static**: No build steps, no npm, no bundlers. Must work with GitHub Pages vanilla static hosting.
- **Keep colors consistent**: When changing the color scheme, update ALL HTML files (index + all story pages). Use find-and-replace across files.
- **No external CSS files**: Styles are embedded. If adding new pages, copy the full `<style>` block from an existing similar page.
- **Escape HTML in stories**: Story text must be HTML-escaped (e.g., `&amp;`, `&lt;`) since it's inserted into `<p>` tags.
- **Test locally**: Open HTML files directly in a browser — no server needed.
- **Copyright**: All content © Ramindu Deshapriya. Stories are original creative works. MIT license applies to code only.
