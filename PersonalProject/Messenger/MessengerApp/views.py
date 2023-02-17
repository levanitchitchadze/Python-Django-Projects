from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib import messages
from django.core import serializers
# from django.contrib.auth.forms import LoginForm 
from django.contrib.auth import authenticate, login,logout

def RegPage(request):

    form=RegistrationForm()
    context={'RegForm':form}

    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
            print("Registrated")


    return render(request, 'HTML/RegistrationPage.html',context)
 

def LoginPage(request):
    Lform=LoginForm()
    context={'LoginForm':Lform}
    object_list=serializers.serialize("python",Customers.objects.all())
    
    
    
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        # user = authenticate(request, username=username, password=password)

        # if user is not None:
        #     print("user is not empty")
        #     login(request,user)
        #     return redirect('Account/')

        for object in object_list:
            # for fields in object['fields'].items():
            Email=object['fields']['username']
            Password=object['fields']['password']
            
            if Email==request.POST['username'] and Password==request.POST['password']:
                Id=object['pk']


                return HttpResponseRedirect('Account/')


    return render(request, 'HTML/LoginPageP.html', context)



def ChatPage(request):
    object_list=Contact.objects.filter().all()

    return render(request, 'HTML/ChatingPage.html',{"OL":object_list})









def AboutPage(request):
    object_list=AboutModel.objects.filter().only('Text')
    object=object_list[len(object_list)-1]
    
    return render(request, 'HTML/AboutPage.html',{"OL":object})



def ContactFunction(request):
    form=ContactForm()
    context={'ContactForm':form}

    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('/')
            print("contact saved")


    return render(request, 'HTML/Contact.html', context)



def ServicesPage(request):
    return render(request, 'HTML/Services.html')


def ProEditPage(request):
    form=AboutForm()
    if request.method=='POST':
        form=AboutForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('/')
            print("AboutText saved")

    return render(request,'HTML/ProfileEditPage.html',{"form":form})



def TestHtml(request):
    return render(request,'test.html')