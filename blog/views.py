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


def blog_detail(request, pk):
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
            return redirect(blog_detail, pk)
    else:
        form = CommentForms()
    return render(request, "blog/blog_detail.html",
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


def editcom(request, id, cid):
    entity = get_object_or_404(Comments, id=cid)
    if entity.user != request.user and entity.user.is_superuser:
        redirect_url = reverse(blog_list)
        return redirect(redirect_url, {})
    form = CommentForms(request.POST or None, instance=entity)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect(reverse("blog_detail", kwargs={'pk': id}))

    return render(request, "blog/edit_com.html", {"form": form})


def delete(request, id):
    blog = get_object_or_404(Blog, id=id)
    if blog.user != request.user and blog.user.is_superuser:
        redirect_url = reverse(blog_list)
        return redirect(redirect_url, {})
    form = ArticleForm(request.POST or None, instance=blog)
    if request.method == "POST" and form.is_valid():
        redirect_url = reverse(blog_list)
        return redirect(redirect_url, {})
    return render(request, "blog/del_post.html", {'form': form, })


def deletecom(request, id, cid):
    comment = get_object_or_404(Comments, id=cid)
    if comment.user != request.user and comment.user.is_superuser:
        redirect_url = reverse(blog_list)
        return redirect(redirect_url, {})
    form = CommentForms(request.POST or None, instance=comment)
    if request.method == "POST" and form.is_valid():
        comment.delete()
        return redirect(reverse("blog_detail", kwargs={'pk': id}))
    return render(request, "blog/del_com.html", {"form": form})