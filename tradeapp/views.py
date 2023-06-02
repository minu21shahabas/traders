from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'homepage.html')
def company(request):
    return render(request,'company.html')
def homes(request):
    return render(request,'homepage.html')
def service(request):
    return render(request,'services.html')
def pro(request):
    return render(request,'projects.html')
def con(request):
    return render(request,'contact.html')