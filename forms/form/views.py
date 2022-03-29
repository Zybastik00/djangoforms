from django.shortcuts import render
from .models import Animals
from .forms import UserForm

def home(request):
   # Animal=[]
  #  for item in Animals.objects.all():
   #     Animal.append(item)
    if request.method == "POST":
        name = request.POST.get("name")
        type1 = request.POST.get("type1")
        b=Animals(name=name,type1=type1)
        b.save()
        return render(request, 'home.html')
    else:
        userform = UserForm()

    context={'animal':Animals.objects.all,
            "form": userform
             }
    return render(request,'home.html',context)


