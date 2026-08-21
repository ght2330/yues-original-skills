# Design Reference Source Catalog

Use this catalog to choose sources by job. Verify individual candidate pages at run time; a working homepage does not guarantee every case page is public.

## Awwwards

- Official URL: https://www.awwwards.com/
- Primary role: visual direction and experiential storytelling.
- Best for: brand sites, campaigns, portfolios, editorial experiences, expressive landing pages.
- Inspect: first-screen composition, type/image relationship, scroll rhythm, transitions, brand voice, and memorable interaction moments.
- Access: canonical public site; direct access timed out from the current environment on 2026-07-17, so verify candidate pages before claiming visual inspection.
- Risk: award-oriented sites often sacrifice clarity, accessibility, loading cost, and repeated-task efficiency. Do not use as the main structure source for SaaS or dashboards.

## Mobbin

- Official URL: https://mobbin.com/
- Primary role: product structure and interaction patterns.
- Best for: mobile apps, web apps, onboarding, authentication, subscription, checkout, settings, dashboards, and operational workflows.
- Inspect: information hierarchy, task sequence, component states, navigation, empty/error/loading states, and density.
- Access: homepage returned HTTP 200 on 2026-07-17; some screenshot depth and search features may require an account or paid plan.
- Risk: copying isolated screens without their product context can produce inconsistent flows. Use patterns, not branded UI.

## Recent

- Official URL: https://recent.design/
- Primary role: broad visual and trend discovery.
- Best for: early direction finding across web, branding, typography, illustration, motion, and adjacent visual disciplines.
- Inspect: repeated visual motifs, current typography, color use, composition, and cross-discipline ideas that can translate into web rules.
- Access: homepage returned HTTP 200 on 2026-07-17 and identifies itself as design inspiration.
- Risk: trend aggregation can encourage novelty without product fit. Require a brief-specific reason before promoting a trend into the contract.

## Unicorn Studio

- Official URL: https://www.unicorn.studio/
- Primary role: WebGL, motion, and interactive visual references.
- Best for: approved expressive hero scenes, product storytelling, interactive backgrounds, and motion-led brand experiences.
- Inspect: interaction trigger, visual hierarchy, fallback behavior, embed path, and performance cost.
- Access: homepage returned HTTP 200 on 2026-07-17 and positions the product as a no-code WebGL tool for web embeds.
- Risk: continuous rendering can harm mobile performance, accessibility, and content clarity. Require explicit approval, reduced-motion behavior, and a performance budget.

## MotionSites

- Official URL: https://motionsites.ai/
- Primary role: AI-oriented hero, animation, and prompt references.
- Best for: landing-page hero exploration, animated backgrounds, gradients, and prompt vocabulary for AI website builders.
- Inspect: hero scale, content placement, background behavior, CTA treatment, animation purpose, and what the prompt makes explicit.
- Access: homepage returned HTTP 200 on 2026-07-17 and describes a library of AI website prompts, apps, and animations. The similarly named `motionsites.com` was not the verified site.
- Risk: prompt libraries can reproduce generic spectacle. Translate examples into project-specific rules and avoid stacking multiple attention effects.

## Refero Styles

- Official URL: https://styles.refero.design/
- Parent product: https://refero.design/
- Primary role: AI-readable design-system references and `DESIGN.md` examples.
- Best for: turning selected visual direction into explicit color, typography, spacing, component, and density rules for coding agents.
- Inspect: token naming, hierarchy, component conventions, rule specificity, and how reference evidence maps to implementation instructions.
- Access: both domains returned HTTP 200 on 2026-07-17; availability of specific examples may change.
- Risk: a borrowed design file may conflict with the project's existing component library or brand. Merge by explicit diff and preserve compatible local rules.

## Routing By Project Type

### Expressive Marketing, Brand, Or Portfolio

- Visual: Awwwards or Recent.
- Structure: Mobbin or a comparable real product/marketing flow.
- Motion: MotionSites or Unicorn Studio when the brief requires it.
- Contract: Refero Styles for explicit rules.

### SaaS, Dashboard, Or Operational Tool

- Structure first: Mobbin and real product examples.
- Visual: restrained examples from Recent or relevant product cases.
- Design system: Refero Styles plus the existing project system.
- Motion: state feedback only unless the user explicitly approves an expressive use case.

### Restrained Content Or Static Site

- Visual: Recent and relevant Awwwards editorial examples.
- Structure: content-first real sites or Mobbin web flows.
- Design system: Refero Styles.
- Motion: usually `N/A` or limited to meaningful transitions.

