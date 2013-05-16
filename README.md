# Spotify Playlist Exporter

Exports Spotify playlists from URL or URI to `stdout` or CSV.

## Usage

```
usage: export-spotify-playlist.py [-h] [--csv] playlist [playlist ...]

Exports a Spotify playlist to stdout or csv.

positional arguments:
  playlist    a Spotify playlist URL or URI

optional arguments:
  -h, --help  show this help message and exit
  --csv, -c   exports playlist to a CSV file
```

## Example

```
./export-spotify-playlist.py http://open.spotify.com/user/vietjtnguyen/playlist/58BEX3K4yuhqlkF1lAn0r5 spotify:user:vietjtnguyen:playlist:61ajjIvbt8FvbseV8PHWdm
```

## Dependencies

The script was developed using Python 2.7.3.

### Mechanize

[[http://wwwsearch.sourceforge.net/mechanize/]]

Easily installed with `easy_install mechanize` (`sudo easy_install mechanize` if necessary). Looks like you can also use `pip`: `pip install mechanize`.

The script could be written to rely on `urllib2` and `re` only, but `mechanize` made it easier to develop.

## Funny Things

For some reason some of the track URLs that Spotify lists for some tracks and some playlists are broken and lead to a 404.

