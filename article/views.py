from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader, Context
from article.models import Article
from datetime import datetime

# Create your views here.

def home(request):
    ctx = {'post_list': Article.objects.all()}
    return render_to_response('home.html', ctx)

def detail(request, args):
    try:
    	post = Article.objects.all()[int(args)]
    	parameter = ("title = %s, category = %s, date_time = %s, content%s" %
        (post.title, post.category, post.date_time, post.content))
    except:
         parameter = "Parameter is not exist" 
    return HttpResponse(parameter)

def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})
