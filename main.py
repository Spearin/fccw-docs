# main.py
import re

"""
SYMBOL_MAP: each key is the shortcode (e.g. "en-tank"), and its value is a tuple:
   (css_class, unicode_string)

When we see :en-tank: outside of backticks, we replace it with
   <span class="css_class">unicode_string</span>
"""

SYMBOL_MAP = {
    # Example entries; fill in the rest
    "en-tank":      ("sym-en-land",    "A"),
    "fr-armored":           ("sym-fr-land", "A"),
    "fr-cavalry":           ("sym-fr-land", "C"),
    "fr-artillery":         ("sym-fr-land", "F"),
    "fr-engineer":          ("sym-fr-land", "G"),
    "fr-aviation":          ("sym-fr-land", "H"),
    "fr-infantry":          ("sym-fr-land", "I"),
    "fr-armor-recon":       ("sym-fr-land", "J"),
    "fr-mechanized":        ("sym-fr-land", "K"),
    "fr-tank-destroyer":    ("sym-fr-land", "L"),
    "fr-antiarmor":         ("sym-fr-land", "M"),
    "fr-air-defense":       ("sym-fr-land", "N"),
    "fr-headquarters":      ("sym-fr-land", "O"),
    "fr-signal":            ("sym-fr-land", "Q"),
    "fr-chemical":          ("sym-fr-land", "R"),
    "fr-reconnaissance":    ("sym-fr-land", "S"),
    "fr-transport":         ("sym-fr-land", "T"),
    "fr-medical":           ("sym-fr-land", "U"),
    "fr-maintenance":       ("sym-fr-land", "V"),
    "fr-supply":            ("sym-fr-land", "W"),
    "fr-engine":            ("sym-fr-land", "X"),
    "fr-commando":          ("sym-fr-land", "Y"),
    "fr-militia":           ("sym-fr-land", "Z")
}

# Pattern to find :tag-name: (lowercase letters, digits, hyphens)
_shortcut_pattern = re.compile(r":([a-z0-9\-]+):")

# Pattern to split on inline code spans: (`[^`]*`)
_code_span_pattern = re.compile(r"(`[^`]*`)")

def _replace_shortcodes(text):
    """
    Replace all instances of :tag: in `text` with <span class="css">glyph</span>,
    based on SYMBOL_MAP. If tag not found, leave it alone.
    """
    def _sub(match):
        tag = match.group(1)  # e.g. "en-tank"
        entry = SYMBOL_MAP.get(tag)
        if entry:
            css_class, glyph = entry
            return f'<span class="{css_class}">{glyph}</span>'
        return match.group(0)  # no change if tag not in SYMBOL_MAP

    return _shortcut_pattern.sub(_sub, text)


def on_post_page_macros(env):
    """
    MkDocs-Macros hook (v1.x) called AFTER macros expand but BEFORE Markdown → HTML.
    env.markdown is the *raw* Markdown of the page (including any backticks, etc.).

    Steps:
      1. Split env.markdown on inline code spans (`…`), so that code spans
         are preserved literally.
      2. For each non-code segment, run _replace_shortcodes().
      3. Re-join all segments into one string, assign back to env.markdown.
    """
    # Split on every inline code span. The resulting list alternates:
    # [text_before_code, "`code...`", text_after, "`other code`", ...]
    segments = _code_span_pattern.split(env.markdown)

    # Process only the “even‐indexed” segments (0, 2, 4, …), i.e. the plain text.
    for i in range(0, len(segments), 2):
        segments[i] = _replace_shortcodes(segments[i])

    # Re-join everything. Code spans (odd indices) remain untouched.
    env.markdown = "".join(segments)

# Macro for image paths in MkDocs offline/online versions
def define_env(env):
    """
    Called by mkdocs-macros-plugin.
    Exposes a single macro `img(name)` that returns:
      <configured image_dir>/<name>
    """
    image_dir = env.config.extra.get('image_dir', '').rstrip('/')

    @env.macro
    def img(filename):
        # strip any accidental leading slash on filename
        return f"{image_dir}/{filename.lstrip('/')}"