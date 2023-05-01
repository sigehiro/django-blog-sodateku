from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html')

# 新規投稿
def create(request):
    return render(request,'blog/create.html')

# 登録投稿
def store(request):
    pass

# 詳細画面
def show(request):
    return render(request,'blog/show.html')

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
