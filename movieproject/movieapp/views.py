from django.http import HttpResponse
from django.shortcuts import render,redirect

from .models import Movie
from .forms import movform

# Create your views here.
def demo(request):
    movie=Movie.objects.all()
    context={
        'movielist':movie
    }
    return render(request,'index.html',context)

def detail(request,movieid):
    movie=Movie.objects.get(id=movieid)
    return render(request,"detail.html",{'movie':movie})

def addmov(request):
    if request.method == "POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        movie=Movie(name=name,desc=desc,year=year,img=img)
        movie.save()
        return redirect('/')
    return  render(request,'add.html')


def update(request,id):
    movie1=Movie.objects.get(id=id)
    form1=movform(request.POST or None, request.FILES,instance=movie1)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request,'edit.html',{'movie':movie1,'form':form1})

def delete(request,id):
    if request.method=="POST":
        movie2=Movie.objects.get(id=id)
        movie2.delete()
        return redirect('/')
    return render(request,'del.html')


