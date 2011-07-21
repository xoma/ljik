# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from ljik.post.models import Post

def for_user(request,user_name):
    posts = Post.objects.filter(author__username=user_name)
    return  render_to_response('post/for_user.html',{'posts':posts,'user_name':user_name})

def for_tag(request,tag_name):
    posts = Post.objects.filter(tags__name=tag_name)
    return render_to_response('post/for_tag.html',{'posts':posts,'tag':tag_name})
    
def show(request,id):
    post = get_object_or_404(Post,pk=id)
    tags = post.tags.all()
    return render_to_response('post/show.html',{'tags':tags,'post':post})


