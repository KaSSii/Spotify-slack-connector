import sys
import spotipy
import json
import spotipy.util as util
import time

spotify_files = open('./info.json', 'r')
spotify_json = spotify_files.read()
spotify_info = json.loads(spotify_json)

print('Getting Auth Token...')
token = util.prompt_for_user_token(
    spotify_info['username'],
    'user-read-currently-playing',
    client_id=spotify_info['client_id'],
    client_secret=spotify_info['secret_id'],
    redirect_uri=spotify_info['redirect_uri']
)

if token:
    print('Activating...')

    sp = spotipy.Spotify(auth=token)

    print('Fetching song...')
    previousSong = '' # How I will handle updating slack name
    while True:
        results = sp._get('me/player/currently-playing', sp._auth_headers())
        currentSong = 'Listening to - ' + results['item']['name'] + ' by ' + results['item']['artists'][0]['name']
        if previousSong != currentSong:
            previousSong = currentSong
            print(currentSong)
        time.sleep(5)

else:
    print ("Can't get token for", username)