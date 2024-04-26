from django.db.models import Q
from django.db.models.sql import AND
from django.shortcuts import render
from .models import Userregistration
from .forms import UserregistrationForm


def home(request):
    return render(request, 'visa/home.html')
def login(request):
    context = {'message':'Invalid Credentials......'}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = Userregistration.objects.filter(Q(username=username),  Q(password=password))
        if data:
            return render(request,'visa/main_home.html')
        else:
            return render(request,'visa/login.html',context)
    return render(request, 'visa/login.html')
def signup(request):
    form = UserregistrationForm(request.POST)
    if(request.method == "POST"):

        print('inside post')
        if(form.is_valid()):
            form.save()
            return render(request,'visa/loginsuccess.html')
    # else:
    #     form = UserRegForm()
    return render(request, 'visa/signup.html',{'form':form})

def eligibility(request):
    return render(request, 'visa/eligibility.html')

def faqs(request):
    return render(request, 'visa/faqs.html')

def instructions(request):
    return render(request, 'visa/instructions.html')

def payment(request):
    return render(request, 'visa/payment.html')

def apply(request):
    return render(request, 'visa/apply.html')

def regular(request):
    return render(request, 'visa/regular.html')

def r2(request):
    return render(request, 'visa/r2.html')

def r3(request):
    return render(request, 'visa/r3.html')

def r4(request):
    return render(request, 'visa/r4.html')

def r5(request):
    return render(request, 'visa/r5.html')

def r6(request):
    return render(request, 'visa/r6.html')

def r7(request):
    return render(request, 'visa/r7.html')




