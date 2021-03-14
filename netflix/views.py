from django.contrib.auth.decorators   import login_required , permission_required
from django.shortcuts                 import render , redirect
from django.http                      import HttpResponse
from .forms                           import MovieForm , CategoryForm
from .models                          import Movie , Category
# from django.contrib.auth.models import User

# Create your views here.


@login_required
def index(request):
    global aid
    movies = Movie.objects.all()
    print(movies)
    return render(request , "netflix/index.html" , {
        "movies"  : movies ,
    })

@login_required
@permission_required("netflix.view_movie") #"application.view_modelname" it can be view or add or delete or change
def show(request , id):
    movie = Movie.objects.get(pk=id)
    return render(request , "netflix/show.html" , {
        "movie" : movie ,
    })

@login_required
def create(request):
    form = MovieForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request , "netflix/create.html" , {
        "form" : form ,
    })

@login_required
def update(request , id):
    movie = Movie.objects.get(pk=id)
    form = MovieForm(request.POST or None , request.FILES or None , instance=movie)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request , "netflix/edit.html" , {
        "form"  : form  ,
        "movie" : movie ,
    })

@login_required
def delete(request , id):
    movie = Movie.objects.get(pk=id)
    movie.delete()
    return redirect("index")