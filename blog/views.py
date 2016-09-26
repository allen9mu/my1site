from django.shortcuts import render

# Create your views here.

from .models import Post

def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts':posts})

def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post,slug=post,
                             status='published',
                             published_year=year,
                             published_month=month,
                             published_day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post':post})
