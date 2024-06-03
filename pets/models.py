from django.db import models



class Pet(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.CharField(max_length=100,  null=True, verbose_name='слаг')

    class Meta:
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    pet = models.ForeignKey(Pet,  null=True ,blank=True, on_delete=models.CASCADE, verbose_name='питомец')


    slug = models.CharField(max_length=100,  null=True, verbose_name='слаг')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    image = models.ImageField(upload_to="products_images", blank=True, null=True, verbose_name='изображение')
    price = models.IntegerField(verbose_name='Цена')

    category = models.ForeignKey(Category,  null=True ,blank=True, on_delete=models.CASCADE, verbose_name='категория')
    slug = models.CharField(max_length=100,  null=True, verbose_name='слаг')

    amount = models.IntegerField(verbose_name='В наличии', default=0)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __repr__(self):
        return self.title