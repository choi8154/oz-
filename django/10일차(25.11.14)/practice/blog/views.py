from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .form import BlogForm

def blog_list(request):
    blogs = Blog.objects.filter(complete=False)
    context = {
        'blogs':blogs
    }
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {
        'blog':blog
    }
    return render(request, 'blog/blog_detail.html', context)

def blog_create(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        blog = form.save(commit=False)
        blog.save()
        return redirect('blog_list')
    context = {
        'form':form,
    }
    return render(request, 'blog/blog_create.html', context)


def blog_put(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        blog = form.save(commit=False)
        blog.save()
        return redirect('blog_detail', pk=blog.pk)
    context = {
        "form":form
    }
    return render(request, 'blog/blog_create.html', context)

def blog_complete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.complete = True
    blog.save()
    return redirect('blog_list')


def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('blog_list')

def done_list(request):
    dones = Blog.objects.filter(complete=True)
    return render(request, 'blog/done_list.html', {'dones':dones})