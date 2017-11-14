from django.shortcuts import render,get_object_or_404
from .models import *

# Create your views here.
def index(request):
    post = Post.objects.all()
    return render(request,'blog/index.html',context={'post':post})

def post(request,postid):
    post = get_object_or_404(Post,pk = postid)
    #post = Post.objects.get(id=postid)
    return render(request,'blog/post.html',context={'post':post})

def category(request):
    category = Category.objects.all()
    return render(request,'blog/category.html',context={'category':category})

def category_post(request,cid):
    c = get_object_or_404(Category,pk=cid)
    post = c.post_set.all()
    return render(request, 'blog/index.html', context={'post': post})

def tag(request):
    tag = Tag.objects.all()
    return render(request,'blog/tag.html',context={'tag':tag})

def tag_post(request,tid):
    t = get_object_or_404(Tag,pk=tid)
    post = t.post_set.all()
    return render(request, 'blog/index.html', context={'post': post})