# Site Features

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## TO DO

- [ ] Configure Site Settings
    * [ ] Setup PDF export
    * [x] Setup theme switch 
    * [x] Install Mil Symbols fonts --> Build [test page](symbols.html)
- [ ] Configure Navigation
- [ ] Convert Content
- [ ] Modify and Create Content
- [x] Multiple themes

## Plugins & Extensions

* `enumerate-headings` - This will automatically add numbers to each section header
* `macros` - We can set and use variables `{{ test_macro }}` --> {{ test_macro }}
    * This also powers our military symbol font codes `:fr-infantry:` --> :fr-infantry:
* `live-edit` - Can edit the markdown pages in the browser! Will disable before going public.
* `mermaid2` - Make flowcharts and diagrams with Markdown
* `awesome-nav` - Reorganize the navigation
* `exporter` - Exports the docs into a PDF
* `abbr` Abbreviations have helpers (see below)

Find more: https://github.com/mkdocs/catalog

### Testing Grounds

1. [This link to NATO](FCCW/FCCW.html#NATO) should take us to the [Cold War](FCCW/FCCW.html#NATO) page. _Keyword: *Should*_
2. We can show an enemy tank icon with `:en-tank:`, and a friendly infantry icon with `:fr-infantry:`
:en-tank: :fr-infantry:

