# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.models import User

from ljik.quotes.models import Quote

def for_user(request,user_name):
    user = get_object_or_404(User,username=user_name)
    quotes = Quote.public.filter(author=user.id).all()
    return render_to_response('quotes/for_user.html',{'user':user,'quotes':quotes})


def show(request,id):
    id = int(id)
    try:
        quote = Quote.public.get(pk=id)
        tags  = quote.tags.all()
    except Quote.DoesNotExist:
        raise Http404

    return render_to_response('quotes/show.html',{'quote':quote,'tags':tags})

def list(request):
    quotes_list = Quote.public.all()[1]
    return render_to_response('quotes/list.html',{'list':quotes_list})

def for_tag(request,tag_name):
    quotes = Quote.public.filter(tags__name=tag_name)
    return render_to_response('quotes/for_tag.html',{'quotes':quotes,'tag':tag_name})

