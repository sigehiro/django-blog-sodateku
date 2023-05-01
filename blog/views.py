from django.shortcuts import render, get_object_or_404, redirect

from blog.models import Post, Comment
from .forms import CommentCreateForm

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        
    }
    return render(request, 'blog/index.html', context)

# 新規投稿
def create(request):
    return render(request,'blog/create.html')

# 登録投稿
def store(request):
    post = Post(
        title = request.POST.get('title'),
        text = request.POST.get('text'),
        user = request.user,
    )
    post.save()
    return redirect(index)

# 詳細画面
def show(request, id):
    post = get_object_or_404(Post, pk=id)
    comments = Comment.objects.filter(target=id)
    context = {
        'post': post,
        'comments': comments
    }
    return render(request,'blog/show.html', context)

# 編集画面
def edit(request, id):
    post = get_object_or_404(Post, pk=id)
    context = {
        'post': post,
    }
    return render(request,'blog/edit.html', context)

# 更新画面
def update(request, id):
    post = Post(
        pk = id,
        title = request.POST.get('title'),
        text = request.POST.get('text'),
    )
    post.save(
        update_fields = ['title', 'text', 'updated_at']
    )
    return redirect(index)

# 削除画面
def destroy(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect(index)

# コメント画面
def comment(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        comment_create_form = CommentCreateForm(request.POST)
        if comment_create_form.is_valid():
            comment = comment_create_form.save(commit=False)
            comment.user = request.user
            comment.target = post
            comment.save()
            return redirect(show, id)
    else:
        comment_create_form = CommentCreateForm()   
    
    context = {
        'post': post,
        'form': comment_create_form,
    
    }
    return render(request,'blog/comment.html', context)
