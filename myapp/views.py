from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Review
from .forms import ReviewForm

# Create your views here.
def home(request):
    reviews = Review.objects.all().order_by('-date')
    return render(request, "./html/index.html", {'reviews': reviews})

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

def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReviewForm()
    return render(request, 'html/submit_review.html', {'form': form})



# Hobbies
def standart(request):
    return render(request, './html/hobbies/standart.html')

def calisthenics(request):
    return render(request, './html/hobbies/calisthenics.html')

def swimming(request):
    return render(request, './html/hobbies/swimming.html')

def basketball(request):
    return render(request, './html/hobbies/basketball.html')