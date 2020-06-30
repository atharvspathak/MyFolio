from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),                                  #mainpage/loginpage
    path("createUser",views.createUser),              #newuserpage
    path("home",views.homePage,name="Home"),                            #homepage
    path("cv",views.cvPage,name="CV"),                                  #cvpage
    path("projects",views.projectsPage,name="Projects"),                #projectpage
    path("getInformation",views.getInfo,name="User Info"),              #User Inforamtion
    path("",views.logoutUser,name="logout")                       #logout
   
  
]
