from django.contrib import admin

from .models import Product, Category, Pet




admin.site.index_title = "Зоомагазин верный друг"

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pet', 'slug')

    list_display_links = ('id', 'title')
    list_filter = ('pet',)
    search_fields = ('id', 'title')  # Добавить возможность поиска по названию




from django.utils.translation import gettext_lazy as _  # Импорт функции для перевода строк

class AvailabilityFilter(admin.SimpleListFilter):
    title = _('наличие')  # Заголовок фильтра, переведенный на язык, установленный в настройках
    parameter_name = 'availability'  # Параметр фильтра, используемый в URL-адресе административной панели

    def lookups(self, request, model_admin):
        """
        Определение значений фильтрации для отображения в интерфейсе административной панели.
        Возвращается кортеж кортежей, где каждый кортеж состоит из пары (значение, отображаемое_имя).
        """
        return (
            ('in_stock', _('В наличии')),      # Параметр фильтра для товаров в наличии
            ('out_of_stock', _('Нет в наличии')),  # Параметр фильтра для товаров отсутствующих в наличии
        )

    def queryset(self, request, queryset):
        """
        Фильтрация queryset в зависимости от выбранного значения фильтра.
        """
        if self.value() == 'in_stock':  # Если выбран параметр 'in_stock'
            return queryset.filter(amount__gt=0)  # Возвращаем товары с количеством больше нуля
        if self.value() == 'out_of_stock':  # Если выбран параметр 'out_of_stock'
            return queryset.filter(amount__lte=0)  # Возвращаем товары с количеством меньше или равным нулю


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'price', 'amount')
    list_display_links = ('id',)
    list_editable = ('title', 'price', 'amount') # быстрое редактирование
    list_filter = ('category', AvailabilityFilter)  # Добавить фильтр по категории
    search_fields = ('title',)  # Добавить возможность поиска по названию
    ordering = ('-id',)  # Сортировать по убыванию ID



