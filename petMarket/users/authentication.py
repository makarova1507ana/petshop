# users/authentication.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

# Класс EmailAuthBackend для аутентификации по E-mail
class EmailAuthBackend(BaseBackend):
    # Метод authenticate выполняет проверку E-mail и пароля
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()  # Получение модели пользователя
        try:
            # Пытаемся найти пользователя по E-mail
            user = user_model.objects.get(email=username)
            # Проверка пароля
            if user.check_password(password):
                return user  # Возвращаем пользователя при успешной проверке
            return None  # Возвращаем None, если пароль не подошел
        except (user_model.DoesNotExist, user_model.MultipleObjectsReturned):
            return None  # Возвращаем None, если пользователь не найден или найдено несколько

    # Метод get_user возвращает объект пользователя по его ID
    def get_user(self, user_id):
        user_model = get_user_model()  # Получение модели пользователя
        try:
            return user_model.objects.get(pk=user_id)  # Возвращаем пользователя по ID
        except user_model.DoesNotExist:
            return None  # Возвращаем None, если пользователь не найден