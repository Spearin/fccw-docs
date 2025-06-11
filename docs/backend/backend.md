# Site Features

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

!!! example
    This page will not be displayed to the public. Internal tracking use only!

## TO DO

- [ ] Configure Site Settings
    * [ ] Setup PDF export
    * [x] Setup theme switch
    * [x] Install Mil Symbols fonts --> Build [test page](symbols.html)
- [ ] Setup Navigation
    * [ ] Simplify Navigation
- [ ] Convert Content
    * [x] Introduction
    * [X] FAQ
    * [x] Setup Guide
    * [x] Credits
    * [x] FM01 Operations
    * [x] FM02 Primer
    * [x] FM03 Tutorials
    * [ ] FM04 Scenario Design
    * [ ] FM05 Battle Planning
    * [ ] FM06 Campaign Design
    * [ ] FM07 Map Construction
    * [ ] FM08 Mods
    * [ ] FM09 Data Structures
    * [ ] FM10 Weather
- [ ] Modify and Create Content
    * [ ] Create Reference Section
    * [ ] Force Diagram Template
    * [ ] Equipment Reference Templates
- [x] Multiple themes
    * [ ] Default - based on the current manual design
    * [ ] Dark - inspired by retro computing
    * [ ] Determine multiple theme support

## Plugins & Extensions

- `enumerate-headings` - This will automatically add numbers to each section header
- `macros` - We can set and use variables `{{ test_macro }}` --> {{ test_macro }}
      - This also powers our military symbol font codes `:fr-infantry:` --> :fr-infantry:
- `live-edit` - Can edit the markdown pages in the browser! Will disable before going public. This is only used when serving the site on the local computer, cannot be used when hosted... unless I find a workaround.
- `mermaid2` - Make flowcharts and diagrams with Markdown
- `awesome-nav` - Reorganize the navigation
- `exporter` - Exports the docs into a PDF
- `abbr` Abbreviations have helpers (see below)

[Find more plugins here.](https://github.com/mkdocs/catalog)

### Testing Grounds

1. [This link to NATO](FCCW/FCCW.html#NATO) should take us to the [Cold War](FCCW/FCCW.html#NATO) page. _Keyword: *Should*_
2. We can show an enemy tank icon with `:en-tank:`, and a friendly infantry icon with `:fr-infantry:`
:en-tank: :fr-infantry:
