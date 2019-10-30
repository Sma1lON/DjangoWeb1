from django.shortcuts import render
from blog.models import Blog, Comments
from django.shortcuts import render,get_object_or_404
from blog.forms import CommentForms
def blog_list(request):
    """Вивод новин"""
    blog=Blog.objects.all()
    return render(request,"blog/blog_list.html",{"blog":blog})

def new_single(request, pk):
    """Повна стаття """
    new = get_object_or_404(Blog, id=pk)
    comment = Comments.objects.filter(new=pk)
    if request.method == "post":
        form = CommentForms(request.post)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.new = new
            form.save()
    else:
         form = CommentForms()
    return render(request, "blog/new_single.html",{"new": new,"comments":comment,
                                                   "form":form})