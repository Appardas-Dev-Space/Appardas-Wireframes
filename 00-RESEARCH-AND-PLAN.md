# Appardas Website Hub — Research & Master Plan

> **Document type:** Research + Specification + Implementation Plan
> **Status:** Draft v1 — ready for review
> **Scope:** A centralized website hub with two faces — a **Public Face** (landing page, subpages, staff digital IDs) and an **Internal Face** (essential tools only). The Ticketing System is already built and treated as a finished, integrated module.
> **Companion artifacts:** Static wireframes in `wireframes/public/` and `wireframes/internal/` (HTML + Tailwind, no JavaScript).

---

## 1. Executive Summary

The **Appardas Website Hub** is a single product with **two faces** sharing one backend and one design language:

| Face | Audience | Purpose | Auth |
|---|---|---|---|
| **Public Face** | Prospects, clients, partners, the general public | Explain who Appardas is, what it offers, prove credibility, and provide contact + staff identity pages | None (open) |
| **Internal Face** | Staff, managers, admins | The minimum operational tooling needed to *run* the hub: content control, staff/public-profile management, inquiries, and module launch | Required (RBAC) |

**Key architectural decision:** Do **not** rebuild the ticketing system. The hub reuses the **existing Next.js 14 + Strapi v5 + PostgreSQL** stack (already proven by `Appardas-Ticketing-Module`). The ticketing module becomes **one module inside the Internal Face**, reached through a Hub Launcher. The hub adds only what is essential.

**Guiding principle:** *Public face = persuasive but respectful. Internal face = essential, not exhaustive.* Every internal screen must justify its existence by enabling the public face or preserving operational integrity.

---

## 2. Objectives & Success Criteria

### 2.1 Business Objectives
1. Give Appardas a credible, modern public presence that converts visitors into inquiries/clients.
2. Centralize the brand, content, and staff identity in one maintainable place.
3. Expose staff professional identity publicly in a controlled, privacy-respecting way that builds trust.
4. Provide staff a single internal starting point (hub) that links to all operational modules.

### 2.2 Success Criteria (measurable)
| Goal | Metric |
|---|---|
| Lead generation | Contact/inquiry submissions per month |
| Engagement | Bounce rate < 55%; avg. session > 60s on landing |
| Trust | Team page → staff profile click-through; profile view depth |
| Performance | LCP < 2.5s; page weight < 1.5MB; 100% HTTPS |
| Accessibility | WCAG 2.1 AA on all public pages |
| Operability | Hub admin can publish a content/profile change without developer help |
| Privacy | 0 unnecessary PII fields published; consent recorded for every public profile |

### 2.3 Non-Goals (explicitly out of scope)
- Rebuilding or modifying the ticketing system.
- Public user accounts / client portal (future backlog).
- E-commerce, billing, or payments.
- Blog/CMS marketing engine beyond core pages (future backlog).
- Multi-tenant / multi-brand tenancy.

---

## 3. Research Findings

> Findings are grouped by theme. Sources are listed in §3.4. Items marked **[best practice synthesis]** are drawn from established design convention rather than a single cited study.

### 3.1 Modern Flat Design ("Flat-Modern")
- Flat design uses **simple two-dimensional elements, bright contrasting colors, no gradients/textures/heavy shadows**, and prioritizes **minimalism, functionality, and usability** (IxDF).
- Strengths: **faster load times, easier responsive scaling, lower cognitive load, consistent brand application, contemporary aesthetic.**
- **Critical risk:** *pure* flat design removes affordance cues — buttons stop looking clickable. The industry answer is **"Flat Design 2.0" / "almost flat"**: keep clean 2D visuals but add **subtle depth** (soft shadows, layering, color variation, borders) to signal interactivity (IxDF).
- Practical recipe from the research: **limited bright palette, simple recognizable iconography, legible sans-serif type, strong visual hierarchy via size/color/placement, consistent grid, generous negative space.** **[best practice synthesis]**

**Decision for Appardas:** Adopt **flat-modern 2.0** — flat color blocks and bold type, but interactive elements get subtle `shadow-sm`/borders and clear hover states so they remain obviously clickable.

### 3.2 Website & Landing-Page Best Practices
- **Above-the-fold value proposition** is the single most important landing element; state what you do and for whom immediately (Kinsta/Orbit Media standards).
- Conventional, low-friction layout: **logo top-left, horizontal top navigation (≤ 7 items)** (Kinsta). Avoid mega/dropdown menus where possible — users dislike them and they hurt crawlability.
- Layout principles: **balance, composition, spacing/negative space, one clear focal point per page, deliberate hierarchy** (Kinsta).
- Color & contrast: **WCAG 2.1 AA, contrast ratio ≥ 4.5:1 for normal text**; don't rely on color alone (Kinsta).
- Type: **limit to ~2–3 typefaces**; sans-serif for headings; avoid decorative body text (Kinsta).
- Performance: **~50% of users expect < 2s load**; optimize/limit images, use CDN, defer non-critical assets (Kinsta).
- **Mobile-first:** >60% of traffic is mobile; Google prioritizes mobile-friendly sites (Kinsta).
- Accessibility: **ALT text, keyboard-operable nav, transcripts for media, skip links** (Kinsta).
- Security: **HTTPS everywhere, secure auth, limit login attempts** (Kinsta).
- **≤ 3-click rule** to reach any key information (Kinsta). **[applied to IA]**

**Decision for Appardas:** Landing page follows the canonical funnel: **Hero (value prop + primary CTA) → Proof (logos/stats) → Services → Process → Featured work → Team teaser → Final CTA → Footer.** Nav is a flat, ≤6-item top bar with a single **"Get in Touch"** button.

### 3.3 Privacy for Public Staff Profiles
Publicly exposing staff information is a **data-protection matter**, not just a design choice. The UK/EU GDPR principles (ICO) apply directly:
- **Lawfulness, fairness & transparency** — staff must know and agree to what is published; publish a privacy notice.
- **Purpose limitation** — collect staff data only for a stated purpose (e.g., "identify points of contact / build trust").
- **Data minimisation** — publish **only what is necessary**: name, role, department, a short professional bio, work contact, optional professional links.
- **Accuracy** — profiles must be kept current and correctable by the individual.
- **Storage limitation** — delete/retire profiles for departed staff promptly.
- **Integrity & confidentiality** — protect the private source data; publish only the approved public subset.
- **Accountability** — keep a record of consent and who approved publication.

**Decision for Appardas — "Public-Safe by Default" profile model:**
1. Every public profile is **opt-in** and requires recorded **consent**.
2. Split profile data into three tiers:
   - **Public (publishable):** display name, role/title, department, short bio, work email/phone (optional), professional links, avatar.
   - **Internal-only:** personal contact, employment dates, internal IDs, manager, emergency info, salary/HR data.
   - **Sensitive/never publish:** private phone, home address, government IDs, personal social accounts, salary, HR notes.
3. A staff member can **request edits or removal** at any time (self-service in the Internal Face).
4. Public pages show a **plain-language privacy note** and a link to the full policy.

### 3.4 Sources
| # | Source | Used for |
|---|---|---|
| 1 | Tailwind CSS — *Installation / Play CDN* (tailwindcss.com/docs/installation/play-cdn) | No-build Tailwind via `@tailwindcss/browser@4` CDN for wireframes |
| 2 | Interaction Design Foundation (IxDF) — *What is Flat Design?* (interaction-design.org) | Flat design definition, benefits, Flat 2.0 affordance fix |
| 3 | Kinsta — *Web Design Best Practices* (kinsta.com/blog) | IA, nav, contrast, typography, performance, mobile, a11y, security |
| 4 | ICO — *Guide to the Data Protection Principles* (ico.org.uk) | Data minimisation, purpose limitation, consent, accountability |

> **Note:** Verified facts are attributed above. Items marked **[best practice synthesis]** are professional convention, not a single cited claim. All company-specific details (positioning, service names, metrics) are **placeholders** — see §13 Assumptions.

---

## 4. Information Architecture

### 4.1 Public Face — Sitemap
```
/                         Landing (Home)
├── /services             Services overview (+ anchors per service)
├── /work                 Work / Case Studies (optional, recommended)
├── /team                 Team directory  ─────────► /team/[slug]  Staff Digital ID
├── /about                About / Story / Values
├── /contact              Contact + inquiry form
├── /privacy              Privacy Notice
├── /terms                Terms of Use
└── /support  (link)      ──► Ticketing system (client/partner entry point)
```
- **Nav (top):** Home · Services · Work · Team · About · Contact **[Get in Touch]** — 6 items + 1 CTA.
- **Footer:** quick links, legal, socials, contact summary, privacy link.

### 4.2 Internal Face — Sitemap
```
/internal                 Hub Dashboard (module launcher + KPIs)
├── /internal/login       Authentication gateway
├── /internal/content     Public Content Manager (landing/services/team copy)
├── /internal/directory   Staff Directory (internal, full data)
├── /internal/ids         Digital ID Manager (public/private field control + consent)
├── /internal/inquiries   Inquiry Inbox (contact form submissions)
├── /internal/settings    Profile & preferences
└── /ticketing  (link)    ──► Existing Ticketing Module
```
> **Essential-only rule:** only modules that (a) feed the public face or (b) protect operational integrity are included. Anything else belongs in the ticketing suite or future backlog.

### 4.3 Cross-Face Relationship
```
              ┌───────────────────────── PUBLIC FACE ─────────────────────────┐
              │  Landing · Services · Team · Staff IDs · Contact · Legal       │
              └───────────────▲───────────────────────────┬───────────────────┘
                              │ published content &        │ inquiries
                              │ approved profiles          ▼
┌──── INTERNAL FACE ──────────┴───────────────────────────────────────────────┐
│  Hub Dashboard · Content Manager · Directory · Digital ID Manager · Inbox    │
│  Hub /ticketing ───────► [ EXISTING TICKETING MODULE ]                       │
└──────────────────────────────────────────────────────────────────────────────┘
                              Shared: Next.js BFF · Strapi v5 · PostgreSQL
```

---

## 5. Public Face — Page Specifications

Each section lists purpose, block order, and key CTA. Wireframes in `wireframes/public/`.

### 5.1 Landing Page — `/`
| # | Section | Purpose | Content | CTA |
|---|---|---|---|---|
| 1 | **Top Nav** | Wayfinding | Logo · 6 links · theme-safe | Get in Touch |
| 2 | **Hero** | Value prop above the fold | H1 promise, subhead, 2 CTAs, hero visual/geometry | Primary: Get in Touch · Secondary: See Services |
| 3 | **Trust Bar** | Immediate credibility | Client/partner logos or key stats | — |
| 4 | **Services Grid** | What we do | 3–6 service cards (icon, title, one-liner) | Explore Services |
| 5 | **Value / Why Us** | Differentiation | 3 proof points or benefits | — |
| 6 | **Process** | Reduce uncertainty | 4-step horizontal timeline | — |
| 7 | **Featured Work** | Evidence | 2–3 case study cards | View Work |
| 8 | **Team Teaser** | Humanize | 3–4 staff digital ID cards | Meet the Team |
| 9 | **Testimonial** | Social proof | 1 quote + attribution | — |
| 10 | **Final CTA** | Convert | Big flat color block, headline + form/link | Start a Project |
| 11 | **Footer** | Navigation & legal | Links, contact, socials, privacy | — |

### 5.2 Services — `/services`
Hero (short) → service detail blocks (alternating left/right layout) → engagement models → FAQ → CTA.

### 5.3 Work / Case Studies — `/work` *(recommended)*
Filter row (static tags) → case study grid → results/metrics → CTA. Each card links to a detail page (wireframe can be a future page).

### 5.4 Team Directory — `/team`
Hero → filter/segment row → **responsive grid of Staff Digital ID cards** (avatar, name, role, department, 1-line bio, "View profile") → join-us CTA.

### 5.5 Staff Digital ID — `/team/[slug]` ★
The centerpiece "public identity" page. **Shows only public-safe fields.**
| Block | Content | Privacy |
|---|---|---|
| Header | Avatar, Display name, Role/Title, Department, status badge | Public |
| Short bio | 2–4 sentences, professional only | Public |
| Focus areas / skills | Tags | Public |
| Contact (work) | Work email, desk phone, location (city only) | Public (opt-in per field) |
| Professional links | LinkedIn / GitHub / portfolio | Public (opt-in) |
| "Contact via form" | Protected contact path instead of exposing email | Public |
| Internal-only | *(never rendered on this page)* | Hidden |
| Privacy note | "This profile shows only work information you approved. Request changes." | Public |

### 5.6 About — `/about`
Story → mission/values → milestones timeline → culture images → CTA.

### 5.7 Contact — `/contact`
Intro → **inquiry form** (name, email, company, subject, message, consent checkbox) → direct contact details → map/office block → response-time note.

### 5.8 Legal — `/privacy`, `/terms`
Plain-language privacy notice covering public staff data, cookies, and inquiry handling. Required by the transparency principle (§3.3).

---

## 6. Staff Digital ID — Data & Privacy Model

### 6.1 Field Classification
| Field | Tier | Public page | Notes |
|---|---|---|---|
| `displayName` | Public | ✅ | |
| `roleTitle` | Public | ✅ | e.g., "Lead Engineer" |
| `department` | Public | ✅ | |
| `shortBio` | Public | ✅ | Professional only, reviewed |
| `avatar` | Public | ✅ | Approved photo |
| `workEmail` | Public (opt-in) | ✅ | Or hidden behind contact form |
| `workPhone` | Public (opt-in) | ✅ | Desk line only |
| `locationCity` | Public (opt-in) | ✅ | City only, never address |
| `skills[]` | Public | ✅ | |
| `links[]` | Public (opt-in) | ✅ | Professional only |
| `profileStatus` | Public | ✅ | e.g., "Available / Focused" |
| `legalName` | Internal | ❌ | |
| `personalEmail` | Internal | ❌ | |
| `personalPhone` | Internal | ❌ | |
| `employmentStart` | Internal | ❌ | |
| `manager` | Internal | ❌ | |
| `internalId` | Internal | ❌ | |
| `homeAddress` | Sensitive | ❌ | Never publish |
| `governmentId` | Sensitive | ❌ | Never publish |
| `salary` | Sensitive | ❌ | Never publish |
| `hrNotes` | Sensitive | ❌ | Never publish |

### 6.2 Consent & Governance
- `consentGiven` (bool), `consentDate`, `consentScope[]` — recorded per staff member.
- `approvedBy` + `approvedAt` — publication approval audit.
- `lastReviewedAt` — periodic accuracy check (accuracy principle).
- **Publication gate:** a profile is only rendered publicly when `consentGiven = true` **and** `profileStatus = published`.
- **Removal:** self-service request processes within SLA; departed staff profiles removed promptly (storage limitation).

---

## 7. Internal Face — Module Specifications

Wireframes in `wireframes/internal/`. Essential only.

### 7.1 `/internal/login`
Email + password, "remember me", forgot-password link, security note. Reuses the existing **BFF + httpOnly cookie** auth pattern from the ticketing module.

### 7.2 `/internal` — Hub Dashboard
- Welcome header + user + role badge
- **Module launcher cards:** Ticketing (existing), Content, Directory, Digital IDs, Inquiries
- **Essential KPIs:** new inquiries, profiles pending consent, draft content, system status
- **Activity / alerts:** e.g., "2 profiles awaiting approval"
- **Quick actions**

### 7.3 `/internal/directory` — Staff Directory (internal)
Table/grid of **all** staff with full internal fields. Filter by department/role/status. Row actions: view, edit, open public profile, deactivate. This is the source of truth for the public profiles.

### 7.4 `/internal/ids` — Digital ID Manager ★
- List of profiles with **publication state** (Draft / Pending consent / Published / Retired).
- **Public/Private field toggles** per staff member.
- **Consent panel** (given? scope? date?).
- **Live preview** pane (what the public sees).
- **Approval + audit** actions.

### 7.5 `/internal/content` — Public Content Manager
Edit landing hero, services, about copy, featured work, footer. Publishing workflow (Draft → Review → Published). Backed by Strapi content types.

### 7.6 `/internal/inquiries` — Inquiry Inbox
List of contact-form submissions: status (New / In Progress / Closed), assignee, source page, timestamp. Detail pane with the message and reply/archive actions. Feeds directly from the public contact form.

### 7.7 `/internal/settings`
Own profile + password + preferences. Mirrors the existing ticketing `settings` pattern for consistency.

---

## 8. Design System — Flat-Modern (2.0)

### 8.1 Principles
1. **Flat color blocks over gradients** — bold, confident surfaces.
2. **Big, tight type** for hierarchy; generous negative space.
3. **Subtle depth only where clickable** (Flat 2.0 fix): `shadow-sm`, 1px borders, hover color shifts.
4. **Geometric decoration** — circles, arcs, grids as flat SVG accents (no imagery dependency).
5. **One clear focal point per screen.**
6. **Accessible by default** — AA contrast, focus rings, semantic HTML.

### 8.2 Color Tokens & Brand Identity (Tailwind mapping)
- **Brand Name:** Always stylized in lowercase without capital letters: **`appardas`**.
- **Official Logo:** Continuous ribbon/infinity "A" emblem with warm caramel/amber gradient, deep bronze undertones, and titanium/bone grey curved cap.

| Token | Value | Tailwind | Use |
|---|---|---|---|
| Ink | `#1C1917` | `stone-900` | Text, dark surfaces, hero & footer |
| Surface | `#FFFFFF` | `white` | Cards, page background |
| Muted Surface | `#FAFAF9` | `stone-50` | Section bands, alternate rows |
| Primary / Brand | `#D97706` / `#B45309` | `amber-600` / `amber-700` | CTAs, active states, text links |
| Primary Hover | `#B45309` / `#92400E` | `amber-700` / `amber-800` | Hover states |
| Accent / Highlight | `#F59E0B` | `amber-500` | Artistic pops, notification dots, glow |
| Success | `#10B981` | `emerald-500` | Status, positive indicators |
| Warning / Draft | `#F59E0B` | `amber-500` | Pending states |
| Danger / Revoked | `#F43F5E` | `rose-500` | Errors, revoked states |
| Border | `#E7E5E4` | `stone-200` | Dividers, card borders |
| Muted Text | `#78716C` | `stone-500` | Supporting copy |

> Contrast check: `stone-900` on `white` ≈ 17.5:1 (AAA); `amber-700` on `white` ≈ 5.02:1 (AA for normal text); `white` on `amber-600` ≈ 3.2:1 (AA large / CTA buttons) and `white` on `amber-700` ≈ 5.02:1 (AA normal text) — fully accessible.

### 8.3 Typography
| Role | Font | Tailwind |
|---|---|---|
| Display/Headings | Space Grotesk (fallback system) | `font-black tracking-tight` |
| Body/UI | Inter (fallback system) | `font-normal leading-relaxed` |

Scale: `text-5xl/6xl` hero → `text-4xl` section → `text-lg` lead → `text-base` body → `text-xs uppercase tracking-widest` eyebrow labels.

### 8.4 Spacing, Radius, Elevation
- **Rhythm:** 4/8px base; sections `py-20 md:py-28`; containers `max-w-7xl px-6`.
- **Radius:** `rounded-2xl` cards, `rounded-full` pills/avatars.
- **Elevation:** flat by default; `shadow-sm` on interactive, `shadow-md` on hover.

### 8.5 Components (wireframe coverage)
Top nav with official logo + `appardas` wordmark, buttons (`btn-primary`, `btn-secondary`, `btn-ghost`), badge/pill, card, stat, avatar, section header (eyebrow + title + lead), form field, table row, sidebar nav, module launcher card, empty/status states.

### 8.6 Motion
Wireframes use **zero JavaScript**. In production, motion is limited to CSS transitions (150–200ms) for hover/focus and simple fade/slide on scroll. No autoplay, no parallax.

### 8.7 Accessibility Rules
- Semantic landmarks (`header`, `nav`, `main`, `footer`, `section`).
- Visible focus (`focus-visible:ring-2 ring-amber-500 ring-offset-2`).
- All images/decorative blocks have `alt` or `aria-hidden`.
- Form inputs have `<label>`.
- Contrast ≥ 4.5:1; never color-only status (icon + text).

---

## 9. Technical Architecture & Integration

### 9.1 Reuse the Proven Stack
Match the existing ticketing module exactly (no new paradigm):

| Layer | Technology | Notes |
|---|---|---|
| Frontend | **Next.js 14 (App Router)** | Public routes = static/SSG; Internal = dynamic |
| Styling | **Tailwind CSS** (+ `shadcn/ui` primitives adapted) | Same design tokens |
| Backend / CMS | **Strapi v5** | Content types + REST via Document Service |
| Database | **PostgreSQL** | Shared instance, separate collections |
| Auth | Strapi Users & Permissions + custom policies | Same BFF cookie pattern |
| Data fetching | Server Components for public; TanStack Query for internal | As ticketing |

### 9.2 Rendering Strategy
- **Public pages:** `export const revalidate` (ISR) / static generation for speed and SEO; content pulled from Strapi at build/revalidate time.
- **Staff profiles:** generated from published StaffProfile documents; only public fields selected in the query.
- **Internal pages:** server-rendered behind auth middleware, identical guard approach to ticketing (`middleware.ts`).
- **BFF:** reuse `/api/[...proxy]` pattern; JWT stays in httpOnly cookie, never client-side.

### 9.3 Security
- Same **zero client-side token exposure** guarantee as the ticketing module.
- **Field-level projection:** the public API/query must never return internal/sensitive fields — enforce at the Strapi controller, not just the UI.
- Rate-limit the public contact form + add spam protection (honeypot/CAPTCHA).
- HTTPS only; security headers (CSP, HSTS).
- Publication gate enforced server-side (consent + approved).

### 9.4 Proposed Strapi Content Types (new)
| Content Type | Purpose | Key fields |
|---|---|---|
| `StaffProfile` | Public digital ID + private source data | all §6.1 fields + consent/governance fields |
| `Service` | Public services | title, slug, summary, body, icon, order |
| `CaseStudy` | Work items | title, slug, client, summary, metrics[], media |
| `SiteContent` (single type) | Landing/about/global copy | hero, CTAs, footer, socials |
| `Inquiry` | Contact submissions | name, email, company, subject, message, consent, status, source |
| `LegalPage` | Privacy/Terms | title, slug, body, updatedAt |

> Reuse existing `User`/RBAC from ticketing for internal auth; add policies `is-content-editor`, `is-hr-admin` as needed.

---

## 10. Wireframe Inventory

All wireframes are **static HTML + Tailwind (Play CDN), no JavaScript**.

### Public Face (`wireframes/public/`)
| File | Page |
|---|---|
| `index.html` | Landing / Home |
| `services.html` | Services |
| `work.html` | Work / Case Studies |
| `team.html` | Team Directory |
| `staff-profile.html` | Staff Digital ID (detail) |
| `about.html` | About |
| `contact.html` | Contact |
| `privacy.html` | Privacy Notice |

### Internal Face (`wireframes/internal/`)
| File | Page |
|---|---|
| `login.html` | Internal Login |
| `dashboard.html` | Hub Dashboard (module launcher) |
| `directory.html` | Staff Directory (internal) |
| `id-manager.html` | Digital ID Manager |
| `content.html` | Public Content Manager |
| `inquiries.html` | Inquiry Inbox |
| `settings.html` | Profile & Settings |

### Index
| File | Purpose |
|---|---|
| `wireframes/index.html` | Visual gallery linking every wireframe |

**How to view:** open `wireframes/index.html` in a browser (internet needed for the Tailwind CDN + Google Fonts). No build step.

---

## 11. Build Roadmap (Suggested Phases)

| Phase | Deliverable | Exit criteria |
|---|---|---|
| **0. Align** | Approve this plan, confirm brand/positioning, confirm service list | Sign-off on §13 assumptions |
| **1. Foundations** | Design tokens, base components, Next.js route shells, Strapi content types | Empty pages render with shared nav/footer |
| **2. Public Face** | Landing + Services + About + Contact (+ legal) | Content editable in Strapi; contact form writes Inquiry |
| **3. Staff Digital ID** | Team directory + profile pages + Digital ID Manager + consent | Only consented+approved fields render publicly |
| **4. Internal Face** | Login, Dashboard, Content, Directory, Inquiries, Settings | RBAC enforced; ticketing linked via launcher |
| **5. Hardening** | A11y audit (AA), performance budget, security headers, spam protection | Lighthouse ≥ 90 a11y/perf on public pages |
| **6. Launch** | SEO, analytics, monitoring, legal review | Live + monitored |

---

## 12. Risks & Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| Publishing staff PII accidentally | Legal/trust | Server-side field projection + publication gate + consent audit |
| Pure-flat design hurts usability | Lower conversion | Adopt Flat 2.0: subtle depth on interactive elements |
| Divergence from ticketing stack | Maintenance cost | Reuse stack, tokens, BFF and auth patterns |
| Scope creep in internal face | Overbuild | "Essential-only" rule + phase gate |
| Content goes stale | Accuracy principle breach | Content Manager + review reminders |
| Contact form spam | Ops noise | Honeypot/CAPTCHA + rate limiting |
| Slow public pages | SEO/conversion loss | ISR/static + image optimization + CDN |

---

## 13. Assumptions & Open Questions

**Assumptions (confirm or correct):**
1. "Appardas" is a software/digital solutions company; the ticketing module is an internal tool, so it is **not** sold publicly.
2. The hub shares the ticketing module's Next.js + Strapi + PostgreSQL stack.
3. "Public information" for staff means professional, work-related data only.
4. Ticketing remains functionally unchanged; the hub only links to it.
5. Wireframes use placeholder brand copy, service names, and metrics.

**Open questions:**
- Should the public site expose any client-facing ticketing/support entry point, or is ticketing strictly internal?
- Languages/locales required? (Affects IA and content modelling.)
- Do you want a `/work` case-studies section in v1 or defer it?
- Who is the data controller and what retention period applies to inquiries/staff profiles?
- Confirm whether work email and phone are public by default or opt-in (plan assumes opt-in).

---

## 14. Definition of Done (for this deliverable)
- [x] Research-backed plan with sources.
- [x] Two-face sitemap and page specs.
- [x] Staff Digital ID privacy/data model.
- [x] Design system (flat-modern 2.0).
- [x] Technical architecture reusing the existing stack.
- [x] Static HTML + Tailwind wireframes for public, staff ID, and internal faces.
- [x] Wireframe gallery index.
