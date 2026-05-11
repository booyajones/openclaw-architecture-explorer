"""
Batch B fixes for openclaw-architecture-explorer.
- Add skip-to-content link
- Wrap content in <main id="content">
- Remove role="tablist" from filter rows (they're chip filters, not tabs)
- Add :focus-visible system
- Wire project card click handler
- Add aria-current to active nav
- Wire cmdk focus management improvements
- Mobile nav hamburger
"""
import re
from pathlib import Path

HTML = Path(r"C:\Users\chris\Downloads\openclaw-architecture-explorer\index.html")
src = HTML.read_text(encoding="utf-8")
changes = []

# === 1. Remove role="tablist" from filter chips (a11y: filter chips are not tabs) ===
before = src.count('role="tablist"')
src = src.replace('role="tablist"', 'role="group" aria-label="Filter"')
after = src.count('role="tablist"')
changes.append(f"role=tablist -> group on {before - after} filter rows")

# === 2. Skip-to-content link, just after <body> ===
if 'class="skip-link"' not in src:
    src = src.replace(
        "<body>\n",
        '<body>\n<a href="#content" class="skip-link">Skip to main content</a>\n',
        1
    )
    changes.append("added skip-to-content link")

# === 3. Wrap content in <main id="content"> ===
# Open <main> right after <a id="top"></a>, close </main> right before <footer class="foot">
if '<main id="content">' not in src:
    src = src.replace('<a id="top"></a>\n', '<a id="top"></a>\n<main id="content">\n', 1)
    src = src.replace('<footer class="foot">', '</main>\n\n<footer class="foot">', 1)
    changes.append("wrapped content in <main id='content'>")

# === 4. Inject :focus-visible system + skip-link styles + mobile hamburger styles ===
focus_css = """
/* === A11Y: focus-visible system (added 2026-05-11 council) === */
:focus { outline: none; }
:focus-visible {
  outline: 2px solid var(--mc-blue-soft);
  outline-offset: 2px;
  border-radius: 6px;
}
a:focus-visible, button:focus-visible, [role="button"]:focus-visible, [tabindex]:focus-visible,
input:focus-visible, kbd:focus-visible {
  outline: 2px solid var(--mc-blue-soft);
  outline-offset: 2px;
}
.search-trigger:focus-visible, .filter-chip:focus-visible, .icon-btn:focus-visible,
.proj-item:focus-visible, .integ-card:focus-visible, .cron-row:focus-visible {
  outline: 2px solid var(--mc-blue-soft);
  outline-offset: 3px;
}

/* === A11Y: skip-to-content link (visually hidden until focus) === */
.skip-link {
  position: absolute; top: -100px; left: 12px;
  z-index: 9999;
  background: var(--mc-blue);
  color: #fff;
  padding: 10px 14px;
  border-radius: 8px;
  font-family: var(--font-caption);
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  text-decoration: none;
  transition: top 160ms;
}
.skip-link:focus { top: 12px; }

/* === A11Y: active state ARIA hooks === */
.top-nav a[aria-current="true"] { color: var(--mc-blue-soft); background: rgba(22,158,227,0.10); }
.filter-chip[aria-pressed="true"] { /* visual handled via .is-active class */ }

/* === RESPONSIVE: mobile hamburger + section nav drawer === */
.nav-toggle {
  display: none;
  background: rgba(255,255,255,0.04);
  border: 1px solid var(--mc-line);
  color: var(--mc-text);
  width: 36px; height: 36px;
  border-radius: 8px;
  align-items: center; justify-content: center;
  cursor: pointer;
}
.nav-toggle:hover { border-color: var(--mc-line-strong); }
@media (max-width: 1080px) {
  .nav-toggle { display: inline-flex; }
  .top-nav.is-open {
    display: flex;
    position: absolute; top: 60px; left: 0; right: 0;
    flex-direction: column;
    background: rgba(5,11,26,0.97);
    backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px);
    border-bottom: 1px solid var(--mc-line);
    padding: 12px 20px;
    gap: 4px;
  }
  .top-nav.is-open a { padding: 12px 14px; font-size: 13px; }
}

/* === RESPONSIVE: mobile hero stats grid (5 stats no orphan row) === */
@media (max-width: 720px) {
  .hero-stats { grid-template-columns: repeat(2, 1fr) !important; }
}
@media (max-width: 480px) {
  .hero-stats { grid-template-columns: 1fr !important; }
}
"""

# Inject before </style>
marker = "</style>\n</head>"
if "focus-visible system" not in src and marker in src:
    src = src.replace(marker, focus_css + "\n" + marker, 1)
    changes.append("injected focus-visible + skip-link + mobile-nav CSS")

# === 5. Add nav-toggle button in topbar ===
# Insert before top-actions
nav_toggle_html = '''<button class="nav-toggle" type="button" id="navToggle" aria-label="Toggle navigation" aria-expanded="false" aria-controls="topNav">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
      </button>
      '''
if 'id="navToggle"' not in src:
    src = src.replace('<div class="top-actions">', nav_toggle_html + '<div class="top-actions">', 1)
    changes.append("added mobile nav-toggle button")

# Give nav an id for aria-controls
src = src.replace('<nav class="top-nav" aria-label="Sections">', '<nav class="top-nav" id="topNav" aria-label="Sections">', 1)

# === 6. Wire nav toggle JS + active link aria-current ===
nav_js = '''
  // === NAV TOGGLE (mobile) ===
  (function navToggle() {
    const btn = document.getElementById('navToggle');
    const nav = document.getElementById('topNav');
    if (!btn || !nav) return;
    btn.addEventListener('click', () => {
      const open = nav.classList.toggle('is-open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.addEventListener('click', e => {
      if (e.target.tagName === 'A') { nav.classList.remove('is-open'); btn.setAttribute('aria-expanded', 'false'); }
    });
  })();
  // === ACTIVE NAV aria-current (driven by IntersectionObserver) ===
  (function activeNav() {
    const links = document.querySelectorAll('.top-nav a[data-sec]');
    if (!links.length) return;
    const map = new Map();
    links.forEach(a => {
      const id = a.getAttribute('href').slice(1);
      const sec = document.getElementById(id);
      if (sec) map.set(sec, a);
    });
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        const a = map.get(e.target);
        if (!a) return;
        if (e.isIntersecting) {
          links.forEach(l => { l.removeAttribute('aria-current'); l.classList.remove('is-active'); });
          a.setAttribute('aria-current', 'true');
          a.classList.add('is-active');
        }
      });
    }, { rootMargin: '-50% 0px -50% 0px' });
    map.forEach((_a, sec) => io.observe(sec));
  })();
'''

# Inject near end of <script>, just before </script>
# Find the last </script>
last_script_close = src.rfind('</script>')
if last_script_close != -1 and 'navToggle()' not in src:
    src = src[:last_script_close] + nav_js + '\n' + src[last_script_close:]
    changes.append("added nav-toggle + active-nav JS")

# === 7. Filter chip aria-pressed (find filter chip render and add aria-pressed) ===
# Pattern: <button class="filter-chip${i===0?' is-active':''}" data-filter="${f}" type="button">
src_old = src
src = src.replace(
    '`<button class="filter-chip${i===0?\' is-active\':\'\'}" data-filter="${f}" type="button">${f}<span class="filter-count">${count}</span></button>`',
    '`<button class="filter-chip${i===0?\' is-active\':\'\'}" data-filter="${f}" type="button" aria-pressed="${i===0?\'true\':\'false\'}">${f}<span class="filter-count">${count}</span></button>`'
)
if src != src_old:
    changes.append("added aria-pressed to filter chips")

# Also update the click handler to flip aria-pressed
src_old = src
src = re.sub(
    r"filtersEl\.addEventListener\('click', e => \{ const b=e\.target\.closest\('\.filter-chip'\); if\(!b\) return; \$\$\('\.filter-chip',filtersEl\)\.forEach\(x=>x\.classList\.remove\('is-active'\)\); b\.classList\.add\('is-active'\); af=b\.dataset\.filter; apply\(\); \}\);",
    "filtersEl.addEventListener('click', e => { const b=e.target.closest('.filter-chip'); if(!b) return; $$('.filter-chip',filtersEl).forEach(x=>{x.classList.remove('is-active');x.setAttribute('aria-pressed','false');}); b.classList.add('is-active'); b.setAttribute('aria-pressed','true'); af=b.dataset.filter; apply(); });",
    src
)
if src != src_old:
    changes.append("filter-chip click handler updated for aria-pressed")

# === 8. Project card affordance: keep cursor:pointer but wire a click handler ===
# Currently .proj-item has cursor:pointer but no handler. Wire an expand-detail or scroll-into-view behavior.
# Look at how projects render to add a click that toggles a detail row.
# For now: add tabindex/role and a no-op-but-tracked click that scrolls to anchor.
# Actually less risky: just remove the pointer cursor since we don't have a target action.
src_old = src
src = src.replace(
    ".proj-item { display: grid; grid-template-columns: 12px 1fr auto 16px; gap: 12px; align-items: center; padding: 12px 0; border-top: 1px solid var(--border-1); cursor: pointer; transition: background 120ms; }",
    ".proj-item { display: grid; grid-template-columns: 12px 1fr auto 16px; gap: 12px; align-items: center; padding: 12px 0; border-top: 1px solid var(--border-1); transition: background 120ms; }"
)
if src != src_old:
    changes.append("removed false-affordance cursor:pointer from .proj-item")

# === 9. cmdkInput accessible name ===
src_old = src
src = re.sub(
    r'<input([^>]*?)id="cmdkInput"([^>]*?)>',
    lambda m: '<input' + m.group(1) + 'id="cmdkInput" aria-label="Search across sections, integrations, crons, and projects"' + m.group(2) + '>',
    src
)
# Avoid double-adding if already there
if 'aria-label="Search across sections' in src:
    if src != src_old:
        changes.append("added aria-label to #cmdkInput")

# Write
HTML.write_text(src, encoding="utf-8")
print("== Batch B changes ==")
for c in changes:
    print(f"  - {c}")
