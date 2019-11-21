from django.http import HttpResponseRedirect, HttpResponseNotFound

from .forms import CommentForms, NewPost
from .forms import ArticleForm
from blog.models import Blog, Comments
from django.shortcuts import render, get_object_or_404, redirect, render, reverse
from django.utils import timezone


def blog_list(request):
    """Вивод новин"""
    blog = Blog.objects.all()
    return render(request, "blog/blog_list.html", {"blog": blog})


def new_single(request, pk):
    """Повна стаття """
    new = get_object_or_404(Blog, id=pk)
    comment = Comments.objects.filter(new=pk)
    if request.method == "POST":
        form = CommentForms(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.new = new
            form.save()
            return redirect(new_single, pk)
    else:
        form = CommentForms()
    return render(request, "blog/new_single.html",
                  {"new": new,
                   "comments": comment,
                   "form": form})


def post_new(request):
    if request.method == "POST":
        form = NewPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.created = timezone.now()
            post.save()
            redirect_url = reverse(blog_list)
            return redirect(redirect_url)
    else:
        form = NewPost
    return render(request, 'blog/new_post.html', {'form': form})


def edit(request, id, template_name='blog/edit_post.html'):
    if id:
        article = get_object_or_404(Blog, id=id)
        if article.user != request.user and article.user.is_superuser:
            redirect_url = reverse(blog_list)
            return redirect(redirect_url, {})
    else:
        article = Blog(user=request.user)

    form = ArticleForm(request.POST or None, instance=article)
    if request.POST and form.is_valid():
        form.save()
        redirect_url = reverse(blog_list)
        return redirect(redirect_url, {})
    return render(request, template_name, {'form': form, })

def editcom(request, id):
    try:
        com = Comments.objects.get(id=id)
        if request.method == "POST":
            com.text = request.POST.get("text")
            com.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "blog/edit_comment.html", {"com": com})
    except Comments.DoesNotExist:
        return HttpResponseNotFound("<h2>Коментар не знайдено</h2>")

def delete(request, id):
    try:
        blog = Blog.objects.get(id=id)
        blog.delete()
        return HttpResponseRedirect("/")
    except Blog.DoesNotExist:
        return HttpResponseNotFound("<h2>Пост не знайдено</h2>")

def deletecom(request, id):
    try:
        comment = Comments.objects.get(id=id)
        comment.delete()
        return HttpResponseRedirect("/")
    except Blog.DoesNotExist:
        return HttpResponseNotFound("<h2>Коментар не знайдено</h2>")