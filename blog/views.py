from ctypes.wintypes import HENHMETAFILE
from django.http import HttpResponseGone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Wallet
from .forms import PostForm
from django.utils import timezone

# Create your views here.
def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.order_by('published_date')
    # wallet = Wallet()
    # wallet = get_object_or_404(Wallet,pk=1)
    
    return render(request, 'blog/post_list.html',{'posts':posts})

def init_wallet(request):
    wallet = Wallet()
    wallet.save()
    return render(request,'blog/post_list.html',{'wallet':wallet})
    # redirect('post_list')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        if "plus_1_btn" in request.POST:
            post.plus1()
        elif "minus_1_btn" in request.POST:
            post.minus1()
        # return redirect('')
    return render(request, 'blog/post_detail.html',{'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form})
