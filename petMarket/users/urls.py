from django.urls import path, re_path
from django.contrib.auth.views import PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy

import users.views as users
urlpatterns = [

    path('login/', users.LoginPage.as_view(), name="login"),
    path('logout/', users.LogoutUser.as_view(), name="logout"),
    path('register/', users.RegisterUser.as_view(), name="register"),
    path('profile/', users.ProfileUser.as_view(), name="profile"),
    path('password-change/', users.UserPasswordChange.as_view(), name="password_change"),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name="password_change_done"),
    # Изменение пароля пользователя
    path('password-change/', users.UserPasswordChange.as_view(), name="password_change"),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"),
         name="password_change_done"),

    # Сброс пароля пользователя
    path('password-reset/',
         PasswordResetView.as_view(
             template_name="password_reset_form.html",
             email_template_name="password_reset_email.html",
             success_url=reverse_lazy("password_reset_done")
         ),
         name='password_reset'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(template_name="password_reset_done.html"),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name="password_reset_confirm.html",
             success_url=reverse_lazy("password_reset_complete")
         ),
         name='password_reset_confirm'),
    path('password-reset/complete/',
         PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),
         name='password_reset_complete'),
]