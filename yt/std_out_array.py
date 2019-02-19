import youtube_dl


def std_out_array(url, options={}):
    """
    Takes a youtube-dl command and returns the output as an array
    :param url: String url to video or playlist to download
    :param options: object download preferences
    :return: array of the std_out strings
    """

    ydl_opts = options

    # override logger -- needed to get expected output
    options['logger'] = StdOutLogger()

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return options['logger'].log


class StdOutLogger:
    def __init__(self):
        self.log = []

    def debug(self, message):
        # print(message)
        self.log.append(message)

    @staticmethod
    def warning(msg):
        print(msg)

    @staticmethod
    def error(msg):
        print(msg)


# test
if __name__ == "__main__":
    ydl_opt = {'simulate': True,}
    array = std_out_array("https://www.youtube.com/playlist?list=PLOGi5-fAu8bFs6LFkvbpoF9u4J-7wNbQH", ydl_opt)
    print(array)
