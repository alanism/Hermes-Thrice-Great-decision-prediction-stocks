---
version: alpha
name: Five Stocks — Editorial Research
description: Offline editorial research magazine with source-bound financial calculations.
colors:
  primary: "#000"
  secondary: "#454545"
  tertiary: "#ffc500"
  neutral: "#fdfcf3"
  rule: "#d9d9d9"
typography:
  h1:
    fontFamily: Georgia
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1.04
    letterSpacing: "-0.04em"
  body-md:
    fontFamily: Georgia
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.55
  label-caps:
    fontFamily: Arial
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0.05em
rounded:
  none: 0px
spacing:
  sm: 8px
  md: 16px
  lg: 24px
  section: 40px
components:
  button:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary}"
    rounded: "{rounded.none}"
    height: 44px
  focus:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.primary}"
  metadata:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.secondary}"
  separator:
    backgroundColor: "{colors.rule}"
  ledger:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary}"
---

## Overview

**Primary surface: Decide / Learn.** This is an editorial financial-research magazine, not a monitoring dashboard. The PDF is a static evidence edition of the same article, not a second financial analysis. Tokens describe the implemented HTML; responsive and print exceptions below are part of this specification.

Use the general editorial principles of the existing [Monocle reference](../../design/DESIGN-Monocle.md), with the Satori six-column/four-plus-two reading grid. The [Creative Giants](../../design/DESIGN-Creative%20Giants.md) and [Ease Health](../../design/DESIGN-Ease%20Health.md) files remain alternative references, not competing themes. This is an original composition, not an official Monocle publication or endorsement.

The hierarchy is: opening conclusion and objection; history and the position illustration; **actual native financial calculations**; macro uncertainty; upstream Page diagnostics; eight simulated investor essays; constraints and the source ledger. Adverse findings must remain visible. Numbers in a code block or a heading alone do not establish that an engine ran.

## Colors

- Ink `#000`: body, headlines, outlines and numerals.
- Paper `#fdfcf3`: warm, untextured reading surface; print uses white.
- Signal `#ffc500`: keyboard focus, restrained annotations, and correlation encoding. Yellow does not mean a purchase recommendation.
- Metadata `#454545`: secondary source context.
- Rule `#d9d9d9`: non-text separators, not a low-contrast text color.

No gradient, glass effect, rainbow market sentiment, or decorative price tile.

## Typography

Georgia / Times New Roman / serif for reading; Arial / sans-serif for captions, controls and metadata. No remote fonts. Body is 18px with 1.55 line height; essays use 1.6. The desktop cover scales to 64px, with 38px and 32px narrow-screen exceptions. Feature headings scale from 29px to 40px. Use tabular numerals in financial tables, explicit USD/%/session units, and the exact observed AVGO quote of **295.345 USD**.

Print body, cells, source notes, receipt text and scaled SVG labels are at least **12pt**. Keep word wrapping for long hashes and URLs. PDF footer is 12pt. Do not shrink financial text to make an unreviewed page count look tidy.

## Layout

Maximum article width 1280px; six equal columns with 24px gutters. Prose uses four columns, with a two-column margin note. Figures interrupt the article at the point where their data are discussed. The essays are two columns on desktop and one column on narrow screens. At 900px and below, feature grids collapse to a single reading flow. Native wide-table scrolling is local, not page-wide overflow. The implemented HTML was exercised at 1920, 768, 390 and 280px.

The primary finance tables must stay outside disclosures. Secondary ledgers and provenance use native `details` / `summary`, with 44px targets and predictable keyboard behavior. Six source-capture folios are real screenshots, not recreated market graphics. Do not replace them with simulated screens.

PDF: A4 portrait, 12mm top/side margins and 20mm bottom margin. The export uses 18.5px SVG-label CSS to retain at least 12pt after physical scaling, adds an 18px correlation-label gutter, and limits capture images to 170mm so provenance stays with its image. These are PDF-only adaptations; the published HTML remains byte-identical to the verified interactive report. Open evidence disclosures, eagerly load every capture, disable animation and print final SVG geometry. Preserve all eight 200-word essays, all 25 tables, and the exact underlying HTML values. Check exported pages, not only print-media CSS.

## Elevation & Depth

Flat paper. Hierarchy comes from type, spacing, rules, numbered features and alignment. No shadows, floating cards or overlay stacks in the article.

## Shapes

Square rules and controls; no oversized rounded containers. Use line patterns as well as labels to distinguish five historical series without depending on color.

## Components

Five figures: 501-session adjusted-price history with a real date slider; original illustrative allocation comparison; raw macro books with horizon/resolution context; Page tail-fit diagnostics; and the 5×5 correlation matrix. D3.js 7.9.2 is embedded with its license. No runtime CDN, font, API or data requests.

Animation must reveal actual geometry. Pause completes the geometry; replay works; reduced-motion and print produce final static values. Matrix inspection is keyboard-operable. The PDF freezes one meaningful view of each figure; HTML remains the interactive edition, and the printed raw ledgers/captures carry the other macro books.

The Enochian atlas was considered as the user's default control source. Existing native controls and the explicit editorial style take precedence; no Enochian code, proprietary control replica or new license obligation is imported into this bundle.

## Do's and Don'ts

- Keep the exact evidence labels **measured / calculate / modeled / forecasted**.
- Pair numeric outputs with assumptions, formula/case bindings and counterevidence.
- Distinguish historical Sharpe from forward performance; constant cash rates are assumptions, not retrieved Treasury yields.
- Distinguish conditional Kelly references from approved portfolio weights; standalone references do not add up to an allocation.
- State that full binary-Kelly fractions fail retained full-path log-growth domains; a capped reference passing sampled paths is not proof of safety or optimality.
- Convexity score is finite scenario asymmetry, not option gamma.
- Label the eight essays as simulated lenses, not actual opinions or endorsements.
- Never silently normalize an incoherent prediction-market book, refresh only part of a snapshot, substitute fabricated data, or hide a negative finding.
- Never publish brokerage holdings, private account information, credentials or local runtime folders with this public hypothetical report.
