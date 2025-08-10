from django.shortcuts import redirect, render
from django.contrib.auth import logout

# Create your views here.


def landing_login(request):
    # Redirects unauthenticated users to the login page.
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('account_login')


def profile_view(request):
    # View to make profile a template variable
    profile = request.user.profile
    return render(request, 'profile/profile.html', {'profile': profile})


def delete_user(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            user.delete()
            logout(request)
            return redirect('account_login')
        else:
            return render(request, 'profile/delete_user.html')
