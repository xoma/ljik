from django.http import Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.models import User
from ljik.links.models import Link


def show(request,id):
    id = int(id)
    try:
        link = Link.public.get(pk=id)
        tags = link.tags.all()
    except Link.DoesNotExists:
        raise  Http404
        
    return  render_to_response('links/show.html',{'link':link,'tags':tags})
    

def for_user(request,user_name):
    user = get_object_or_404(User, username=user_name)
    links = Link.public.filter(author=user.id).all()
    return  render_to_response('links/for_user.html',{'links':links,'user':user})

def for_tag(request,tag_name):
    links = Link.public.filter(tags__name=tag_name)
    return render_to_response('links/for_tag.html',{'links':links,'tag':tag_name})