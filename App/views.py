from django.shortcuts import render, reverse, redirect
from .models import Job
# Create your views here.

def search(request):

    if request.method == "POST":
        searched= request.POST['query']
        search = Job.objects.filter(title__contains= searched)
        context = {
            "searches": search,
        }
        return render(request, "Home/search.html", context)
    else:
        return render(request, "Home/search.html")

def home(request):
    jobs = Job.objects.all()

    context = {
        "jobs": jobs,
    }
    return render(request, "Home/index.html", context)


def details(request, id):
    if id == 0:
        return redirect(reverse('home'))
    jobs = Job.objects.get(pk=id)
    context = {
        "jobs": jobs,
    }
    return render(request,'Home/details.html',context)