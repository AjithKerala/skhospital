from django.shortcuts import render

from skapp.models import departmentss


# Create your views here.
def home(request):
    valu={'data':departmentss.objects.all()}
    return render(request,'Home.html',valu)
def depart(request):
    dic={"value":departmentss.objects.all()}

    return render(request,'departments.html',dic)

def docters(request):
    return render(request,'docters.html')