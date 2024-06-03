from datetime import datetime

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from .models import Product, Category, Pet
from feedback.models import Feedback


class Home(TemplateView):
    template_name = 'index.html'
    extra_context = {'name_product': 'name1',
                     'products': Product.objects.filter(amount=1)[:3]}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        feedbacks = Feedback.objects.filter(rating=5) # [Feedback(...,product), ...]
        products_highest_mark = set()
        for feedback in feedbacks:
            product_id = feedback.product.id #  feedback.product -> title
            product = Product.objects.get(id=product_id)
            products_highest_mark.add(product)
        context['products_highest_mark'] = products_highest_mark
        return context

class Catalog(ListView):
    model = Product
    template_name = 'catalog.html'
    context_object_name = 'products'  # 'products' - это ключ словаря
    paginate_by = 3


    def get_context_data(self, **kwargs):
        # Дополнительные данные для передачи в контекст (необязательно)
        context = super().get_context_data(**kwargs)
        context['pets'] = Pet.objects.all()
        return context



class Category_Products(ListView):
    model = Category
    template_name = 'products.html'
    context_object_name = 'categories'  # 'products' - это ключ словаря

    def render_to_response(self, context, **response_kwargs):
        if context['error'] == 'error':
            return render(self.request, '404.html',  context, **response_kwargs, status=404)
        return super().render_to_response(context, **response_kwargs)

    def get_context_data(self, **kwargs):
        # Дополнительные данные для передачи в контекст (необязательно)
        context = super().get_context_data(**kwargs)
        pets = Pet.objects.all()
        try:
            pet = Pet.objects.get(slug=self.kwargs['slug'])
            categories = Category.objects.filter(pet=pet.id)
            products = Product.objects.filter(category=pet.id)
            context['pets'] = pets
            context['pet'] = pet
            context['categories'] = categories
            context['products'] = products
            context['error'] = ''
        except:
            #self.template_name = '404.html' # временное решение

            #   raise Http404('') #
            context['error'] = 'error'
        return context

class Product_Detail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'  # Имя переменной в URL для первичного ключа

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.get(id=self.kwargs['product_id']) # заменить
        feedbacks = product.feedback_set.all()
        context['feedbacks'] = feedbacks
        return  context