from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm

# Create your views here.

# makes login the landing page.
def landing_login(request):
    return redirect('account_login')


# View to make Profiel a template variable
def profile_view(request):
    profile = request.user.profile
    return render(request, 'profile/profile.html', {'profile': profile})

# View to handle user registration
class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('profile')

    