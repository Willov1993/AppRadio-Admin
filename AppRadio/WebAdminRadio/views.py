from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'WebAdminRadio/login.html', {'title': 'Login'})

def principal(request):
    return render(request, 'WebAdminRadio/base_site.html', {'title': 'Principal'})