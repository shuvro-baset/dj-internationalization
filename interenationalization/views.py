from django.shortcuts import render
from django.utils.translation import gettext as _, get_language

def home(request):
    user_language = get_language()  # Fetch the active language
    print(user_language) # Display current language in the terminal

    # Translatable message
    message = _("Hello, world!")
    print(message)

    return render(request, 'base.html', {'message': message})