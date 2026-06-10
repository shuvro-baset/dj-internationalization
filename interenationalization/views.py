from django.shortcuts import render

from django.utils.translation import gettext as _

def home(request):
    message = _("Hello, world!")
    print(message)