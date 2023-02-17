from django.shortcuts import render, redirect

# Create your views here.
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {'posts': posts}
    return render(request, 'social/home.html', context)

from django.contrib.auth.decorators import login_required

@login_required
def post(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        Post.objects.create(text=text, user=request.user)
        return redirect('home')
    return render(request, 'social/post.html')
