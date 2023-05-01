from django.shortcuts import render, get_object_or_404

from blog.models import Post

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
    pass

# 詳細画面
def show(request, id):
    post = get_object_or_404(Post, pk=id)
    context = {
        'post': post,
    }
    return render(request,'blog/show.html', context)

# 編集画面
def edit(request):
    return render(request,'blog/edit.html')

# 更新画面
def update(request):
    pass

# 削除画面
def destroy(request):
    pass

# コメント画面
def comment(request):
    return render(request,'blog/comment.html')
