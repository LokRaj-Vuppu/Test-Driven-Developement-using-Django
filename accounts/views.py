from django.shortcuts import render, redirect
from accounts.forms import ProfileUpdateForm, UserRegistrationForm, UserUpdateForm
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from posts.models import Post
from django.contrib.auth.decorators import login_required
from accounts.decorators import is_user_authenticated
from django.conf import settings


@is_user_authenticated #custom decorator
def register(request):
    try:
        form = UserRegistrationForm()
        if request.method == "POST":
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse("login_page"))
                # redirect to login page
        return render(request, "accounts/register.html", {"form": form})
    except Exception as error:
        print(f"Exception in registering user - {error}")

 
@is_user_authenticated #custom decorator
def login_view(request):
    form = AuthenticationForm()
    # import pdb
    # pdb.set_trace()
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                from .tasks import send_login_mail
                send_login_mail.delay(
                    user_email = request.user.email,
                    sender = settings.EMAIL_HOST_USER,
                    subject = "Welcome!",
                    message = "Thank you for logging in. Welcome to our website!" 
                )

                return redirect(reverse("homepage"))

    context = {"form": form}
    return render(request, "accounts/login.html", context)


def logout_view(request):
    logout(request)
    return redirect(reverse("homepage"))


@login_required
def current_user_profile(request):
    user = request.user

    posts = Post.objects.filter(author=user).all()

    context = {"user": user, "posts": posts}

    return render(request, "accounts/currentuserprofile.html", context)


@login_required
def update_user_profile(request):
    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUpdateForm(instance=request.user.profile)

    if request.method == "POST":
        profile_form = ProfileUpdateForm(
            instance=request.user.profile,
            data={
                "bio": request.POST.get("bio", None),
                "address": request.POST.get("address", None),
            },
        )
        user_form = UserUpdateForm(
            instance=request.user,
            data={
                "first_name": request.POST.get("first_name", None),
                "last_name": request.POST.get("last_name", None),
                "username": request.POST.get("username", None),
            },
        )

        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()

            return redirect(reverse("current_user_profile"))

    context = {"profile_form": profile_form, "user_form": user_form}
    return render(request, "accounts/updateprofile.html", context)
