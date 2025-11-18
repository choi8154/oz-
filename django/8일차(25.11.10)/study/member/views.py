from django.shortcuts import render
from django.views.generic import FormView

from member.forms import SignupForm

# Create your views here.
class SignupView(FormView):
    template_name = 'auth/signup.html'
    form_class = SignupForm