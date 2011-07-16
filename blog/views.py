# Create your views here.
from django.http import Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.models import User
from ljik.core.models import Blog
from ljik.links.models import Link
from ljik.quotes.models import Quote
from ljik.post.models import Post


def show(request,id):
    id = int(id)

    try:
        blog = Blog.objects.get(pk=id)
    except Blog.DoesNotExist:
        raise Http404

    links_cnt = Link.objects.filter(blog=id).count()
    post_cnt  = Post.objects.filter(blog=id).count()
    quote_cnt = Quote.objects.filter(blog=id).count()

    return render_to_response('blog/show.html',{'blog':blog,'links_cnt':links_cnt,'post_cnt':post_cnt,'quote_cnt':quote_cnt})

def user(request,user_name):

    try:
        user  = User.objects.filter(username=user_name).get()
        blogs = Blog.objects.filter(owner=user.id).all();
        post_cnt  = Post.objects.filter(author=user.id).count();
        quote_cnt = Quote.objects.filter(author=user.id).count();
        link_cnt  = Link.objects.filter(author=user.id).count();
    except User.DoesNotExist:
        raise  Http404

    return  render_to_response('blog/show_user.html',{'link_cnt':link_cnt,'quote_cnt':quote_cnt,'post_cnt':post_cnt,'user':user,'blogs':blogs})


    
