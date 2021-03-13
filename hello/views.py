from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.

tasks =[]

def index(request):
    isStudent = True
    # print(request.POST.get("task"))
    # cities = ["cairo" , "alex" , "dubai" , "luxor"]
    return render(request , "hello/index.html" , {
        "name"      : "ahmed",
        "tasks"    : tasks,
        "isStudent" : isStudent, 
    })

def addNew(request):
    print("add task done")
    if request.method == "POST":
        task = request.POST["task"]
        tasks.append(task)
        return redirect("index")
    return render(request , "hello/addNew.html")

def deleteTask(request , taskName):
    print("delete task done")
    tasks.remove(taskName)
    return redirect("index")

def viewCity(request):
    name        = "cairo"
    description = "this is city"
    return render(request , "hello/city.html" , {
        "name": name,
        "description": description,
    })

def helloWorld(request):
    return HttpResponse("<h1>hello, world!</h1>")

def helloAdel(request):
    return HttpResponse("hello, Adel!")

def hello(request , name):
    return HttpResponse(f"hello {name} from hello view")