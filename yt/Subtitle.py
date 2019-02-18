import os.path as path
import re


class Subtitle:
    """
    Subtitle Class provides methods for parsing subtitles from
    various subtitle formats into python readable objects
    -- at the moment only vtt file format is supported
    """

    lang = ""
    # each caption segment is represented by a tuple with the signature
    # (int time_start, int time_end, string subtitle)
    captions = []
    video_uid = ""
    video_title = ""

    def __init__(self, file_path, uid, title = ""):
        """

        :param file_path: path to the vtt file to read text from
        :return: Subtitle object
        """

        if path.exists(file_path):
            with open(file_path, 'r') as subtitle_file:
                info = self.parse_vtt(subtitle_file)

                self.lang = info[0]
                self.captions = info[1]
                self.video_uid = uid
                self.video_title = title
        else:
            # TODO implement with proper syntax/pattern
            raise FileNotFoundError("File does not exist:: ", file_path)

    def parse_vtt(self, file):
        """

        :param file: python file object reprsentation of vtt file
        :return: tuple with signature (String language, Tuple array captions and times)
        """
        lang_line = re.compile("Language:\s(.{2,3})")
        time_line = re.compile("(\d{2}:\d{2}:\d{2}.\d{3})\s-->\s(\d{2}:\d{2}:\d{2}.\d{3})\n")
        caption_line = re.compile("([^\n].*)\n")

        captions_started = False

        lang =""
        start_times = []
        end_times = []
        words = []

        for line in file:

            if time_line.match(line):
                start_times.append(self.parse_time(time_line.search(line).group(1)))
                end_times.append(self.parse_time(time_line.search(line).group(2)))

            elif lang_line.match(line):
                captions_started = True
                lang = lang_line.search(line).groups(0)[0]

            elif caption_line.match(line) and captions_started:
                if len(start_times) > len(words): # a new segment of captions has started
                    words.append(caption_line.match(line).groups(0)[0])
                else:
                    words[len(words)-1] += " " + (caption_line.match(line).groups(0)[0])

        return lang, list(zip(start_times, end_times, words))

    def words_by_time(self):
        """

        :return: an array where each index is a tuple of the following singature
                 (start_time of segment that word is spoken in, string instance of word)
        """

        words_by_segment = [[(segment[0], self.format_word(word)) for word in segment[2].split(" ")] for segment in self.captions]

        words = [word for words in words_by_segment for word in words]

        return words

    def format_word(self, str_word):
        special_chars  =  re.compile("[.,!?]")
        return ''.join([ x for x in str_word if not special_chars.match(x)]).lower()

    def parse_time(self, time_string):
        """

        :return: time in seconds
        """
        time_regex = re.compile("(\d{2}):(\d{2}):(\d{2}).(\d{3})")

        search_result = time_regex.search(time_string)
        hours         = int(search_result.groups(1)[0])
        minutes       = int(search_result.groups(1)[1])
        seconds       = int(search_result.groups(1)[2])
        milliseconds  = int(search_result.groups(1)[3])

        time_in_seconds = 3600*hours + 60*minutes + seconds + (10**-3)*milliseconds

        return time_in_seconds


# test
# path IS wrong!!!!
if (__name__ == '__main__'):
    sub1 = Subtitle("../../data/Quantum computing explained in 10 minutes _ Shohini Ghose-QuR969uMICM.en.vtt", "QuR969uMICM")
    r = sub1.words_by_time()
    t=0