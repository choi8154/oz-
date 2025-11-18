from django.shortcuts import render, get_object_or_404, redirect
from photo.models import Photo
from photo.forms import PhotoForm

# Create your views here.
def photo_list(request):
    photos = Photo.objects.all()
    context = {
        "photos":photos
    }
    return render(request, 'photo/photo_list.html', context)

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    context = {
        "photo":photo,
    }
    return render(request, "photo/photo.html", context)

def photo_create(request):
    form = PhotoForm(request.POST or None)
    if form.is_valid():
        photo = form.save(commit=False)
        photo.save()
        return redirect('photo_detail', pk=photo.pk)
    context = {
        'form':form,
    }
    return render(request, 'photo/photo_post.html', context)

def photo_update(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    form = PhotoForm(request.POST or None, instance=photo)
    if form.is_valid():
        photo = form.save(commit=False)
        photo.save()
        return redirect("photo_detail", pk=photo.pk)
    context = {
        "form": form,
    }
    return render(request, "photo/photo_post.html", context)