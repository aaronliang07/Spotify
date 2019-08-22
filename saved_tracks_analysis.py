pip install spotipy
pip install requests

import spotipy


# getting the dictionary of a user's saved songs and their musical qualities

import sys
import spotipy.util as util

scope = 'user-library-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope, client_id = '2d29c9a814ee4b7a92122ad3da33f6d8', client_secret = '3d2a4ec30ab847d495713942d4dd796f', redirect_uri = 'http://mysite.com/callback/')

songs = {}
count = 0

if token:
    sp = spotipy.Spotify(auth=token)
    while count <= 500:
        try:
            results = sp.current_user_saved_tracks(limit = 50, offset = count)
            for item in results['items']:
                track = item['track']
                print(track['name'] + ' - ' + track['artists'][0]['name'])
                songs[track['name']] = sp.audio_features(track['id'])
            if count == 0:
                count += 49
            else:
                count += 50
        except TypeError:
            break
else:
    print("Can't get token for", username)


# Fastest song in a user's library

max_bpm = 0
fastest_song = ''

for count, track in enumerate(songs):
    if songs[track][0]['tempo'] > max_bpm:
        max_bpm = songs[track][0]['tempo']
        fastest_song = track

print('The fastest song in your library is ' + fastest_song + ' with a tempo of ' + str(max_bpm) + ' bpm.')


# Slowest song in a user's library

min_bpm = 1000
slowest_song = ''

for count, track in enumerate(songs):
    if songs[track][0]['tempo'] < min_bpm:
        min_bpm = songs[track][0]['tempo']
        slowest_song = track

print('The slowest song in your library is ' + slowest_song + ' with a tempo of ' + str(min_bpm) + ' bpm.')


# Most danceable song in a user's library

danceable = ''
danceability = 0

for count, track in enumerate(songs):
    if songs[track][0]['danceability'] > danceability:
        danceability = songs[track][0]['danceability']
        danceable = track

print('The most danceable song in your library is ' + danceable + '.')


# Least danceable song in a user's library

danceable = ''
danceability = 1000

for count, track in enumerate(songs):
    if songs[track][0]['danceability'] < danceability:
        danceability = songs[track][0]['danceability']
        danceable = track

print('The least danceable song in your library is ' + danceable + '.')


# Most positive sounding song in a user's library

song = ''
positive = 0

for count, track in enumerate(songs):
    if songs[track][0]['valence'] > positive:
        positive = songs[track][0]['valence']
        song = track

print('The most positive sounding song in your library is ' + song + '.')


# Most negative sounding song in a user's library

song = ''
negative = 1000

for count, track in enumerate(songs):
    if songs[track][0]['valence'] < negative:
        negative = songs[track][0]['valence']
        song = track

print('The most negative sounding song in your library is ' + song + '.')


# Loudest song in a user's library

song = ''
volume = 1000

for count, track in enumerate(songs):
    if songs[track][0]['loudness'] < volume:
        volume = songs[track][0]['loudness']
        song = track

print('The loudest song in your library is ' + song + '.')


# Quietest song in a user's library

song = ''
volume = -1000

for count, track in enumerate(songs):
    if songs[track][0]['loudness'] > volume:
        volume = songs[track][0]['loudness']
        song = track

print('The quietest song in your library is ' + song + '.')


# Most energetic song in a user's library

song = ''
energy = 0

for count, track in enumerate(songs):
    if songs[track][0]['energy'] > energy:
        energy = songs[track][0]['energy']
        song = track

print('The most energetic song in your library is ' + song + '.')


# Least energetic song in a user's library

song = ''
energy = 1000

for count, track in enumerate(songs):
    if songs[track][0]['energy'] < energy:
        energy = songs[track][0]['energy']
        song = track

print('The least energetic song in your library is ' + song + '.')


# Average tempo of songs in a user's library

tempo = 0
scount = 0

for count, track in enumerate(songs):
    tempo += songs[track][0]['tempo']
    scount += 1

print('The average tempo of songs in your library is ' + str(tempo/scount) + '.')


# Most opposite pair of songs in a user's library

difference = 0
song1 = ''
song2 = ''

for count, track in enumerate(songs):
    for count2, track2 in enumerate(songs):
        temp_difference =  (abs((songs[track][0]['tempo'])/max_bpm - (songs[track2][0]['tempo'])/max_bpm) + abs(songs[track][0]['energy'] - songs[track2][0]['energy']) + abs(songs[track][0]['mode'] - songs[track2][0]['mode']) + abs(songs[track][0]['danceability'] - songs[track2][0]['danceability']) + abs(songs[track][0]['valence'] - songs[track2][0]['valence']))
        if temp_difference > difference:
            difference = temp_difference
            song1 = track
            song2 = track2

print('Your most opposite songs are ' + song1 + ' and ' + song2 + '.')
            
            
            
# Most similar pair of songs in a user's library

difference = 1000
song1 = ''
song2 = ''

for count, track in enumerate(songs):
    for count2, track2 in enumerate(songs):
        if track2 == track:
            continue
        temp_difference =  (abs((songs[track][0]['tempo'])/max_bpm - (songs[track2][0]['tempo'])/max_bpm) + abs(songs[track][0]['energy'] - songs[track2][0]['energy']) + abs(songs[track][0]['mode'] - songs[track2][0]['mode']) + abs(songs[track][0]['danceability'] - songs[track2][0]['danceability']) + abs(songs[track][0]['valence'] - songs[track2][0]['valence']))
        if temp_difference < difference:
            difference = temp_difference
            song1 = track
            song2 = track2

print('Your most similar songs are ' + song1 + ' and ' + song2 + '.')    

