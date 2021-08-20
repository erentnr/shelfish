from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView

# Create your views here.

class SignupView(CreateView):
    form_class = UserCreationForm
    model = User
    template_name = 'registration/signup.html'
    success_url = '/'
