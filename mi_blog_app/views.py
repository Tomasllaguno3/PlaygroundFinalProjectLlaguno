from django.shortcuts import render, redirect
from .forms import AuthorForm, PostForm, CommentForm
from .models import Post

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_author_success')  # Redirige a una página de éxito o a donde desees
    else:
        form = AuthorForm()
    return render(request, 'create_author.html', {'form': form})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_post_success')  # Redirige a una página de éxito o a donde desees
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_comment_success')  # Redirige a una página de éxito o a donde desees
    else:
        form = CommentForm()
    return render(request, 'create_comment.html', {'form': form})

def search(request):
    query = request.GET.get('query')
    if query:
        results = Post.objects.filter(title__icontains=query)
    else:
        results = []
    return render(request, 'search.html', {'results': results})