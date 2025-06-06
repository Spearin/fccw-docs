# Time to RTFM!

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## TODO

1. Configure Site Settings

    * Setup PDF export
    * Setup theme switch
    * Configure Navigation
    * Install Mil Symbols fonts --> Build test page

2. Convert Content
3. Modify and Create Content

## Plugins

* `enumerate-headings` - This will automatically add numbers to each section header
* `macros` - We can set and use variables {{ test_macro }}
* `live-edit` - Can edit the markdown pages in the browser! Will disable before going public.
* `mermaid2` - Make flowcharts and diagrams with Markdown
* `awesome-nav` - Reorganize the navigation

### Testing

1. [This link to NATO](#NATO) should take us to the [Cold War](FCCW/FCCW.html) page. _Keyword: *Should*_
2. We can show an enemy tank icon with `:en-tank:`, and a friendly infantry icon with `:fr-infantry:`
:en-tank: :fr-infantry:

## Macro Plugin Info

{{ macros_info() }}