"""
Methods for loading captions into sql database
"""
import re
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'langProject.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from captions.models import Word, Subtitle as SubModel, Video, CaptionSegment
from yt import Subtitle

# TODO figure out why the syntaxt highlighing is throwing errors and warning for this file
def load_captions(file_path, video_id, title):
    """
    loads captions from a file
    :param file_path: path to subtitle file
    :param video_id:
    :return: None
    """
    subtitle = Subtitle.Subtitle(file_path, video_id)

    # Check if the Video is already in the database
    if len(Video.objects.filter(video_id=video_id)) == 0:
        video_row = Video(video_id=video_id, title=title)
        video_row.save()

    # Check if the subtitle is already in the database
    if len(SubModel.objects.filter(video_id=video_id).filter(language=subtitle.lang)) == 0:
        subtitle_segment_row = SubModel(video_id_id=video_id, language=subtitle.lang)
        subtitle_segment_row.save()


    for caption_segment in subtitle.captions:
        start_time = caption_segment[0]
        end_time = caption_segment[1]
        caption = caption_segment[2]

        # Check if the caption_segment is already in the database
        if len(CaptionSegment.objects.filter(video_id__video_id=video_id).filter(start_time=start_time)) == 0:
            caption_row = CaptionSegment(video_id_id=video_id, start_time=start_time, end_time=end_time, caption=caption)
            caption_row.save()

    for word in subtitle.words_by_time():
        # TODO Check if the caption_segment is already in the database
        print("Word add:: " + word[1])
        segment_start_time = word[0]
        word = word[1]

        # find the caption segment containing word
        parent_segment = CaptionSegment.objects.filter(start_time=segment_start_time).filter(video_id_id=video_id)

        word_row = Word(video_id_id=video_id, caption_segment_id_id=parent_segment.values('id')[0]['id'], word=word)

        word_row.save()

# BULK LOAD IS VERY SLOW -- note it was slow even before existence checks where added
# TODO optmize this algoritm
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
        load_captions(dir_path+subtitle_paths[i], uids[i],video_titles[i])



# test
if __name__ == "__main__":
    #load_captions("../../../data/Quantum computing explained in 10 minutes _ Shohini Ghose-QuR969uMICM.en.vtt", "QuR969uMICM")
    bulk_load('../../../data/')
