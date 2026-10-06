# 02 — Design System

Impression to create: **a real software product built by experienced engineers.** Restraint over effects.

---

## 1. Colour combination

### Brand

| Role | Name | Hex | Use |
|---|---|---|---|
| Primary | Deep Navy | `#0F2747` | Header, primary buttons, headings emphasis, hero background |
| Secondary | Professional Blue | `#1E5AA8` | Links, secondary actions, selected states, chart primary |
| Accent | Muted Teal | `#187C7A` | Small accents only: verified marks, highlights, one chart series |

### Neutrals

| Role | Hex |
|---|---|
| Page background | `#F7F8FA` |
| Surface / card | `#FFFFFF` |
| Primary text | `#172033` |
| Secondary text | `#5F6B7A` |
| Border | `#DCE2E8` |
| Border strong (inputs, hover) | `#C4CCD6` |
| Subtle fill (table header, hover row) | `#F0F3F6` |
| Disabled text (never for essential info) | `#8A94A3` |

### Tints and hover shades

| Token | Hex | Use |
|---|---|---|
| navy-hover | `#0B1E38` | Primary button hover |
| blue-hover | `#184A8B` | Secondary button / link hover |
| blue-50 | `#EAF1FA` | Selected row, info background |
| teal-50 | `#E6F2F2` | Verified background |

### Semantic (muted, never neon)

| State | Text/Icon | Background tint | Use only for |
|---|---|---|---|
| Success | `#2F7D4F` | `#E8F3EC` | Matched, verified, high alignment |
| Warning | `#9A6A12` | `#FBF3E0` | Partial match, concern, moderate gap |
| Error | `#B3433F` | `#FAEAE9` | Missing skill, critical gap, form errors |

### Colour rules

1. Large surfaces are neutral: page `#F7F8FA`, panels white.
2. Navy/blue for primary actions. Teal is an accent, never the dominant colour.
3. Semantic colours only where the meaning applies.
4. No purple as a brand colour. No neon. No rainbow charts. No glowing borders.
5. No gradients. Use flat colour.
6. Colour is never the only signal. Pair with an icon and a text label.

### Chart palette (in order)

`#0F2747` navy · `#1E5AA8` blue · `#187C7A` teal · `#7A8797` slate · `#9A6A12` amber (gaps only)

---

## 2. CSS variables

```css
:root {
  --sb-navy: #0F2747;
  --sb-navy-hover: #0B1E38;
  --sb-blue: #1E5AA8;
  --sb-blue-hover: #184A8B;
  --sb-blue-50: #EAF1FA;
  --sb-teal: #187C7A;
  --sb-teal-50: #E6F2F2;

  --sb-bg: #F7F8FA;
  --sb-surface: #FFFFFF;
  --sb-fill: #F0F3F6;
  --sb-text: #172033;
  --sb-text-2: #5F6B7A;
  --sb-text-disabled: #8A94A3;
  --sb-border: #DCE2E8;
  --sb-border-strong: #C4CCD6;

  --sb-success: #2F7D4F;  --sb-success-bg: #E8F3EC;
  --sb-warning: #9A6A12;  --sb-warning-bg: #FBF3E0;
  --sb-error:   #B3433F;  --sb-error-bg:   #FAEAE9;

  --sb-radius-sm: 6px;    /* buttons, inputs, badges */
  --sb-radius-md: 8px;    /* cards, panels */
  --sb-radius-lg: 12px;   /* modals, menus (max) */

  --sb-shadow-sm: 0 1px 2px rgba(15, 39, 71, 0.06);
  --sb-shadow-md: 0 4px 12px rgba(15, 39, 71, 0.08); /* menus, modals only */

  --sb-focus: 0 0 0 3px rgba(30, 90, 168, 0.35);
}
```

## 3. Tailwind CDN config (current React file)

```html
<script src="https://cdn.tailwindcss.com"></script>
<script>
  tailwind.config = {
    theme: {
      extend: {
        colors: {
          navy:  { DEFAULT: '#0F2747', hover: '#0B1E38' },
          brand: { DEFAULT: '#1E5AA8', hover: '#184A8B', 50: '#EAF1FA' },
          teal:  { DEFAULT: '#187C7A', 50: '#E6F2F2' },
          canvas: '#F7F8FA',
          ink:   { DEFAULT: '#172033', muted: '#5F6B7A' },
          line:  { DEFAULT: '#DCE2E8', strong: '#C4CCD6' },
          ok:    { DEFAULT: '#2F7D4F', bg: '#E8F3EC' },
          warn:  { DEFAULT: '#9A6A12', bg: '#FBF3E0' },
          bad:   { DEFAULT: '#B3433F', bg: '#FAEAE9' },
        },
        fontFamily: {
          sans: ['"IBM Plex Sans"', 'Inter', 'system-ui', '-apple-system', 'Segoe UI', 'Roboto', 'sans-serif'],
        },
        borderRadius: { sm: '6px', md: '8px', lg: '12px' },
      },
    },
  }
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
```

---

## 4. Typography

Font: **IBM Plex Sans** (fallback Inter, then system sans). One family only. Weights 400 / 500 / 600. No 700+ bold blocks.

| Level | Size / line | Weight | Notes |
|---|---|---|---|
| Hero title | 32–36 / 40 | 600 | Home only. Not giant |
| Page title | 28 / 36 | 600 | |
| Section heading | 20 / 28 | 600 | |
| Card / panel heading | 16 / 24 | 600 | Compact |
| Body | 14 / 22 | 400 | Default |
| Metadata | 12 / 16 | 400–500 | Colour `#5F6B7A` |
| Table header | 12 / 16 | 500 | Sentence case, not uppercase |

Avoid: giant hero text, ALL-CAPS labels (only tiny table column headers if needed), decorative fonts, heavy bold. Hierarchy comes from size, weight and spacing before colour.

---

## 5. Spacing and layout

- Base unit 4px. Scale: 4, 8, 12, 16, 24, 32, 48.
- Card/panel padding: 16–24px, consistent per screen.
- Page max width: 1280px, centred, 24px side padding (16px on mobile).
- Gap between page sections: 32px. Between related items: 12–16px.
- Hierarchy comes from spacing, typography, borders, alignment and grouping — not effects.

## 6. Shape, borders, shadow

- Radius: 6px buttons/inputs/badges, 8px cards/panels, 12px modals/menus. Never larger.
- Border: 1px `#DCE2E8` on cards and panels.
- Shadow: `--sb-shadow-sm` at most on cards. `--sb-shadow-md` only on floating layers (menu, modal).
- No glassmorphism, no blobs, no glow.

---

## 7. Components

**Buttons**
- Primary: navy fill, white text, 36–40px height, radius 6px. Hover `navy-hover`. Active slightly darker. Focus ring `--sb-focus`. Disabled: `#DCE2E8` fill, `#8A94A3` text, `cursor: not-allowed`.
- Secondary: white fill, 1px `#C4CCD6` border, navy text. Hover `#F0F3F6`.
- Tertiary / link: blue text, underline on hover.
- Destructive: only for real destructive actions, muted red.

**Inputs**
- Visible `<label>` above every field. 40px height. 1px `#C4CCD6` border, radius 6px. Focus: blue border + focus ring. Error: red border + message below with an icon.

**Cards vs other structures** — do not make everything a card. Use the right structure:
- Tables for comparisons (skills demand, benchmark, candidates)
- Lists for requirements and plans
- Metric rows (inline figures separated by dividers) instead of big stat tiles
- Tabs for switching views
- Plain sections with a heading and a 1px divider
- Compact cards only for discrete objects (an opportunity, a candidate)

**Badges / status**
- Small, 12px text, radius 6px, tint background. Always icon + label: `✓ Matched`, `⚠ Partial`, `✕ Missing`, `✓ Verified`.
- Do not use pills for decoration.

**Tables**
- Header row `#F0F3F6`, 1px row dividers, 44px rows, hover `#F7F8FA`. Wrap in `overflow-x: auto`. On mobile either scroll inside the wrapper or stack rows.

**Tabs** — underline style, 2px blue underline on active, text navy.

**Modal** — white, radius 12px, `--sb-shadow-md`, dim overlay `rgba(15,39,71,0.45)`, focus trapped, Esc closes, close button labelled.

**Hamburger menu** — dropdown anchored under the icon, white, 1px border, radius 8px, 3 items only, closes on outside click and Esc.

**Avatar** — circular photo (or initials fallback in navy-on-blue-50). **Not clickable.**

**Skill level bar** — thin 6px bar, navy fill on `#E3E8EE` track, with numeric or text level beside it.

**Blurred private region** — see `03_PAGES_AND_FLOWS.md`. Heading never blurred. Content `filter: blur(5px)`, `user-select: none`, `aria-hidden`. Whole region is a button that opens the login prompt.

---

## 8. Motion

- Duration 120–180ms, `ease-out`. Properties: colour, background, border, opacity, transform ≤ 2px.
- Allowed: hover colour changes, dropdown fade, modal fade, tab underline, bar fill on first render.
- Not allowed: floating or pulsing elements, parallax, bouncing, glow, long entrance animations.
- Respect `prefers-reduced-motion: reduce` (disable non-essential transitions).

## 9. Responsive

| Breakpoint | Behaviour |
|---|---|
| ≥1280 desktop | Full layout, three stakeholder blocks in a row |
| 1024–1279 laptop | Same, reduced gutters |
| 768–1023 tablet | Two-column grids collapse to one where needed; side panels become full-width sections below |
| <768 mobile | Single column; header keeps logo + avatar + hamburger; tables scroll inside wrappers; skill graph fits viewport width and stays touch-interactive |

Never allow: text overflow, horizontal page scroll, overlapping buttons, graphs wider than the viewport.

## 10. Accessibility

- Semantic `<button>`, `<nav>`, `<main>`, `<table>`, `<label>`.
- Visible focus ring on every interactive element.
- Text contrast ≥ 4.5:1 (use `#5F6B7A` or darker for secondary text, never `#8A94A3` for essential text).
- Logical tab order; modals trap focus; menus close on Esc.
- Status = icon + label + colour.
- Form errors announced with `aria-live="polite"` and tied to inputs with `aria-describedby`.

---

## 11. Avoid the "AI-generated" look

Do not use: excessive gradients, purple/blue neon, glowing elements, glassmorphism, giant rounded cards, heavy shadows, decorative blobs, lots of emoji, "AI" labels everywhere, many pills, huge type, unnecessary animation, a card for every item, repeated stat tiles, saturated dashboards, sci-fi styling, generic SaaS landing-page layout.

Do use: tables, dividers, restrained colour, consistent alignment, realistic density (not empty, not crowded), subtle states, clear hierarchy.
