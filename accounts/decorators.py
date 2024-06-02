from django.shortcuts import redirect
from django.urls import reverse


def is_user_authenticated(view_func):
    def wrapper(request, *args, **kwargs):
        # Your custom logic goes here
        if request.user.is_authenticated:
            return redirect(reverse("homepage"))
        else:
            # Call the original view function
            return view_func(request, *args, **kwargs)

    # It's a good practice to maintain the original view function's attributes
    wrapper.__name__ = view_func.__name__
    wrapper.__doc__ = view_func.__doc__

    return wrapper
