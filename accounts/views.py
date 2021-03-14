from django.shortcuts               import render , redirect
from django.contrib.auth            import authenticate , login
from .models                        import UserCreationFormEdit

# from django.http               import HttpResponse
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signUp(request):
    form = UserCreationFormEdit(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]
        user     = authenticate(username=username , password=password)
        if user :
            login(request , user)
            return redirect("index")
    return render(request , "registration/signUp.html" , {
        "form" : form ,
    })