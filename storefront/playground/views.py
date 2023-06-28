from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User


def dashboard_view(request):
    user = User()
    # Handle login form submission
    user.username = request.POST['username']
    user.password = request.POST['password']
    user.auCo = 0
    user.cad = 0
    user.save()
    return render(request, 'dashboard.html', {'user': user})


def add_money(request):
    if request.method == 'POST':
        auco_input = request.POST.get('auco_input', 0)
        cad_input = request.POST.get('cad_input', 0)
        success = 'AuCo: ' + str(auco_input) + '\n' + 'CAD: ' + str(cad_input)
        return HttpResponse(success)

def login(request):
    return render(request, 'login.html')


def create_account(request):
    pass
