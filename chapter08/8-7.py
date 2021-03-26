def make_album(artist, album_name, tracks=''):
    albums = {
        'artist': artist.title(),
        'album': album_name.title(),
    }
    if tracks:
        albums['tracks'] = tracks
    return albums


album_1 = make_album('taylor swift', 'red')
album_2 = make_album('ed sheeran', 'x')
album_3 = make_album('coldplay', 'parachutes', 11)
album_4 = make_album('coldplay', 'parachutes', '12')

print(album_1)
print(album_2)
print(album_3)
print(album_4)
