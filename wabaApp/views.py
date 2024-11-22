from django.shortcuts import render

# Create your views here.
def blank_page(request):
    return render(request, 'blank-page.html')

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def login_admin(request):
    return render(request, 'loginadmin.html')

def login_employee(request):
    return render(request, 'loginemployee.html')

def register(request):
    return render(request, 'register.html')

def employeedashboard(request):
    return render(request, 'employee-dashboard.html')

def customerdashboard(request):
    return render(request, 'admin-dashboard.html')

def admindashboard(request):
    return render(request, 'customer-dashboard.html')
