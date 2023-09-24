from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
def LOGIN(request):

    return render(request,'Accounts/login.html')
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
                # print(First_name,Last_name,Username,Email,Pass,Pass1)
                    else:
                        messages.warning(request, "Your given password not matched")

    return render(request,'Accounts/reg.html')
def Reset(request):

    return render(request,'Accounts/reset.html')