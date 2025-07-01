from django.shortcuts import redirect, render

# Create your views here.

# makes login the landing page.
def landing_login(request):
    return redirect('account_login')


#
def profile_view(request):
    profile = request.user.profile
    return render(request, 'profile.html', {'profile': profile})