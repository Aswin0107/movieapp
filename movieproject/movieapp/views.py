from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

from .models import movie
from .forms import movieform


def demo(request):
    film=movie.objects.all()
    content={
        'cinema':film
    }
    return render(request,'index.html',content)

def detail(request,movieid):
    movies=movie.objects.get(id=movieid)
    return  render(request,'detail.html',{'movies':movies})

def add(request):
     if request.method=='POST':
         name=request.POST.get('name')
         about = request.POST.get('about')
         Year = request.POST.get('Year')
         image = request.FILES['image']
         film=movie(name=name,about=about,Year=Year,image=image)
         film.save()
     return render (request,'add.html')

def update(request,id):
     film=movie.objects.get(id=id)
     form=movieform(request.POST or None,request.FILES,instance=film)
     if form.is_valid():
        form.save()
        return redirect('/')
     return render(request,'edit.html',{'film':film,'form':form})
def delete(request,id):
    if request.method=='POST':
        film=movie.objects.get(id=id)
        film.delete()
        return redirect('/')
    return  render(request,'delete.html')
