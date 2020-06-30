from django.shortcuts import render,redirect
from django.contrib.auth.models import User                #For import user
from django.contrib.auth import authenticate,login,logout
from home.models import Biodata
# Create your views here.

def index(request):                                
    if request.method=="POST":                       #check for post method
        user_name=request.POST.get('username')       #get username and password
        user_password=request.POST.get('password')
        user=authenticate(username=user_name,password=user_password)
        if user is not None:
            login(request,user)
            abc=Biodata.objects.filter(author=user).last()

            return render(request,"home.html",{'abc':abc})
            
        else:
            return render(request,"index.html")
   
    return render(request,"index.html",)

def createUser(request):
    if request.method=="POST":
        user_name=request.POST.get("username")
        user_mail=request.POST.get("email")
        user_password=request.POST.get("password")
        user_first_name=request.POST.get("firstname")
        user_last_name=request.POST.get("lastname")

        user = User.objects.create_user(user_name, user_mail, user_password)
        user.first_name=user_first_name
        user.last_name = user_last_name
        user.save()
        return redirect("/")
    return render(request,"NewUser.html")

def homePage(request):
    abc=Biodata.objects.filter(author=request.user).last()
    return render(request,"home.html",{'abc':abc})

def cvPage(request):
    abc=Biodata.objects.filter(author=request.user).last()
    return render(request,"cv.html",{'abc':abc})

def projectsPage(request):
    abc=Biodata.objects.filter(author=request.user).last()
    return render(request,"projects.html",{'abc':abc})

def getInfo(request):
    if request.method=="POST":
        firstname=request.POST.get("firstname")
        lasttname=request.POST.get("lastname")
        contact=request.POST.get("contactnumber")
        email=request.POST.get("email")
        localaddress=request.POST.get("localaddress")
        permenantaddress=request.POST.get("permenantaddress")
        careerobjective=request.POST.get("careerobjective")
        skill1=request.POST.get("skill1")                       #
        skill2=request.POST.get("skill2")                       #
        skill3=request.POST.get("skill3")                       #
        internship=request.POST.get("internship")
        ssc=request.POST.get("ssc")
        hsc=request.POST.get("hsc")
        cgpa=request.POST.get("cgpa")
        project1=request.POST.get("project1")
        project2=request.POST.get("project2")
        project3=request.POST.get("project3")
        author = request.user
        print(author)
        biodata=Biodata(firstname=firstname,lasttname=lasttname,contact=contact,email=email,localaddress=localaddress,permenantaddress=permenantaddress,careerobjective=careerobjective,skill1=skill1,skill2=skill2,skill3=skill3,internship=internship,ssc=ssc,hsc=hsc,cgpa=cgpa,project1=project1,project2=project2,project3=project3,author=author)
        biodata.save()
        return redirect("/home")
    return render(request,"getInfo.html")




def logoutUser(request):
    logout(request)
    return render(request,"index.html")






