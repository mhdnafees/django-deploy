from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from test_app_temp.models import PUser
from . import forms
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index_main.html')

def index_users(request):
    User_Base = PUser.objects.order_by('name')
    my_dic = {'userbase':User_Base}
    return render(request,'test_app_temp/index.html', context = my_dic )

def index_forms(request):
    tform = forms.Aform()
    if request.method == 'POST':
        tform = forms.Aform(request.POST)

        if tform.is_valid():
            print("NAME: "+tform.cleaned_data['name'])
            print("EMAIL: "+tform.cleaned_data['email'])
            print("TEXT: "+tform.cleaned_data['text'])
            tform.save()
            return index(request)

    return render(request,'test_app_temp/forms.html',{'form':tform})

def reg_forms(request):
    registered = False

    if request.method == 'POST':
        user_form = forms.UserForm(request.POST)
        userinfo_form = forms.UserInfoForm(request.POST)

        if user_form.is_valid() and userinfo_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            UI = userinfo_form.save(commit=False)
            UI.user = user

            if 'dp' in request.FILES:
                UI.dp = request.FILES['dp']

            UI.save()

            registered = True
            return HttpResponseRedirect(reverse('index'))


        else:
            print(user_form.errors,userinfo_form.errors)
    else:
        user_form = forms.UserForm()
        userinfo_form = forms.UserInfoForm()
    return render(request,'test_app_temp/register.html',{'user_form':user_form,'userinfo_form':userinfo_form,'registered':registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("You are not a active user")
        else:
            print("Thiefff")
            return HttpResponse("Invalid details")
    else:
        return render(request,'test_app_temp/ulogin.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("This is a special one")
