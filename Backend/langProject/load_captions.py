"""
Methods for loading captions into sql database
"""
import re
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'langProject.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from captions.models import Caption, Word
from yt import Subtitle

# TODO figure out why the syntaxt highlighing is throwing errors and warning for this file
def load_captions(file_path, uid):
    """
    loads captions from a file
    :param file_path: path to subtitle file
    :param uid:
    :return: None
    """
    subtitle = Subtitle.Subtitle(file_path, uid)

    for caption_segment in subtitle.captions:
        start_time = caption_segment[0]
        end_time = caption_segment[1]
        caption = caption_segment[2]
        caption_row = Caption(video_id=uid, start_time=start_time, end_time=end_time, caption=caption)

        caption_row.save()

    for word in subtitle.words_by_time():
        print("Word add:: " + word[1])
        segment_start_time = word[0]
        word = word[1]
        word_row = Word(video_id=uid, segment_start_time=segment_start_time, word=word)

        word_row.save()

def bulk_load(dir_path):
    """
    load all vtt files in directory
    (files should have name format:: '/TITLE:%(title)s__ID:%(id)s.%(ext)s')

    :param dir_path: path to directory containing subtitle files
    :return: None
    """

    # get all the paths to files in the folder that match pattern -- and store in array
    # use the same pattern pull ids from the file name
    accept_path = re.compile("TITLE:(.*)__ID:(.*)\..{2}\.vtt")
    paths = os.listdir(dir_path)

    subtitle_paths = []
    video_titles = []
    uids = []
    for path in paths:
        state = accept_path.search(path)
        if state is not None:
            subtitle_paths.append(path)
            video_titles.append(state.groups(0)[0])
            uids.append(state.groups(0)[1])

    # loop through the arrays and run load caption for each file_path uid pair
    for i in range(0, len(subtitle_paths) - 1):
        print("Loading Video::" + video_titles[i])
        load_captions(dir_path+subtitle_paths[i], uids[i])



# test
if __name__ == "__main__":
    #load_captions("../../../data/Quantum computing explained in 10 minutes _ Shohini Ghose-QuR969uMICM.en.vtt", "QuR969uMICM")
    bulk_load('../../../data/')
