from django.db import models
from pets.models import Product


class Feedback(models.Model):
    text = models.CharField(max_length=30)
    rating = models.IntegerField(default=0)# оценка
    image = models.ImageField(upload_to='feedback_images/', blank=True, null=True)# фото
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Product, default=1, on_delete=models.CASCADE )