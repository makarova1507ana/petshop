from django.urls import path, re_path
from django.views.generic import TemplateView
from django.shortcuts import render
from django.conf.urls import handler404
import pets.views as pets

urlpatterns = [
    # path('', TemplateView.as_view(template_name='index.html',
    #                               extra_context={'name_product': 'name1'}),
    #      name="main_url"),
    path('', pets.Home.as_view(), name="main_url"),
    path('catalog/', pets.Catalog.as_view(), name="catalog"),

    path("categories/<slug:slug>/", pets.Category_Products.as_view(), name="categories"),
    path("product/<int:product_id>/", pets.Product_Detail.as_view(), name="product"),
]


