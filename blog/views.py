from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Post, Category
from .forms import PostForm
from .forms import CategoryForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('post_list')
    else:
        form = PostForm()
        return render(request, 'blog/post_form.html', {'form': form})


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            # post = form.save(commit=False)
            # post.author = request.user
            # post.save()
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'blog/post_form.html', {'form': form})


#Удаление поста
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":  # подтверждаем удаление
        post.delete()
        return redirect("post_list")  # имя твоего URL со списком постов
    return render(request, "blog/post_confirm_delete.html", {"post": post})







# ----- CRUD для категорий -----

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'blog/category_form.html', {'form': form})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'blog/category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'blog/category_confirm_delete.html', {'category': category})
# C_R_UD

# Post.objects.all()
# Post.objects.get(id=1)
# Post.objects.filter()
# author = User.objects.get(username='pushkin')
# Filters :
    # contains 
    # exact =
    # startwith
    # endwith 
    # gt >
    # gte >=
    # lt < 
    # lte <=
