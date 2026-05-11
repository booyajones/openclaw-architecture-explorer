"""
Batch A fixes for openclaw-architecture-explorer.
- Counter sync: 19 -> 25 (integrations) / 23 (crons), 38 -> 42 (projects)
- Em dash removal
- Ticker fix
- Command palette count fix
- Missing-font CSS cleanup
"""
import re
from pathlib import Path

REPO = Path(r"C:\Users\chris\Downloads\openclaw-architecture-explorer")
HTML = REPO / "index.html"
CSS = REPO / "css" / "finexio-tokens.css"

src = HTML.read_text(encoding="utf-8")
css = CSS.read_text(encoding="utf-8")

changes = []

def replace_once(text, old, new, label):
    if old not in text:
        print(f"  SKIP (not found): {label}")
        return text, False
    new_text = text.replace(old, new, 1)
    changes.append(label)
    return new_text, True

def replace_all(text, old, new, label):
    if old not in text:
        print(f"  SKIP (not found): {label}")
        return text, False
    count = text.count(old)
    new_text = text.replace(old, new)
    changes.append(f"{label} (x{count})")
    return new_text, True

# === Counter sync ===
print("== Counter sync ==")

# Hero subhead: "19 nightly crons" -> "23 nightly crons"
src, _ = replace_once(src, "and 19 nightly crons", "and 23 nightly crons", "hero subhead 19->23 nightly crons")

# Hero projects counter: data-target="38" -> "42"
src, _ = replace_once(src, 'class="stat-num counter" data-target="38"', 'class="stat-num counter" data-target="42"', "hero projects counter 38->42")

# Integrations section heading: "19 systems on the wire" -> "25 systems on the wire"
src, _ = replace_once(src, "19 systems on the wire", "25 systems on the wire", "integ section heading 19->25")

# Integrations search placeholder
src, _ = replace_once(src, 'placeholder="Search 19 integrations', 'placeholder="Search 25 integrations', "integ search placeholder 19->25")

# Projects section heading: "38 projects, 9 categories" -> "42 projects, 9 categories"
src, _ = replace_once(src, "38 projects, 9 categories", "42 projects, 9 categories", "projects section heading 38->42")

# Ticker "CRONS GREEN 19/19" -> "23/23"
src, _ = replace_once(src, "['CRONS GREEN', '19/19', 'flat']", "['CRONS GREEN', '23/23', 'flat']", "ticker CRONS GREEN 19/19->23/23")

# Command palette section items
src, _ = replace_once(src, "id: 'cron', label: '19 Crons'", "id: 'cron', label: '23 Crons'", "cmdk 19 Crons->23")
src, _ = replace_once(src, "label: 'Integrations', sub: '02 · the network', href: '#integrations', meta: '19'", "label: 'Integrations', sub: '02 · the network', href: '#integrations', meta: '25'", "cmdk Integrations meta 19->25")
src, _ = replace_once(src, "label: 'Crons', sub: '03 · automation', href: '#crons', meta: '19'", "label: 'Crons', sub: '03 · automation', href: '#crons', meta: '23'", "cmdk Crons meta 19->23")
src, _ = replace_once(src, "label: 'Projects', sub: '05 · work', href: '#projects', meta: '38'", "label: 'Projects', sub: '05 · work', href: '#projects', meta: '42'", "cmdk Projects meta 38->42")

# === Em dash removal ===
# Most em dashes serve as appositive separators. Replace with comma, period, or colon contextually.
# Safe global: em dash with spaces around it (most common) -> comma
em_count_before = src.count("—")
print(f"\n== Em dash removal ==")
print(f"  Em dashes before: {em_count_before}")

# Specific high-value replacements
specifics = [
    # Hero lede: "Chris Wyatt's personal AI assistant — callsign Booya Jones, deployed as Wyattbot on top of OpenClaw."
    (" — callsign ", ", callsign "),
    # "A single Node.js process on EC2, fanning Slack messages out across LLMs, CRMs, data warehouses, and 19 nightly crons. All live, all in conversation."
    # (no em dash there)
    # "the last mile is where AP breaks, so we own it"
    # Generic patterns
    (" — ", ", "),   # spaced em dash -> comma
    (" —", ","),       # em dash with leading space, no trailing -> comma
    ("— ", ", "),      # em dash with trailing space, no leading -> comma
    ("—", ","),         # bare em dash -> comma (final pass)
]
for old, new in specifics:
    if old in src:
        c = src.count(old)
        src = src.replace(old, new)
        changes.append(f"em dash variant '{repr(old)}' -> '{repr(new)}' (x{c})")

em_count_after = src.count("—")
print(f"  Em dashes after:  {em_count_after}")

# === Missing-font CSS cleanup ===
# Remove @font-face rules pointing to files that don't exist in /fonts/
fonts_dir = REPO / "fonts"
present = {p.name for p in fonts_dir.iterdir()}
print(f"\n== Font cleanup ==")
print(f"  Present font files: {len(present)}")

new_css_lines = []
removed = 0
for line in css.splitlines():
    m = re.search(r"url\('\.\./fonts/([^']+)'\)", line)
    if m and m.group(1) not in present:
        # @font-face rule referencing missing file: drop the entire @font-face line
        removed += 1
        continue
    new_css_lines.append(line)
new_css = "\n".join(new_css_lines)
if removed > 0:
    changes.append(f"removed {removed} @font-face rules pointing to missing files")
    print(f"  Removed {removed} @font-face rules")

# === Write ===
HTML.write_text(src, encoding="utf-8")
CSS.write_text(new_css, encoding="utf-8")

print("\n== Changes applied ==")
for c in changes:
    print(f"  - {c}")
