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
        pass


# test
if __name__ == "__main__":
    url = "https://www.youtube.com/playlist?list=PLOGi5-fAu8bFs6LFkvbpoF9u4J-7wNbQH"
    t = Playlist(url)
