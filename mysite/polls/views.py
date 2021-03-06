from django.http import HttpResponse
from pprint import *
from django.template import loader

from .models import Question
from django.shortcuts import get_object_or_404, render

def detail(request, question_id):
    return render(request, 'polls/detail.html', {'question': question})

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    pprint(vars(request))
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    pprint(vars(request))
    return HttpResponse("You're voting on question %s." % question_id)