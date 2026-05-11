"""
Batch C fixes for openclaw-architecture-explorer.
- Add inline SVG favicon (fixes favicon.ico 404)
- Fix footer h4 -> h3 (heading-order WCAG)
- Add closing CTA section + author/contact strip (Recruiter mindset closure)
- Lower font-weight 800 references where appropriate
- Inject author-strip CSS
"""
import re
from pathlib import Path

HTML = Path(r"C:\Users\chris\Downloads\openclaw-architecture-explorer\index.html")
src = HTML.read_text(encoding="utf-8")
changes = []

# === 1. Inline SVG favicon (no external file needed) ===
favicon_link = '<link rel="icon" type="image/svg+xml" href=\'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><polygon points="16,2 29,9.5 29,22.5 16,30 3,22.5 3,9.5" fill="%23043886"/><polygon points="16,8 23.5,12.25 23.5,19.75 16,24 8.5,19.75 8.5,12.25" fill="%23169EE3"/><circle cx="16" cy="16" r="2.6" fill="%23fff"/></svg>\' />'
if 'rel="icon"' not in src:
    src = src.replace(
        '<link rel="stylesheet" href="css/finexio-tokens.css" />',
        favicon_link + '\n<link rel="stylesheet" href="css/finexio-tokens.css" />',
        1
    )
    changes.append("added inline SVG favicon (Booya Jones hexagon mark)")

# === 2. Footer h4 -> h3 (heading-order: h2 -> h3, not h2 -> h4) ===
footer_h4_count = src.count('      <h4>')
if footer_h4_count:
    src = src.replace('      <h4>', '      <h3>')
    src = src.replace('</h4>\n      <ul class="foot-list">', '</h3>\n      <ul class="foot-list">')
    changes.append(f"footer h4 -> h3 (x{footer_h4_count})")

# === 3. Closing CTA + author/contact strip BEFORE </main> ===
closing_section = '''
<!-- ============== CLOSING / CONTACT ============== -->
<section class="closing" id="closing" aria-labelledby="closing-h">
  <div class="wrap closing-inner">
    <div class="closing-copy">
      <div class="closing-eyebrow">End of tour</div>
      <h2 id="closing-h" class="closing-h">That's the whole stack, live and wired.</h2>
      <p class="closing-lede">Everything above is in production. One Node.js process, 23 nightly crons, 25 integrations, 5 LLM providers, 42 projects, all driven from Slack. If you're curious how a single operator runs this much surface area solo, the source is open.</p>
    </div>
    <div class="closing-actions">
      <a class="closing-cta primary" href="https://github.com/booyajones/openclaw-architecture-explorer" target="_blank" rel="noopener">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 .5C5.65.5.5 5.65.5 12c0 5.08 3.29 9.39 7.86 10.91.58.1.79-.25.79-.56 0-.28-.01-1.02-.02-2-3.2.69-3.87-1.54-3.87-1.54-.52-1.33-1.28-1.69-1.28-1.69-1.05-.72.08-.71.08-.71 1.16.08 1.77 1.19 1.77 1.19 1.03 1.77 2.71 1.26 3.37.96.1-.75.4-1.26.73-1.55-2.55-.29-5.24-1.28-5.24-5.69 0-1.26.45-2.29 1.18-3.1-.12-.29-.51-1.46.11-3.05 0 0 .97-.31 3.18 1.18.92-.26 1.91-.39 2.89-.39.98 0 1.97.13 2.89.39 2.21-1.49 3.18-1.18 3.18-1.18.62 1.59.23 2.76.11 3.05.74.81 1.18 1.84 1.18 3.1 0 4.42-2.69 5.39-5.25 5.68.41.36.78 1.06.78 2.14 0 1.55-.01 2.79-.01 3.17 0 .31.21.67.8.56C20.21 21.39 23.5 17.08 23.5 12 23.5 5.65 18.35.5 12 .5z"/></svg>
        Browse the source
      </a>
      <a class="closing-cta secondary" href="https://chriswyatt.dev" target="_blank" rel="noopener">More from Chris Wyatt</a>
    </div>
    <div class="closing-byline">
      Built by <a href="https://chriswyatt.dev" target="_blank" rel="noopener"><b>Chris Wyatt</b></a>
      <span class="closing-sep">/</span>
      <a href="https://www.linkedin.com/in/chriswyatt1/" target="_blank" rel="noopener">LinkedIn</a>
      <span class="closing-sep">/</span>
      <a href="https://github.com/booyajones" target="_blank" rel="noopener">GitHub</a>
      <span class="closing-sep">/</span>
      Reach: <a href="mailto:chris@finexio.com">chris@finexio.com</a>
    </div>
  </div>
</section>
'''

if 'id="closing"' not in src:
    src = src.replace('</main>', closing_section + '\n</main>', 1)
    changes.append("added closing CTA + author strip")

# === 4. CSS for closing section ===
closing_css = '''
/* === CLOSING / CONTACT SECTION === */
.closing {
  background: linear-gradient(180deg, #050B1A 0%, #081229 100%);
  border-top: 1px solid var(--mc-line);
  padding: 88px 0 96px;
}
.closing-inner { display: grid; grid-template-columns: 1fr; gap: 28px; max-width: 880px; }
.closing-eyebrow {
  font-family: var(--font-caption);
  font-size: 11px; font-weight: 700; letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--mc-blue-soft); margin-bottom: 14px;
}
.closing-h {
  font-family: var(--font-display); font-weight: 700;
  font-size: clamp(30px, 4vw, 48px); line-height: 1.08;
  letter-spacing: -0.022em;
  color: var(--mc-text); margin: 0 0 18px;
}
.closing-lede {
  font-size: 17px; line-height: 1.6;
  color: var(--mc-text-2); max-width: 620px; margin: 0 0 28px;
}
.closing-actions { display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 28px; }
.closing-cta {
  display: inline-flex; align-items: center; gap: 8px;
  padding: 12px 18px; border-radius: 10px;
  font-family: var(--font-display); font-weight: 600;
  font-size: 14px; letter-spacing: 0.005em;
  text-decoration: none;
  transition: transform 120ms, box-shadow 160ms, background 160ms;
}
.closing-cta.primary {
  background: var(--mc-blue); color: #fff;
  box-shadow: 0 8px 22px rgba(22,158,227,0.28);
}
.closing-cta.primary:hover { transform: translateY(-1px); background: #1FB0F4; box-shadow: 0 12px 28px rgba(22,158,227,0.36); }
.closing-cta.secondary {
  background: rgba(255,255,255,0.04);
  border: 1px solid var(--mc-line-strong);
  color: var(--mc-text);
}
.closing-cta.secondary:hover { background: rgba(255,255,255,0.08); border-color: var(--mc-blue-soft); }
.closing-byline {
  font-family: var(--font-mono);
  font-size: 12px; color: var(--mc-text-3);
  display: flex; flex-wrap: wrap; gap: 8px; align-items: center;
}
.closing-byline a { color: var(--mc-text-2); text-decoration: none; border-bottom: 1px solid var(--mc-line); }
.closing-byline a:hover { color: var(--mc-blue-soft); border-bottom-color: var(--mc-blue-soft); }
.closing-byline b { color: var(--mc-text); font-weight: 700; }
.closing-sep { color: var(--mc-text-3); }
@media (max-width: 600px) {
  .closing-actions { flex-direction: column; align-items: stretch; }
  .closing-cta { justify-content: center; }
}
'''
marker = "</style>\n</head>"
if "CLOSING / CONTACT SECTION" not in src and marker in src:
    src = src.replace(marker, closing_css + "\n" + marker, 1)
    changes.append("injected closing-section CSS")

# === 5. Reduce a few non-hero font-weight 800 to 700 (brand max for DM Sans Bold) ===
# Keep display weights at 700 max. Stat numbers, df-core-label, integ-glyph, memory-subhead all use 800.
# Drop them to 700 for brand discipline. The 800 in body.font-feature-settings does not affect weight.
weight_sites = [
    (".hero-stats .stat-num { font-family: var(--font-display); font-weight: 800;",
     ".hero-stats .stat-num { font-family: var(--font-display); font-weight: 700;"),
    (".df-core-label { fill: #fff; font-family: var(--font-display); font-weight: 800;",
     ".df-core-label { fill: #fff; font-family: var(--font-display); font-weight: 700;"),
    (".integ-glyph { width: 32px; height: 32px; flex-shrink: 0; border-radius: 8px; display: inline-flex; align-items: center; justify-content: center; font-family: var(--font-display); font-weight: 800; font-size: 13px; color: #fff; }",
     ".integ-glyph { width: 32px; height: 32px; flex-shrink: 0; border-radius: 8px; display: inline-flex; align-items: center; justify-content: center; font-family: var(--font-display); font-weight: 700; font-size: 13px; color: #fff; }"),
    (".memory-subhead { margin: 36px 0 14px; font-family: var(--font-caption); font-size: 11px; font-weight: 800;",
     ".memory-subhead { margin: 36px 0 14px; font-family: var(--font-caption); font-size: 11px; font-weight: 700;"),
]
for old, new in weight_sites:
    if old in src:
        src = src.replace(old, new, 1)
        changes.append(f"font-weight 800 -> 700 on {old.split(' ')[0]}")

# === 6. Lock down letter-spacing token drift: keep 0.06, 0.08, 0.12, 0.18 only ===
# Already mostly clean; leave as-is, would need more careful review to consolidate

# Write
HTML.write_text(src, encoding="utf-8")
print("== Batch C changes ==")
for c in changes:
    print(f"  - {c}")
