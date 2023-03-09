from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.


class PostList(heneric.ListView):
    model = Post
    queryset = Post.object.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6