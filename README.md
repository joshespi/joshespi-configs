# Josh Espi system configs

## Untrap for YouTube

Settings for [Untrap](https://untrap.app/), a YouTube distraction blocker.

To restore: open Untrap settings and use the import string in `untrapForYoutubeSettings.txt`.

## Bookmarks

Browser bookmarks managed via TOML. Edit `bookmarks/bookmarks.toml`, then run:

```bash
cd bookmarks && python3 bookmarks_build.py
```

Requires Python 3.11+. Import the generated `bookmarks_import.html` into any browser via its bookmarks settings.
