# Daniela Hotz — Healthcare Analytics & Business Intelligence

A responsive English-language portfolio designed for static hosting, including GitHub Pages. No build step, package installation, tracking or external font requests are required.

## Preview

Open `index.html` in a browser, or run `python -m http.server 8000` in this folder and visit `http://localhost:8000`.

## Contents

- Home: selected work, professional background, LinkedIn and code demonstrations.
- Three navigable case pages: healthcare costs, chronic population analytics and forecasting.
- Self-contained SVG charts with original aggregate study data. The hero visual remains illustrative.
- Two runnable Python demonstrations using synthetic data and the standard library.

## Content status

This is the first working version. Case narratives are conservative summaries of the supplied professional context and scripts. They do not publish original patient records, financial values, internal PDFs, model accuracy claims or unverified savings. Case figures reproduce selected original aggregate study results with the organization name anonymized. The hero remains illustrative. The classification demo is dictionary-based and requires review; it does not perform clinical diagnosis. The seasonal-naive demonstration is separate from the original SARIMAX project.

Before adding substantive results, prepare a public dataset and reproducible analysis, validate classification rules, and confirm the personal contribution, tool use and wording for each case. The cost case includes nominal expenditure, membership and cost-per-member comparisons. Oncology and governance appear as areas of expertise, not completed standalone cases.

## GitHub setup

The GitHub profile URL provided by Daniela is https://github.com/DHOTZ8/. The header links to this profile. The intended user-site repository is DHOTZ8.github.io; the repository exists and GitHub Pages has been activated. The LinkedIn URL is taken from the supplied profile.

For publication, use the contents of this folder at the repository root; `.nojekyll` is included. Connect the repository to the user's GitHub account before deployment. The site is published through GitHub Pages.

## Editing

- `index.html`: homepage copy and navigation.
- `assets/style.css`: colors, spacing, desktop and mobile layouts.
- `cases/*.html`: individual case narratives.
- `assets/*.svg`: illustrations.
- `code/*.py`: public synthetic-data examples.

The site uses system serif typography, so there are no external font dependencies. Relative links support both root and repository-subpath hosting.
