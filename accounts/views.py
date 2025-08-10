from django.shortcuts import redirect, render
from django.contrib.auth import logout

# Create your views here.

# Redirects unauthenticated users to the login page.
def landing_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('account_login')

# View to make profile a template variable
def profile_view(request):
    profile = request.user.profile
    return render(request, 'profile/profile.html', {'profile': profile})

# view to delete user account
def delete_user(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            user.delete()
            logout(request)
            return redirect('account_login')
        else:
            return render(request, 'profile/delete_user.html')
        
