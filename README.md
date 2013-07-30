# Spotify Playlist Exporter

Exports Spotify playlists from URL or URI to `stdout` or CSV.

Note that this public web interface is limited to 30 songs (see [Issue #1](https://github.com/vietjtnguyen/export-spotify-playlist/issues/1)).

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

## Dependencies

The script was developed using Python 2.7.3.

### Mechanize

http://wwwsearch.sourceforge.net/mechanize/

Easily installed with `pip install mechanize` or `easy_install mechanize`. `sudo` if you must.

The script could be written to rely on `urllib2` and `re` only, but `mechanize` made it easier to develop.

## Funny Things

For some reason some of the track URLs that Spotify lists for some tracks and some playlists are broken and lead to a 404.

## Example

```
> ./export-spotify-playlist.py http://open.spotify.com/user/vietjtnguyen/playlist/58BEX3K4yuhqlkF1lAn0r5 spotify:user:vietjtnguyen:playlist:61ajjIvbt8FvbseV8PHWdm

http://open.spotify.com/user/vietjtnguyen/playlist/58BEX3K4yuhqlkF1lAn0r5
Flavor of the Day

Thao with The Get Down Stay Down - Know Better Learn Faster - Body
Thao with The Get Down Stay Down - We Brave Bee Stings and All - Beat (Health, Life, and Fire)
Thao with The Get Down Stay Down - Know Better Learn Faster - Cool Yourself
Keane - Under The Iron Sea (Ecopac) - Nothing In My Way
Keane - Under The Iron Sea (Ecopac) - A Bad Dream
Caroline Smith & The Good Night Sleeps - Live At The Cedar - Tying My Shoes
Caroline Smith & The Good Night Sleeps - Backyard Tent Set - You Promised Me
Lenka - Lenka - The Show
Lenka - Lenka - Don't Let Me Fall
Lenka - Two - Two
Lenka - Two - Sad Song
Lenka - Two - Here To Stay
Lenka - Two - You Will Be Mine
Mr. Gnome - Heave Yer Skeleton - Sit Up & Hum
She & Him - Volume One - Black Hole
Bruno Mars - Unorthodox Jukebox - When I Was Your Man
Mr. Gnome - Madness In Miniature - We Sing Electric
Of Monsters And Men - My Head Is An Animal - Mountain Sound
Garbage - Not Your Kind Of People - Not Your Kind Of People
Woodkid - The Golden Age - The Great Escape
Woodkid - The Golden Age - I Love You
Dido - Life For Rent - White Flag
Metric - Synthetica - Artificial Nocturne
Metric - Synthetica - Youth Without Youth
Metric - Synthetica - Speed The Collapse
Metric - Synthetica - Breathing Underwater
Metric - Synthetica - Dreams So Real
Metric - Synthetica - Lost Kitten
Metric - Synthetica - The Void
Metric - Synthetica - Synthetica

http://open.spotify.com/user/vietjtnguyen/playlist/61ajjIvbt8FvbseV8PHWdm
Ambient All

The American Dollar - Ambient One - Starscapes - Ambient
The American Dollar - Ambient One - Bump - Ambient
The American Dollar - Ambient One - Lights Dim - Ambient
The American Dollar - Ambient One - Dea - Ambient
The American Dollar - Ambient One - We're Hitting Everything - Ambient
The American Dollar - Ambient One - Rudiments Of A Spiritual Life - Ambient
The American Dollar - Ambient One - Signaling Through The Flames
The American Dollar - Ambient One - The Slow Wait (Part 1) - Ambient
The American Dollar - Ambient One - The Slow Wait (Part 2) - Ambient
The American Dollar - Ambient One - Anything You Synthesize - Ambient
The American Dollar - Ambient One - Time - Ambient
The American Dollar - Ambient One - Transcendence - Ambient
The American Dollar - Ambient One - Signaling Through The Flames - Film Edit
The American Dollar - Ambient One - Time - Film Edit
The American Dollar - Ambient One - Intro
The American Dollar - Ambient One - Chase
The American Dollar - Ambient Two - A Few Words - Ambient
The American Dollar - Ambient Two - Age Of Wonder - Ambient
The American Dollar - Ambient Two - Fade In Out - Ambient
The American Dollar - Ambient Two - Shadows - Ambient
The American Dollar - Ambient Two - Oil And Water - Ambient
The American Dollar - Ambient Two - Circuits - Ambient
The American Dollar - Ambient Two - Red Letter - Ambient
The American Dollar - Ambient Two - Equinox - Ambient
The American Dollar - Ambient Two - Second Sight - Ambient
The American Dollar - Ambient Two - Flood - Ambient
The American Dollar - Ambient Two - Near East - Ambient
The American Dollar - Ambient Two - Landing - Ambient
The American Dollar - Ambient Two - Where We Are - Ambient
The American Dollar - Ambient Two - Par Avion
```

