from django.shortcuts import redirect

# Create your views here.

def landing_login(request):
    return redirect('account_login')