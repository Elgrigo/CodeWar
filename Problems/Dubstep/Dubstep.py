def song_decoder(song):
    return ' '.join(song.replace('WUB'," ").split())
n = song_decoder("WUBAWUBBWUBC")
print(n)

        