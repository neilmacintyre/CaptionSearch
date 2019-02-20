from django.shortcuts import render
from django.template import Context, Template
from django.http import HttpResponse
from .models import Caption, Word

# Create your views here.
def index(request):
    return HttpResponse("Hello  World")

def detail(request, question_id):
    latest_question_list = Caption.objects.all()

    output = ''.join(["<p>" + str(cap) + "</p>" for cap in latest_question_list])

    return HttpResponse("You're looking at question %s." % output)

def word_query(request, word, page=0):
    # query for Words

    query = Word.objects.filter(word=word).values()
    context = {"querqy_results": query[page*5:page*5+5]}

    return render(request, 'query_results.html', context=context)
