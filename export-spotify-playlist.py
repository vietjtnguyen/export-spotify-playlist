# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import csv
import collections
import re

# http://stackoverflow.com/questions/2087370/decode-html-entities-in-python-string
import HTMLParser
html_parser = HTMLParser.HTMLParser()

# http://wwwsearch.sourceforge.net/mechanize/
import mechanize

# <codecell>

arg1 = 'http://open.spotify.com/user/vietjtnguyen/playlist/58BEX3K4yuhqlkF1lAn0r5'
arg1 = 'spotify:user:vietjtnguyen:playlist:58BEX3K4yuhqlkF1lAn0r5'

if arg1.startswith('http'):
    playlist_url = arg1
else:
    playlist_url = 'http://open.spotify.com/user/{}/playlist/{}'.format(*re.search('spotify:user:(.+):playlist:(.+)', arg1).groups())

print(playlist_url)

# <codecell>

playlist_br = mechanize.Browser()
playlist_br.open(playlist_url)

# <codecell>

# http://docs.python.org/2/library/functions.html#filter
track_links = filter(lambda x: x.url.startswith('/track/'), playlist_br.links())

# <codecell>

# http://docs.python.org/2/library/collections.html#ordereddict-objects
tracks = collections.OrderedDict()
for track_link in track_links:
    tracks[track_link.url] = {'mechanized_link': track_link, 'track_url': 'http://open.spotify.com' + track_link.url}

# <codecell>

for track in tracks.values():
    track_html = mechanize.urlopen(track['track_url']).read()
    # http://docs.python.org/2/library/re.html
    matches = re.search(r'<h1 itemprop="name">(.+)</h1>[ \t\n\r]*<h2> by <a href="(/artist/.+)">(.+)</a></h2>[ \t\n\r]*</div>[ \t\n\r]*<h3>Tracks in <a href="(/album/.+)">(.+)</a></h3>', track_html)
    track['title'], track['artist_url'], track['artist'], track['album_url'], track['album'] = matches.groups()
    track['artist_url'] = 'http://open.spotify.com' + track['artist_url']
    track['album_url'] = 'http://open.spotify.com' + track['album_url']
    track['title'], track['artist'], track['album'] = map(html_parser.unescape, (track['title'], track['artist'], track['album']))
    print(track)

# <codecell>

# http://docs.python.org/2/library/csv.html
with open('out.csv', 'wb') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Artist', 'Album', 'Title', 'Artist URL', 'Album URL', 'Track URL'])
    for track in tracks.values():
        csv_writer.writerow([track[key] for key in ['artist', 'album', 'title', 'artist_url', 'album_url', 'track_url']])

# <codecell>


