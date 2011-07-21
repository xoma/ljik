from django.shortcuts import get_object_or_404, render_to_response
from ljik.links.models import Link


def show(request,id):
    link = get_object_or_404(Link,pk=id)
    tags = link.tags.all()
    return  render_to_response('links/show.html',{'link':link,'tags':tags})

def for_user(request,user_name):
    links = Link.objects.filter(author__username=user_name).all()
    return  render_to_response('links/for_user.html',{'links':links,'user_name':user_name})

def for_tag(request,tag_name):
    links = Link.objects.filter(tags__name=tag_name)
    return render_to_response('links/for_tag.html',{'links':links,'tag':tag_name})