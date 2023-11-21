from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
def LOGIN(request):
    if request.method == 'POST':
        Username = request.POST.get('username')
        Pass = request.POST.get('password')
        if len(Pass)==0:
            messages.warning(request, "No password Found")
            return redirect('login')

        user= authenticate( username=Username ,password= Pass )
        if user:
            login(request, user)
            return redirect('user_desh')
        if Pass != User.password:
            messages.warning(request, "your password is incorect")
            return redirect('login')

    return render(request,'Accounts/login.html')

def LOGOUT(request):
    logout(request)
    messages.warning(request, "you are loggout")
    return redirect('login')
def Reg(request):
    if request.method =='POST':
        First_name=request.POST.get('first')
        Last_name=request.POST.get('last')
        Username=request.POST.get('username')
        Email=request.POST.get('email')
        Pass=request.POST.get('pass')
        Pass1=request.POST.get('pass1')
        if Username is not None:
            for i in Username:
                if i in ['#','@','/','*','$']:
                    messages.warning(request, "Your username has special Character Please Remove them")
                    return redirect('reg')


                if User.objects.filter(username=Username).exists():
                    messages.warning(request, "Your username already teaken try New")

                elif User.objects.filter(email=Email).exists():
                    messages.warning(request, "Your Email already teaken try New")
                else:
                    if Pass==Pass1:

                      user=User.objects.create(first_name=First_name,last_name=Last_name,username=Username,email=Email,password=Pass)
                      user.set_password(Pass)
                      user.save()
                      return redirect('login')
                # print(First_name,Last_name,Username,Email,Pass,Pass1)
                    else:
                        messages.warning(request, "Your given password not matched")

    return render(request,'Accounts/reg.html')
def Reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        Pass = request.POST.get('password')
        Pass1 = request.POST.get('password1')
        # if User.objects.filter(username=user_name).exists():
        if User.objects.filter(email=email):
            messages.warning(request, "Your user Found")
            user = User.objects.get(email=email)

            if Pass == Pass1:
                user.set_password(Pass)
                user.save()
                messages.success(request, "Password reset successful. You can now log in with your new password.")
                return redirect('login')

    return render(request,'Accounts/reset.html')

def user_desh(request):
    return render(request, 'Accounts/user-desh.html')