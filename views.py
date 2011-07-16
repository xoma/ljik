# -*- coding: utf-8 -*-

# Create your views here.

from django.shortcuts  import render_to_response
from ljik.quotes.models import Quote
from ljik.post.models import Post
from ljik.links.models import Link

def index(request):
    # получим последние записи всех типов
    quote = Quote.public.latest()
    post  = Post.public.latest()
    link  = Link.public.latest()
    return  render_to_response('index.html',{'link':link,'post':post,'quote':quote})
