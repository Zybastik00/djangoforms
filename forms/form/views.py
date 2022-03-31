from django.shortcuts import render
from .models import People
from .forms import UserForm
from django.http import HttpResponse

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        number_phone = request.POST.get("number_phone")
        b=People(name=name,number_phone=number_phone)
        b.save()
        return render(request, 'menu.html')
    else:
        userform = UserForm()

    context={'man':People.objects.all,
            "form": userform
             }
    return render(request,'home.html',context)

def menu(request):
    print('Добро пожаловать')
    return render(request, 'menu.html')

def opisanie(request):
    return render(request,'opisanie.html')

# def price(request):
#     return render(request,'price.html')



