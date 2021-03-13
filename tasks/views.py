from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from tasks.models import Task

# Create your views here.
flag = False

def index(request):
    tasks = Task.objects.all()
    return render(request , "tasks/index.html" , {
        "tasks" : tasks
    })

def create(request):
    print("enter create method")
    global flag
    print("value of flag is" , flag)
    if flag and request.method == "POST" :
        id          = request.POST["id"]
        title       = request.POST["title"]
        description = request.POST["description"]
        priority    = request.POST["priority"]
        completed   = request.POST["completed"]
        getId = Task.objects.get(pk=id)
        getId.id = id
        getId.title = title
        getId.description = description
        getId.priority = priority
        getId.completed = completed
        getId.save()
        flag = False
        return redirect("index")
    elif request.method == "POST":
        row = {
            "id"          : request.POST["id"],
            "title"       : request.POST["title"],
            "description" : request.POST["description"],
            "priority"    : request.POST["priority"],
            "completed"   : request.POST["completed"],
        }
        Task.objects.create(
            id          = row["id"] , 
            title       = row["title"] , 
            description = row["description"] , 
            priority    = row["priority"] , 
            completed   = row["completed"])
        return redirect("index")
    return render(request , "tasks/create.html")

def update(request , id):
    global flag
    flag = True
    print("enter update method")
    getRow = Task.objects.get(pk=id)
    row = {
        "id"           : getRow.id,
        "title"        : getRow.title,
        "description"  : getRow.description,
        "priority"     : getRow.priority,
        "completed"    : getRow.completed,
        "flag"         : flag,
    }
    # print("check getrow value here" , getRow)
    # getRow.title = "task1 here"
    # getRow.description = "task1 description here"
    # getRow.save()
    # print("see this print message" , getRow.title)
    return render(request , "tasks/create.html" , row)

def delete(request , id):
    getRow = Task.objects.get(pk=id)
    getRow.delete()
    return redirect("index")