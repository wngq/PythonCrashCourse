def make_album(artist, album_name, tracks=''):
    albums = {
        'artist': artist.title(),
        'album': album_name.title(),
    }
    if tracks:
        albums['tracks'] = tracks
    return albums


while True:
    print("\nPlease tell me an album.")
    print("(enter 'q' at any time to quit)")

    artist = input("Artist: ")
    if artist == 'q':
        break

    album_name = input("Album name: ")
    if album_name == 'q':
        break

    print(make_album(artist, album_name))
