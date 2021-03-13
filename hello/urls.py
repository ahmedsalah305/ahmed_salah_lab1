from django.urls import path
from . import views

urlpatterns = [
    # path("city" , views.viewCity , name="viewCity"),
    path("" , views.index , name="index"),
    path("addNew" , views.addNew , name="addNew"),
    path("deleteTask/<str:taskName>" , views.deleteTask , name="deleteTask"),
    # path("world" , views.helloWorld , name="hello"),
    # path("adel" , views.helloAdel , name="adel"),
    # path("<str:name>" , views.hello , name="helloFriend"),
]
