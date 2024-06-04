from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def home(request):
    return render(request, "./html/index.html")

def about(request):
    return render(request, './html/about.html')

def hobbies(request):
    return render(request, './html/hobbies.html')

def contact(request):
    return render(request, './html/form.html')

def gallery(request):
    return render(request, './html/gallery.html')

def posts(request):
    posts_list = Post.objects.all()
    return render(request, './html/posts.html', {'posts': posts_list})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, './html/post_detail.html', {'post': post})