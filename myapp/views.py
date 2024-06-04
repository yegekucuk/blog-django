from django.shortcuts import render, HttpResponse

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
    return render(request, './html/posts.html')