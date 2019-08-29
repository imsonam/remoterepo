from django.shortcuts import render
from .models import FormData
from .forms import EmpForm
from django .http.response import HttpResponse
def emp_view(request):
    if request.method=="POST":
        eform=EmpForm(request.POST)
        if eform.is_valid():
            name1=request.POST.get("name")
            sal1 = request.POST.get("sal")
            mobile1=request.POST.get("mobile")
            email1=request.POST.get("email")
            location1=request.POST.get("location")

            data=FormData(name=name1,sal=sal1,mobile=mobile1,email=email1,location=location1)
            data.save()
            eform=EmpForm()
            return render(request,'empdata.html',{'abcd':eform})
        else:
            return HttpResponse("user invalid data")
    else:
        eform =EmpForm()
        return render(request,'empdata.html',{'abcd':eform})




# Create your views here.
