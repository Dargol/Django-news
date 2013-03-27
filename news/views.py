# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from news.models import *
from news.forms import *

def getNewsByDate():
    return News.objects.all().order_by('-posted_date')

def Front(request):
    news = getNewsByDate()
    if news:
        return render_to_response('front.html',
            {'news': news,
             'title'  :'Strona Główna',

             },
            context_instance=RequestContext(request))
    else:
        return render_to_response('front.html',
            {'zmienna':'Brak wpisów',
             'title'  :'Strona Główna',
            },
            context_instance=RequestContext(request))

def AddNews(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():

            form.save()
            return HttpResponseRedirect('/')
        else:
            return render_to_response('addNews.html', {
                'form': form.as_table(),
                'title': 'Dodaj Newsa',
                },
                context_instance=RequestContext(request))


    else:
        form = NewsForm() # An unbound form

        return render_to_response('addNews.html', {
            'form': form.as_table(),
            'title': 'Dodaj Newsa',
            },
            context_instance=RequestContext(request))