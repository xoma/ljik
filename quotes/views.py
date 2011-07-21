# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from ljik.quotes.models import Quote

def for_user(request,user_name):
    quotes = Quote.objects.filter(author__username=user_name).all()
    return render_to_response('quotes/for_user.html',{'user_name':user_name,'quotes':quotes})

def show(request,id):
    quote = get_object_or_404(Quote,pk=id)
    tags  = quote.tags.all()
    return render_to_response('quotes/show.html',{'quote':quote,'tags':tags})

def list(request):
    quotes_list = Quote.objects.all()[1]
    return render_to_response('quotes/list.html',{'list':quotes_list})

def for_tag(request,tag_name):
    quotes = Quote.objects.filter(tags__name=tag_name)
    return render_to_response('quotes/for_tag.html',{'quotes':quotes,'tag':tag_name})

