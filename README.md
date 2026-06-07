# Josh Espi system configs

## Untrap for YouTube

Settings for [Untrap](https://untrap.app/), a YouTube distraction blocker.

To restore: open Untrap settings and use the import string in `untrapForYoutubeSettings.txt`.

## Bookmarks

Browser bookmarks managed via TOML. Edit `bookmarks/bookmarks.toml`, 
then run:

### if Python is installed

```bash
cd bookmarks && python3 bookmarks_build.py
```

Requires Python 3.11+. Import the generated `bookmarks_import.html` into any browser via its bookmarks settings.

### if Docker is installed

```powershell
docker run --rm -v "c:\Users\joshe\Documents\joshespi-configs\bookmarks:/work" -w /work python:3.11-alpine python3 bookmarks_build.py
```
