import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from .models import Employee
from .forms import EmployeeForm

def index(request):
    context = {}
    return render(request, 'index.html', context)


def show_modal(request):
    context = {}
    return render(request, 'modal.html', context)


def show_button(request):
    context = {}
    return render(request, 'button.html', context)


def employee_list(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'employee_list.html', context)


def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            emp = form.save()
            return HttpResponse(status=204,
            headers={
                    'HX-Trigger': json.dumps({
                        "EmpListChanged": None,
                        "showMessage": f"{emp.first_name} {emp.last_name} added."
                    })
                })
    else:
        form = EmployeeForm()
    context = {'form': form}
    return render(request, 'employee_form.html', context)


def employee_edit(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            emp = form.save()
            return HttpResponse(status=204,
            headers={
                    'HX-Trigger': json.dumps({
                        "EmpListChanged": None,
                        "showMessage": f"{emp.first_name} {emp.last_name} edited."
                    })
                })
    else:
        form = EmployeeForm(instance=emp)
    context = {'form': form,
                'employee': emp}
    return render(request, 'employee_form.html', context)


# @require_POST
def employee_delete(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    emp.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "EmpListChanged": None,
                "showMessage": f"{emp.first_name} {emp.last_name} deleted."
            })
        })