# Create your views here.

from django.http import Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.models import User
from ljik.post.models import Post

def for_user(request,user_name):
    user = get_object_or_404(User, username=user_name)
    posts = Post.public.filter(author=user.id).all()
    return  render_to_response('post/for_user.html',{'posts':posts,'user':user})


def for_tag(request,tag_name):
    posts = Post.public.filter(tags__name=tag_name)
    return render_to_response('post/for_tag.html',{'posts':posts,'tag':tag_name})

    
def show(request,id):
    id = int(id)
    try:
        post = Post.public.get(pk=id)
        tags = post.tags.all()
    except Post.DoesNotExists:
        raise Http404

    return render_to_response('post/show.html',{'tags':tags,'post':post,'blog':post.blog})


