from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import LoginUserForm
from django.views.generic.edit import FormView, CreateView, UpdateView
from .forms import RegisterUserForm, UserPasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth import get_user_model
from .forms import ProfileUserForm
from django.http import HttpResponse


class LoginPage(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    extra_context = {'title': "Авторизация", 'form': form_class}

    def get_success_url(self):
        return reverse_lazy('main_url') # перенаправляет на имя по адрессу ПРОверьте setting.py


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('login')


class LogoutUser(LogoutView):
    next_page = reverse_lazy('main_url')




# Класс ProfileUser для отображения и редактирования профиля пользователя
class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()  # Используем модель пользователя
    form_class = ProfileUserForm  # Форма профиля пользователя
    template_name = 'profile.html'  # Шаблон для профиля пользователя
    extra_context = {'title': "Профиль пользователя"}# 'default_image': settings.DEFAULT_USER_IMAGE}

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        user = self.request.user

        response.set_cookie('cookienameuser', user, max_age=60 * 60 * 24)

        return response

    def get_extra_content(self, **kwargs):
        content = super().get_extra_content(**kwargs)
        cookie = self.request.COOKIES.get('cookienameuser')
        content['cookie_example'] = cookie
        return content
    # Метод для получения URL после успешного обновления профиля
    def get_success_url(self):
        return reverse_lazy('profile')

    # Метод для получения объекта текущего пользователя
    def get_object(self, queryset=None):
        user = self.request.user

        return user

class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'password_change_form.html'
    extra_context = {'title': "Изменение пароля"}

    def get_success_url(self):
        return reverse_lazy('password_change_done')