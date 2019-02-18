import youtube_dl

def get_playlist_urls(url):
    """

    :param url: playlist url
    :return: array of indivdual video urls from playlist
    """
    with youtube_dl.YoutubeDL({'simulate': True}) as ydl:
        ydl.download(url)

# use a logger.logging object similar to the check subs

# Test
get_playlist_urls(['https://www.youtube.com/playlist?list=PL0IS0YyQ-bEm-mRdP6SzUy85BqIb27v8a'])