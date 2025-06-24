from django.shortcuts import render, redirect
from .forms import Form
from .models import Employee
# Create your views here.

def employee_list(request):
    context = {'employee_list' : Employee.objects.all()}
    return render(request, 'employee_register/employee_list.html',context)

def employee_form(request,id=0):
    if request.method == "GET":
        if id ==0:
            form = Form()
        else:
            employee = Employee.objects.get(pk=id)
            form = Form(instance=employee)
        return render(request, 'employee_register/employee_form.html',{'form': form})
    else:
        if id == 0:
            form = Form(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = Form(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')
