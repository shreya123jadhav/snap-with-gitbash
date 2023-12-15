from django.shortcuts import render, redirect
from .models import User_Event_Organiser;
from .models import User;
from django.contrib import messages
from django.contrib.auth.models import auth
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def index(request):
    
    if 'user' in request.session:
        current_user = request.session['user']
        events = User_Event_Organiser.Objects.all()
        param = {'current_user': current_user,'events': events}
        return render(request, 'firstapp/index.html',param)
    else:
        events = User_Event_Organiser.Objects.all()
        return render(request, "firstapp/index.html", {'events': events})

def about(request):
     if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user': current_user}
        return render(request, 'firstapp/about.html', param)
     else:         
        return render(request, "firstapp/about.html")




def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        check_user = User.Objects.filter(emailid=username, password=password)
        if check_user:            
            for u in check_user:
                if u.emailid==username:                    
                 request.session['user'] = u.uname  
            return redirect('http://127.0.0.1:8000/firstapp/index/')
        else:
            return HttpResponse('Please enter valid Username or Password.')

    return render(request, 'firstapp/login.html')

def register(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        user=User(uname=uname,emailid=email,phone=phone,password=password)
        user.save()
        # messages.info("user created")
        print(user)
        return redirect('http://127.0.0.1:8000/firstapp/index/')
    else:
        return render(request, "firstapp/registration.html")

def admin(request):
    return render(request, "firstapp/admin.html")


def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('http://127.0.0.1:8000/firstapp/login/')
    return redirect('http://127.0.0.1:8000/firstapp/login/')

#genre

def entertainment(request):
    return render(request, "firstapp/entertainment.html")
def art(request):
    return render(request, "firstapp/art.html")
def sport(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user': current_user}
        return render(request, 'base.html', param)
    return render(request, "firstapp/sport.html")
def workshop(request):
    return render(request, "firstapp/workshop.html")
def conference(request):
    return render(request, "firstapp/conference.html")
def comedy(request):
    return render(request, "firstapp/comedy.html")



