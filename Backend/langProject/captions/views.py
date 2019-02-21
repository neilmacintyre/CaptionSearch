from django.shortcuts import render
from django.template import Context, Template
from django.http import HttpResponse
from .models import CaptionSegment, Word, Video

# Create your views here.
def index(request):
    return HttpResponse("Hello  World")

def word_query(request, word, page=0):
    # query for Words

    querys = Word.objects.filter(word=word).values()

    # add title, start time, caption segment to query
    for query in querys:
        # get the segment containing the word
        containing_caption_segment = CaptionSegment.objects.get(id=query['caption_segment_id_id'])
        video_title = Video.objects.get(video_id=query['video_id_id']).title

        query['start_time'] = containing_caption_segment.start_time
        query['caption'] = containing_caption_segment.caption
        query['title'] = video_title


    context = {"query_results": querys[page*5:page*5+5]}

    return render(request, 'query_results.html', context=context)
