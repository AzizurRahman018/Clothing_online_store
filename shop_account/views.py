from django.shortcuts import render

def LOGIN(request):

    return render(request,'Accounts/login.html')
def Reg(request):

    return render(request,'Accounts/reg.html')
def Reset(request):

    return render(request,'Accounts/reset.html')