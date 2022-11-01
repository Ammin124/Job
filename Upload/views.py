from django.shortcuts import render
from .forms import UploadForm, UploadFileForm
# Create your views here.

def imgUpdate(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            saveObject = form.instance
            context = {
                'form': form,
                'saveObject': saveObject,
            }
            return render(request, 'imgUpload/upload.html', context)

    else:
        form = UploadForm()
    context ={
        'form': form,
    }
    return render(request,'imgUpload/upload.html',context)


def fileUpdate(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            saveObject = form.instance
            context = {
                'form': form,
                'saveObject': saveObject,
            }
            return render(request, 'imgUpload/file.html', context)

    else:
        form = UploadFileForm()
    context ={
        'form': form,
    }
    return render(request,'imgUpload/file.html',context)
