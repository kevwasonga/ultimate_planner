# Frontend Design & Color Palette

This document describes the exact usage of colors and styling patterns for the **BuildConnect** frontend. The project uses a sophisticated, professional color palette designed for an enterprise-grade construction professional marketplace.

## 🎨 Color Palette (CSS Variables)

Defined in `templates/base.html` under `:root`.

| Variable | Hex Code | Description | Usage |
| :--- | :--- | :--- | :--- |
| `--gold` | `#C8860A` | **Primary Brand Color** | Logos, active links, primary buttons, highlights. |
| `--gold-light` | `#E8A020` | Secondary Gold | Button hover states. |
| `--dark` | `#0F1410` | **Deep Forest Black** | Navigation backgrounds, footers, primary text contrast. |
| `--dark-2` | `#1A2020` | Dark Grey/Green | Secondary background sections. |
| `--dark-3` | `#242E28` | Muted Dark | Card backgrounds or deep borders. |
| `--green` | `#2E6B3E` | **Success/Natural Green** | Secondary actions, successful status indicators. |
| `--green-light`| `#3A8A50` | Lighter Green | Green button hover states. |
| `--cream` | `#F5F0E8` | **Base Background** | Primary body background, soft and professional. |
| `--cream-2` | `#EDE5D5` | Muted Cream | Secondary background areas, input fields. |
| `--text` | `#2A2A2A` | **Primary Text** | Standard body text and headings. |
| `--text-muted` | `#6B7280` | Muted Text | Descriptions, dates, and secondary info. |
| `--white` | `#FFFFFF` | Absolute White | Card content, navigation link contrast. |

## 🏗 Typography

- **Headings:** `Playfair Display` (Serif) - Used for logos and prominent headings to convey authority and craftsmanship.
- **Body:** `DM Sans` (Sans-Serif) - Used for UI elements, descriptions, and standard text for maximum readability.

## ✨ UI Components

### Buttons
- **Gold Button (`.btn-gold`):** The main Call-to-Action. Uses `--gold` background and `--dark` text.
- **Green Button (`.btn-green`):** Used for secondary or success actions. Uses `--green` background and `--white` text.
- **Outline Button (`.btn-outline`):** Used for transparent actions, typically on dark backgrounds.

### Navigation
- Background: `--dark`
- Border Bottom: `1px solid rgba(200,134,10,0.3)` (30% opacity `--gold`).
- Active Link: `--gold`.

### Messages / Alerts
- **Success:** Background `#D1FAE5`, Text `#065F46`, Left Border `--green`.
- **Error:** Background `#FEE2E2`, Text `#991B1B`, Left Border `#EF4444`.

## 📐 Shadows & Depth
- `--shadow`: `0 4px 24px rgba(0,0,0,0.08)` (Subtle elevation).
- `--shadow-lg`: `0 16px 48px rgba(0,0,0,0.14)` (Prominent elevation for modals or featured cards).
