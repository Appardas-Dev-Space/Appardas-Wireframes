# appardas website hub

A centralized website hub for **appardas** with **two faces**:

1. **Public Face** — landing page, subpages, and public staff digital IDs.
2. **Internal Face** — the essential tooling needed to operate the hub.

*Branding Note: The name is always styled in lowercase (**`appardas`**), matching the official ribbon loop logo and warm amber/bronze + stone aesthetic.*

The **Ticketing System is already built** (`../Appardas-Ticketing-Module`) and is treated as a finished, integrated module reached from the Hub.

---

## Deliverables in this directory

| Path | What it is |
|---|---|
| [`00-RESEARCH-AND-PLAN.md`](00-RESEARCH-AND-PLAN.md) | Research-backed master plan / specification (IA, page specs, privacy model, design system, architecture, roadmap). |
| [`wireframes/index.html`](wireframes/index.html) | **Wireframe gallery** — visual index linking every page. **Start here.** |
| `wireframes/public/` | Public-face wireframes (landing, services, work, team, staff profile, about, contact, privacy). |
| `wireframes/internal/` | Internal-face wireframes (login, dashboard, directory, digital ID manager, content, inquiries, settings). |

## Running the Flask Backend

Run locally using Python:

```bash
pip install -r requirements.txt
python app.py
```
Open **`http://127.0.0.1:5000`** in your browser. The root page directly renders the **Wireframe Gallery** with full iframe previews and instant navigation across both faces. Zero client-side JavaScript required.

## Vercel Deployment

Deploy directly to Vercel via Git:
- **Runtime**: Python Serverless (`api/index.py` + `requirements.txt`).
- **Routing**: `vercel.json` routes all requests to `api/index.py` while serving `/static/*` assets cleanly.


## At a glance

### Public Face
| Wireframe | Route |
|---|---|
| Landing / Home | `/` |
| Services | `/services` |
| Work | `/work` |
| Team Directory | `/team` |
| Staff Digital ID ★ | `/team/[slug]` |
| About | `/about` |
| Contact | `/contact` |
| Privacy Notice | `/privacy` |

### Internal Face
| Wireframe | Route |
|---|---|
| Login | `/internal/login` |
| Hub Dashboard | `/internal` |
| Staff Directory | `/internal/directory` |
| Digital ID Manager ★ | `/internal/ids` |
| Content Manager | `/internal/content` |
| Inquiry Inbox | `/internal/inquiries` |
| Settings | `/internal/settings` |
| Ticketing (existing) | `/ticketing` (module) |

## Key decisions

- **Reuse the proven stack** — Next.js 14 (App Router) + Strapi v5 + PostgreSQL, matching the existing Ticketing Module.
- **Flat-modern 2.0 design** — flat color blocks and bold type, with subtle depth on interactive elements to preserve usability.
- **Privacy-safe staff IDs** — public profiles render only consented, work-related fields; private and sensitive fields are never sent to the browser (enforced server-side).
- **Essential-only internal face** — every internal screen must feed the public face or protect operational integrity.

## Status

Draft v1 — ready for review. See §13 of the plan for assumptions and open questions to confirm.
