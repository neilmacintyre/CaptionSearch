import youtube_dl
import std_out_array
import LANG_CODES
import re


class Playlist:
    video_ids = []

    def __init__(self, url):
        self.url = url
        self.video_ids = self.get_ids()

    def get_ids(self):
        output = std_out_array.std_out_array(self.url, {'simulate': True,})
        id_regex = re.compile("\[youtube\]\s(.*):\sDownloading\swebpage")

        return [id_regex.search(line).groups(0)[0] for line in output if id_regex.search(line) is not None]

    def download_subs(self, lang_code, dest):
        """

        :param lang_code: language to download subtitles in
        :param dest: String path to directory to download files to
        :return: None
        """
        for video_id in self.video_ids:
            # check if langage

            ydl_opts = {'skip_download': True,
                        'writesubtitles': True,
                        'subtitleslangs': [lang_code],
                        'outtmpl': dest + '/TITLE:%(title)s__ID:%(id)s.%(ext)s'
                        }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(['https://www.youtube.com/watch?v=%s' % video_id])


# test
if __name__ == "__main__":
    url = "https://www.youtube.com/playlist?list=PLOGi5-fAu8bGxv7pdPIoc5x8s3N0gSsc0"
    t = Playlist(url)
    t.download_subs(LANG_CODES.EN, '../../data')
