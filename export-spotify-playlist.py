#!/usr/bin/python

import argparse
import csv
import collections
import re
import sys
import urllib2

# http://stackoverflow.com/questions/2087370/decode-html-entities-in-python-string
import HTMLParser
html_parser = HTMLParser.HTMLParser()

# http://wwwsearch.sourceforge.net/mechanize/
import mechanize

# http://docs.python.org/2.7/library/argparse.html
parser = argparse.ArgumentParser(description='Exports a Spotify playlist to stdout or csv.')
parser.add_argument('playlist', nargs='+', help='a Spotify playlist URL or URI')
parser.add_argument('--csv', '-c', dest='export_csv', action='store_true', help='exports playlist to a CSV file')
arguments = parser.parse_args()

for playlist in arguments.playlist:

	if playlist.startswith('http'):
		playlist_url = playlist
	else:
		playlist_url = 'http://open.spotify.com/user/{}/playlist/{}'.format(*re.search('spotify:user:(.+):playlist:(.+)', playlist).groups())

	print('')
	print(playlist_url)

	playlist_br = mechanize.Browser()
	playlist_br.open(playlist_url)

	playlist_name = re.search(r'<h1 itemprop="name">(.+)</h1>', playlist_br.response().read()).groups()[0]
	print(playlist_name)
	print('')

	# http://docs.python.org/2/library/functions.html#filter
	track_links = filter(lambda x: x.url.startswith('/track/'), playlist_br.links())

	# http://docs.python.org/2/library/collections.html#ordereddict-objects
	tracks = collections.OrderedDict()
	for track_link in track_links:
		if not tracks.has_key(track_link.url):
			tracks[track_link.url] = {'mechanized_link': track_link, 'track_url': 'http://open.spotify.com' + track_link.url, 'title': track_link.text}

	for track in tracks.values():
		try:
			track_html = mechanize.urlopen(track['track_url']).read()
		except urllib2.HTTPError as e:
			print('{:}, HTTP Error 404, {:} not found'.format(track['title'], track['track_url']))
			track['artist_url'], track['artist'], track['album_url'], track['album'] = ('', '', '', '')
			continue

		# http://docs.python.org/2/library/re.html
		matches = re.search(r'<h1 itemprop="name">(.+)</h1>[ \t\n\r]*<h2> by <a href="(/artist/.+)">(.+)</a></h2>[ \t\n\r]*</div>[ \t\n\r]*<h3>Tracks in <a href="(/album/.+)">(.+)</a></h3>', track_html)
		track['title'], track['artist_url'], track['artist'], track['album_url'], track['album'] = matches.groups()
		track['artist_url'] = 'http://open.spotify.com' + track['artist_url']
		track['album_url'] = 'http://open.spotify.com' + track['album_url']
		track['title'], track['artist'], track['album'] = map(html_parser.unescape, (track['title'], track['artist'], track['album']))
		print('{artist} - {album} - {title}'.format(**track))

	if arguments.export_csv:
		# http://docs.python.org/2/library/csv.html
		csv_file_name = '{}.csv'.format(playlist_name)
		with open(csv_file_name, 'wb') as csv_file:
			csv_writer = csv.writer(csv_file)
			csv_writer.writerow(['Artist', 'Album', 'Title', 'Artist URL', 'Album URL', 'Track URL'])
			for track in tracks.values():
				csv_writer.writerow([track[key] for key in ['artist', 'album', 'title', 'artist_url', 'album_url', 'track_url']])
		print('')
		print('Playlist written to "{:}"'.format(csv_file_name))

