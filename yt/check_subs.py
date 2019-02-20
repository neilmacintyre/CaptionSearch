import youtube_dl
import re

# TODO re-implement using std_out_array_method for reduced redundancy
# takes a youtube url, and a list of target languages
# return true if all
def check_subs(url, targets):
    """

    :param url:
    :param targets: target languages have subtitles
    :return:
    """

    logger = StdOutLog()
    subs_match = True  # do subs match all targets languages

    ydl_opts = {'listsubtitles': True,
                'quiet': True,
                'logger': logger}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)
        # find available languages
        for tar in targets:
            reg_x = re.compile('\n' + tar)
            subs_match = subs_match and \
                         reg_x.search(logger.subtitle_langs) is not None
    return subs_match


class StdOutLog:
    def __init__(self):
        self.subtitle_langs = []
        self.next_message = False # True if next message should be subtitle languages

    def debug(self, message):
        if re.compile('Available subtitles for*').match(message) is not None:
            self.next_message = True
        elif re.compile('Language formats*').match(message) is not None\
            and self.next_message:
            self.subtitle_langs = message

    def warning(self, msg):
        pass

    @staticmethod
    def error(self, msg):
        print(msg)


# Test
print(check_subs(['https://www.youtube.com/watch?v=n1pzVCWEXQM'], ['en', 'es']))

