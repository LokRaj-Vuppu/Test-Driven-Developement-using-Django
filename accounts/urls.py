from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views as account_views


urlpatterns = [
    path("signup/", account_views.register, name="signup_page"),
    path("login/", account_views.login_view, name="login_page"),
    path("logout/", account_views.logout_view, name="logout"),
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="accounts/password_reset.html"
        ),
        name="password_reset",
    ),
    path(
        "password_reset_done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("current_user_profile/",account_views.current_user_profile, name="current_user_profile"),
    path('update_user_profile/',account_views.update_user_profile,name='update_user_profile'),

]
