from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        second_name = request.POST['secondname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password== password2:
            if User.objects.filter(username=username).exists():
                
                messages.info(request,'username already exists')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,password=password2,email=email,first_name=first_name,last_name=second_name)
                user.save()
                print('user created')
                return redirect('login')
        else: 
            messages.info(request,'password does not match')
            return redirect('signup')
    else:

        return render(request,'signup.html')
    
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"inavlid data")
            return redirect('login')

    else:

        return render(request,'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/')