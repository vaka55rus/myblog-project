from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def showblog(request):
	post = Post.objects
	return render(request, 'blog/blog.html', {'post': post})

def post_details(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	return render(request, 'blog/post_details.html', {'post': post})