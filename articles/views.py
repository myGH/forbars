# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from articles.models import Comment, Article
from django.utils import timezone
from django.core.paginator import Paginator, InvalidPage
from django.http import Http404

def index(request, pagenum=1):
    article_list = Article.objects.filter(date_change__lte=timezone.now).order_by('-date_change')
    paginator = Paginator(article_list, 10)
    try:
        articles = paginator.page(pagenum)
    except InvalidPage:
        raise Http404
    if int(pagenum)-5 in paginator.page_range:
        previousArrow = paginator.page_range[0]
    else:
        previousArrow = 0
    if int(pagenum)>1:
        previous = paginator.page_range[:(int(pagenum)-1)]
        previous = previous[-4:]
    else:
        previous = 0
        this = 0
    if int(pagenum)<paginator.num_pages:
        next = paginator.page_range[(int(pagenum)):]
        next = next[:4]
    else:
        next = 0
    if int(pagenum)+5 in paginator.page_range:
        nextArrow = paginator.page_range[paginator.num_pages-1]
    else:
        nextArrow = 0
    if paginator.num_pages>1:
        this = int(pagenum)
    else:
        this = 0
    return render(request, 'articles/index.html', {'articles': articles, 'previousArrow':previousArrow, 'previous': previous, 'next':next, 'nextArrow':nextArrow, 'this':this})

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk, date_change__lte=timezone.now)
    return render(request, 'articles/detail.html', {'article': article})

def comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id, date_change__lte=timezone.now)
    return render(request, 'articles/comment.html', {'article': article})

def add_comment(request, article_id):
    a = get_object_or_404(Article, pk=article_id, date_change__lte=timezone.now)
    if request.POST['comment']:
        a.comment_set.create(comment_text=request.POST['comment'])
        return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))
    else:
        return render(request, 'articles/comment.html', {
            'article': a,
            'error_message': "Поля не должны быть пустыми",
        })

def update(request, article_id):
    article = get_object_or_404(Article, pk=article_id, date_change__lte=timezone.now)
    return render(request, 'articles/article.html', {'article': article})

def add(request):
    return render(request, 'articles/article.html', {'new': True})

def update_article(request, article_id):
    a = get_object_or_404(Article, pk=article_id, date_change__lte=timezone.now)
    a.title = request.POST['title']
    a.article_text = request.POST['text']
    if request.POST['title'] and request.POST['text']:
        a.date_change = timezone.now()
        a.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'articles/article.html', {
            'article': a,
            'error_message': "Поля не должны быть пустыми",
        })

def add_article(request):
    if request.POST['title'] and request.POST['text']:
        a = Article(title=request.POST['title'], article_text=request.POST['text'], date_change=timezone.now())
        a.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'articles/article.html', {
            'new': True,
            'error_message': "Поля не должны быть пустыми",
        })

